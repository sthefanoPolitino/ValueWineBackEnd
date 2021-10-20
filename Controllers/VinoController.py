from werkzeug.wrappers import response
from ..Models.vinoModel import vino
from ..Services import dbVinoService
# Imports necesarios
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
def insertVino(Nombre,Residualsugar,VolatileAcidity,FixedAcidity,CitricAcid,
               FreeSulfurDioxide,Chlorides,Density,
    TotalSulfurDioxide, PH,Sulphates,Alcohol,IdProductor,redwine):
    vinoObj=vino(Nombre,Residualsugar,VolatileAcidity,FixedAcidity,CitricAcid
                 ,FreeSulfurDioxide,Chlorides,Density,TotalSulfurDioxide,PH,Sulphates,
                 Alcohol,None,IdProductor,redwine)
    
    response=dbVinoService.insertVino(vinoObj.__json__())
    return response

def getVinosByIdProductor(id):
    response=dbVinoService.getVinosByIdProductor(id)
    return response

def deleteVino(id):
    response=dbVinoService.deleteVino(id)
    return response

def predictionQuality(id):
    response=dbVinoService.insertpredictionQuality(id)
    return response

