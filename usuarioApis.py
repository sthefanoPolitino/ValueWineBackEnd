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
    print(response)
    if response == 500:
        return Controllererrors.make_error(500,"No se pudo insertar a DB")
    if response == 501:
        return Controllererrors.make_error(500,"Email existente")
    return Controllerresponses.make_response(200,"Usuario Creado correctamente")

@usuario.route(''+url+'/loginUsuario',methods=['GET'])
def LoginUser():
    req=request.get_json();
    reqEmail=req['email']
    reqPassword=req['password']
    response=dbUsuarioController.loginUser(reqEmail,reqPassword)
    if response == 500:
         return Controllererrors.make_error(500,"No se pudo buscar a DB")
    if response == 404:
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
    print(response)
    if response == 401:
        return Controllererrors.make_error(401,"Token incorrecto o expirado")
    return Controllerresponses.make_response(200,"Esta logueado, Token valido")