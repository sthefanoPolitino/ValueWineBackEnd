from ValueWIneBack.Services import dbUsuarioService
from ValueWIneBack.Models import usuarioModel
import json
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

def checkSesion(token):
    response=dbUsuarioService.checkSesion(token)
    return response