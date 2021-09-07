from werkzeug.datastructures import RequestCacheControl
from flask import request
from flask import Blueprint, render_template, abort
from ValueWIneBack import VinoController
vino=Blueprint('vino',__name__)
url='/vino'
@vino.route(''+url+'/insertVino',methods=['PUT'])
def InsertUser():
    req=RequestCacheControl.get_json()
    reqNombre=req["nombre"]
    reqVolatileAcidity=req["VolatileAcidity"],
    reqFixedAcidity=req["FixedAcidity"],
    reqCitricAcid=req["CitricAcid"],
    reqFreeSulfurDioxide=req["FreeSulfurDioxide"],
    reqChlorides=req["Chlorides"],
    reqDensity=req["Density"],
    reqTotalSulfurDioxide=req["TotalSulfurDioxide"],
    reqPH=req["PH"],
    reqSulphates=req["Sulphates"],
    reqAlcohol=req["Alcohol"],
    reqQuality=req["Quality"]
    reqIdProductor=req["idProductor"]
    response=VinoController.insertVino()
    print(response)
    if response == 500:
        return Controllererrors.make_error(500,"No se pudo insertar a DB")
    if response == 501:
        return Controllererrors.make_error(500,"Email existente")
    return Controllerresponses.make_response(200,"Usuario Creado correctamente")