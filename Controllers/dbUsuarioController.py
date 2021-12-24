from ValueWIneBack.Models.response import response
from ValueWIneBack.Services import dbUsuarioService
from ValueWIneBack.Models import usuarioModel
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
    if(response==501):
        return makeError("Email existente",None,501)
    elif(type(response)==str):
        return makeError("Error interno, error: ",response,500)
    return makeResponseSuccess("Usuario creado Correctamente",200,None,None)

def loginUser(Email,Password):
    #crear objeto
    crypPass=hashlib.md5()
    crypPass.update(Password.encode("utf-8"))
    response=dbUsuarioService.login(Email,crypPass.hexdigest())
    if(type(response)==str):
        return makeError("Error interno, error: ",response,500)
    elif(response==206):
        return makeError("Usuario no existente",None,206)
    return response


def checkSesionRefreshtoken(headers):
    secret=os.getenv("KEY")
    try:
        reqHeaders=headers["Authorization"] #obtenemos el authorization dentro de los headers
        token=str(reqHeaders).replace("Bearer ","")
    except:
        return 401
    try:
        decodeToken=jwt.decode(token, secret, algorithms="HS256")
        print("Token is still valid and active")
        payload={"email":decodeToken["email"],
                 "rol":decodeToken["rol"],
                 "exp": datetime.datetime.utcnow()+datetime.timedelta(seconds=30)}
        token=jwt.encode(payload, secret, algorithm="HS256")
        return token
    except jwt.ExpiredSignatureError:
        return 518
    except jwt.InvalidTokenError as e:
        return 401
    
def makeError(msg,e,code):
    if(e):
        errorObj=response(msg + str(e),code)
    else:
        errorObj=response(msg,code)
    return errorObj.__json__()
def makeResponseSuccess(msg,code,nombreEtiqueta,value):
    print("valores",value,nombreEtiqueta)
    if(value):
        Obj=response(msg,code,nombreEtiqueta,value)
    else:
        Obj=response(msg,code)
    return Obj.__json__(value)