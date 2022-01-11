from ValueWIneBack.Controllers import dbUsuarioController
from flask import request
from flask import Blueprint
from ValueWIneBack.Controllers import VinoController
vino=Blueprint('vino',__name__)
url='/vino'
@vino.route(''+url+'/insertVino',methods=['PUT'])
def InsertVino():
    
    req1=request.headers
    respCheckToken=dbUsuarioController.checkSesionRefreshtoken(req1)
    if respCheckToken == 401:
            return VinoController.makeError("No estas autorizado",None,401)
    if respCheckToken == 518:
        return VinoController.makeError("Token expirado",None,401)
    
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
def deleteVino():
    req1=request.headers #trae todos los headers
    respCheckToken=dbUsuarioController.checkSesionRefreshtoken(req1)
    if respCheckToken == 401:
            return VinoController.makeError("No estas autorizado",None,401)
    if respCheckToken == 518:
        return VinoController.makeError("Token expirado",None,401)
    req=request.args #trae los params en formato de dict
    response=VinoController.deleteVino(req["id"])
    return response

@vino.route(''+url+'/getVinosByIdProductor',methods=['GET'])
def getVinosByIdProductor():
    req1=request.headers #trae todos los headers
    respCheckToken=dbUsuarioController.checkSesionRefreshtoken(req1)
    if respCheckToken == 401:
            return VinoController.makeError("No estas autorizado",None,401)
    if respCheckToken == 518:
        return VinoController.makeError("Token expirado",None,401)
    req=request.args #trae los params en formato de dict
    response=VinoController.getVinosByIdProductor(req["idProductor"])
    return response

@vino.route(''+url+'/predictionQuality',methods=['POST'])
def predictionQuality():
    req1=request.headers #trae todos los headers
    respCheckToken=dbUsuarioController.checkSesionRefreshtoken(req1)
    if respCheckToken == 401:
            return VinoController.makeError("No estas autorizado",None,401)
    if respCheckToken == 518:
        return VinoController.makeError("Token expirado",None,401)
    req=request.args
    response=VinoController.predictionQuality(req["idVino"])
    return response
