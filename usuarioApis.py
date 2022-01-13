import json
from flask import Blueprint
from flask import request
from ValueWIneBack.Controllers import dbUsuarioController

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
    return response

@usuario.route(''+url+'/loginUsuario',methods=['POST'])
def LoginUser():
    req=request.get_json();
    reqEmail=req['email']
    reqPassword=req['password']
    response=dbUsuarioController.loginUser(reqEmail,reqPassword)
    return response

@usuario.route(''+url+'/checkSesion',methods=['GET'])
def checkSesion():
    req1=request.headers
    #req=request.get_json();
    #reqToken=req['token']
    response=dbUsuarioController.checkSesionRefreshtoken(req1)
    if response==518:
        return dbUsuarioController.makeError("Sesion expirado",None,518)
    elif response==401:
        return dbUsuarioController.makeError("No estas autorizado",None,401)
    return dbUsuarioController.makeResponseSuccess("Token valido",200,"token",response)