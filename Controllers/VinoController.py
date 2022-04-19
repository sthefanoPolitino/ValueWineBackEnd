from flask import jsonify
from ..Models.response import response
from ..Models.vinoModel import vino
from ..Services import dbVinoService
# Imports necesarios
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
def insertVino(Nombre,Residualsugar,VolatileAcidity,FixedAcidity,CitricAcid,
               FreeSulfurDioxide,Chlorides,Density,
    TotalSulfurDioxide, PH,Sulphates,Alcohol,IdProductor,redwine):
    vinoObj=vino(Nombre,Residualsugar,VolatileAcidity,FixedAcidity,CitricAcid
                 ,FreeSulfurDioxide,Chlorides,Density,TotalSulfurDioxide,PH,Sulphates,
                 Alcohol,None,IdProductor,redwine)
    
    response=dbVinoService.insertVino(vinoObj.__json__())
    if type(response)==str:
        return makeError("Error interno error: ",response,500)
    elif response==200:
        return makeResponseSuccess("Vino insertado correctamente",200,None,None)
    return response

def getVinosByIdProductor(id):
    response=dbVinoService.getVinosByIdProductor(id)
    if response==404:
        return makeError("No existe ese id de productor o el productor no tiene vinos",None,404)
    elif type(response)==str:
        return makeError("Error interno, error: ",response,500)
    return makeResponseSuccess("Vinos encontrados correctamente",200,"vinos",response)

def deleteVino(id):
    response=dbVinoService.deleteVino(id)
    if response==404:
        return makeError("No existe ese vino",None,404)
    elif type(response)==str:
        return makeError("Error interno, error: ",response,500)
    return makeResponseSuccess("Vino eliminado correctamente",200,None,None)

def predictionQuality(id):
    response=dbVinoService.insertpredictionQuality(id)
    if response==404:
        return makeError("No existe ese vino",None,404)
    elif type(response)==str:
        return makeError("Error interno, error: ",response,500)
    return makeResponseSuccess("Vino actualizado correctamente",200,"vino",response)

def makeError(msg,e,code):
    if(e):
        errorObj=response(msg + str(e),code)
    else:
        errorObj=response(msg,code)
    return errorObj.__json__()
def makeResponseSuccess(msg,code,nombreEtiqueta,value):
    if(value):
        Obj=response(msg,code,nombreEtiqueta,value)
    else:
        Obj=response(msg,code)
    return Obj.__json__(value)

def editVino(id,nuevoVino):
    vinoObj=vino(nuevoVino["nombre"],nuevoVino['Residualsugar'],nuevoVino['VolatileAcidity'],nuevoVino['FixedAcidity'],nuevoVino['CitricAcid']
                 ,nuevoVino['FreeSulfurDioxide'],nuevoVino['Chlorides'],nuevoVino['Density'],nuevoVino['TotalSulfurDioxide'],nuevoVino['PH'],nuevoVino['Sulphates'],
                 nuevoVino['Alcohol'],None,nuevoVino['idProductor'],nuevoVino['Redwine'])

    response=dbVinoService.editVino(id,vinoObj.__json__())
    if response==404:
            return makeError("No existe ese vino",None,404)
    elif type(response)==str:
        return makeError("Error interno, error: ",response,500)
    return makeResponseSuccess("Vino actualizado correctamente",200,"vino",response)

def getAllVinos():
    resp=dbVinoService.getAllVinos()
    if type(resp)==str:
        return makeError("Error interno, error: ",resp,500)
    print(resp)
    return jsonify({"msg":"Vinos obtenidos correctamente","code":200,str("vinos"):resp})