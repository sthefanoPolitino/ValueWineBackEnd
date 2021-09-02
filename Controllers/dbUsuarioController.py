from ValueWIneBack.Services import dbUsuarioService
from ValueWIneBack.Models import usuarioModel
import json
import os
import jwt,datetime
import hashlib
def insertUser(Nombre,Telefono,Rol,Direccion,Email,Password):
    crypPass=hashlib.md5()
    crypPass.update(Password.encode("utf-8"))
    usuario=usuarioModel.Usuario(Nombre,Telefono,Rol,Direccion,Email,crypPass.hexdigest())
    user=usuario.__json__()
    response=dbUsuarioService.insertUser(user["Nombre"],user["Telefono"],user["Rol"]
                                         ,user["Direccion"],user["Email"],user["Password"])
    return response

def loginUser(Email,Password):
    #crear objeto
    crypPass=hashlib.md5()
    crypPass.update(Password.encode("utf-8"))
    response=dbUsuarioService.login(Email,crypPass.hexdigest())
    if response==False:
        return False
    return response


def checkSesionRefreshtoken(token):
    secret=os.getenv("KEY")
    try:
        decodeToken=jwt.decode(token, secret, algorithms="HS256")
        print("Token is still valid and active")
        payload={"email":decodeToken["email"],
                 "rol":decodeToken["rol"],
                 "exp": datetime.datetime.utcnow()+datetime.timedelta(seconds=30)}
        token=jwt.encode(payload, secret, algorithm="HS256")
        return token;
    except jwt.ExpiredSignatureError:
        return 518;
    except jwt.InvalidTokenError as e:
        return 401;
    
def checkSesion(token):
    secret=os.getenv("KEY")
    try:
        decodeToken=jwt.decode(token, secret, algorithms="HS256")
        print("Token is still valid and active")
        return 200;
    except jwt.InvalidTokenError as e:
        return 401;