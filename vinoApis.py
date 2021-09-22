from ValueWIneBack.Controllers import dbUsuarioController
from flask import request
from ValueWIneBack.Errors import Controllererrors
from ValueWIneBack.Responses import Controllerresponses
from flask import Blueprint, render_template, abort
from ValueWIneBack.Controllers import VinoController
vino=Blueprint('vino',__name__)
url='/vino'
@vino.route(''+url+'/insertVino',methods=['PUT'])
def InsertVino():
    req1=request.headers
    respCheckToken=dbUsuarioController.checkSesionRefreshtoken(req1)
    if respCheckToken == 401:
            return Controllererrors.make_error(401,"No estas autorizado")
    if respCheckToken == 518:
        return Controllererrors.make_error(401,"Token expirado")
    
    req=request.get_json()
    reqNombre=req["nombre"]
    reqVolatileAcidity=req["VolatileAcidity"]
    reqFixedAcidity=req["FixedAcidity"]
    reqCitricAcid=req["CitricAcid"]
    reqFreeSulfurDioxide=req["FreeSulfurDioxide"]
    reqChlorides=req["Chlorides"]
    reqDensity=req["Density"]
    reqTotalSulfurDioxide=req["TotalSulfurDioxide"]
    reqPH=req["PH"]
    reqSulphates=req["Sulphates"]
    reqAlcohol=req["Alcohol"]
    reqIdProductor=req["idProductor"]
    response=VinoController.insertVino(reqNombre,reqVolatileAcidity,
                                       reqFixedAcidity,reqCitricAcid,reqFreeSulfurDioxide,
                                       reqChlorides,reqDensity,reqTotalSulfurDioxide,reqPH,
                                       reqSulphates,reqAlcohol,reqIdProductor)
    print(response,"aca")
    if response == 500:
        return Controllererrors.make_error(500,"No se pudo insertar en DB")
    return Controllerresponses.make_response(200,"Vino Creado correctamente")

@vino.route(''+url+'/deleteVino',methods=['DELETE'])
def deleteVino():
    req1=request.headers #trae todos los headers
    respCheckToken=dbUsuarioController.checkSesionRefreshtoken(req1)
    if respCheckToken == 401:
            return Controllererrors.make_error(401,"No estas autorizado")
    if respCheckToken == 518:
        return Controllererrors.make_error(401,"Token expirado")
    req=request.args #trae los params en formato de dict
    response=VinoController.deleteVino(req["id"])
    print(response)
    if response == 500:
        return Controllererrors.make_error(500,"No se buscar en DB")
    if response == 404:
        return Controllererrors.make_error(404,"No existe ese vino")
    return Controllerresponses.make_response(200,"Vino eliminado correctamente")

@vino.route(''+url+'/getVinosByIdProductor',methods=['GET'])
def getVinosByIdProductor():
    req1=request.headers #trae todos los headers
    respCheckToken=dbUsuarioController.checkSesionRefreshtoken(req1)
    if respCheckToken == 401:
            return Controllererrors.make_error(401,"No estas autorizado")
    if respCheckToken == 518:
        return Controllererrors.make_error(401,"Token expirado")
    req=request.args #trae los params en formato de dict
    response=VinoController.getVinosByIdProductor(req["idProductor"])
    print(response)
    if response == 500:
        return Controllererrors.make_error(500,"No se buscar en DB")
    if response == 404:
        return Controllererrors.make_error(404,"No existe ese id de productor o el productor no tiene vinos")
    return {"vinos":response}

@vino.route(''+url+'/predictionQuality',methods=['POST'])
def predictionQuality():
    req1=request.headers #trae todos los headers
    respCheckToken=dbUsuarioController.checkSesionRefreshtoken(req1)
    if respCheckToken == 401:
            return Controllererrors.make_error(401,"No estas autorizado")
    if respCheckToken == 518:
        return Controllererrors.make_error(401,"Token expirado")
    req=request.args
    response=VinoController.predictionQuality(req["idVino"])
    print(response)
    if response == 500:
        return Controllererrors.make_error(500,"No se buscar en DB")
    if response == 404:
        return Controllererrors.make_error(404,"No existe ese vino")
    return {"vino":response}
