from flask import Blueprint, render_template, abort
from flask import request
from flask.json import jsonify
from werkzeug.datastructures import Authorization
from ValueWIneBack.Controllers import dbUsuarioController
from ValueWIneBack.Errors import Controllererrors
from ValueWIneBack.Responses import Controllerresponses
import json
usuario=Blueprint('usuario',__name__)
url='/usuario'
@usuario.route(''+url+'/insertUsuario',methods=['PUT'])
def InsertUser():
    req=request.get_json()
    reqNombre=req["nombre"]
    reqDireccion=req["direccion"]
    reqRol=req["rol"]
    reqTelefono=req["telefono"]
    reqEmail=req["email"]
    reqPassword=req['password']
    response=dbUsuarioController.insertUser(reqNombre,reqTelefono,reqRol,reqDireccion,reqEmail,reqPassword)
    if response is False:
        return Controllererrors.make_error(500,"No se pudo insertar a DB")
    if response is None:
        return Controllererrors.make_error(500,"Email existente")
    return Controllerresponses.make_response(200,"Usuario Creado correctamente")

@usuario.route(''+url+'/loginUsuario',methods=['GET'])
def LoginUser():
    req=request.get_json();
    reqEmail=req['email']
    reqPassword=req['password']
    response=dbUsuarioController.loginUser(reqEmail,reqPassword)
    if response is False:
         return Controllererrors.make_error(500,"No se pudo buscar a DB")
    if response is None:
         return Controllererrors.make_error(404,"Usuario o Contraseña incorrectas")
    return response

@usuario.route(''+url+'/checkSesion',methods=['GET'])
def checkSesion():
    req1=request.headers["Authorization"]
    token=str(req1).replace("Bearer ","")
    print(token)
    #req=request.get_json();
    #reqToken=req['token']
    response=dbUsuarioController.checkSesion(token)
    if response is False:
        return Controllererrors.make_error(401,"Esta nunca se logueo o esta deslogueado")
    return Controllerresponses.make_response(200,"Esta logueado")