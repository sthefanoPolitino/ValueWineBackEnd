from .Controllers import dbUsuarioController
from .utils.decorators import checktoken
from flask import request
from flask import Blueprint
from .Controllers import VinoController
vino=Blueprint('vino',__name__)
url='/vino'
@vino.route(''+url+'/insertVino',methods=['PUT'])
@checktoken
def InsertVino():
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
    redRedwine=req["Redwine"]
    reqResidualsugar=req["Residualsugar"]
    response=VinoController.insertVino(reqNombre,reqResidualsugar,reqVolatileAcidity,
                                       reqFixedAcidity,reqCitricAcid,reqFreeSulfurDioxide,
                                       reqChlorides,reqDensity,reqTotalSulfurDioxide,reqPH,
                                       reqSulphates,reqAlcohol,reqIdProductor,redRedwine)
    
    return response

@vino.route(''+url+'/deleteVino',methods=['DELETE'])
@checktoken
def deleteVino():
    req=request.args #trae los params en formato de dict
    response=VinoController.deleteVino(req["id"])
    return response

@vino.route(''+url+'/getVinosByIdProductor',methods=['GET'])
@checktoken
def getVinosByIdProductor():
    req=request.args #trae los params en formato de dict
    response=VinoController.getVinosByIdProductor(req["idProductor"])
    return response

@vino.route(''+url+'/predictionQuality',methods=['POST'])
@checktoken
def predictionQuality():
    req=request.args
    response=VinoController.predictionQuality(req["idVino"])
    return response

@vino.route(''+url+'/edit',methods=['PATCH'])
@checktoken
def editVino():
    req=request.get_json()
    args=request.args
    response=VinoController.editVino(args['id'],req["vino"])
    return response

@vino.route(''+url+'/getAllVinos',methods=['GET'])
@checktoken
def getAllVinos():
    response=VinoController.getAllVinos()
    return response
