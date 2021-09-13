from ..Models.vinoModel import vino
from ..Services import dbVinoService
def insertVino(Nombre,VolatileAcidity,FixedAcidity,CitricAcid,
               FreeSulfurDioxide,Chlorides,Density,
    TotalSulfurDioxide, PH,Sulphates,Alcohol,Quality,IdProductor):
    print(Nombre,VolatileAcidity,FixedAcidity,CitricAcid
                 ,FreeSulfurDioxide,Chlorides,Density,TotalSulfurDioxide,PH,Sulphates,
                 Alcohol,Quality,IdProductor)
    vinoObj=vino(Nombre,VolatileAcidity,FixedAcidity,CitricAcid
                 ,FreeSulfurDioxide,Chlorides,Density,TotalSulfurDioxide,PH,Sulphates,
                 Alcohol,Quality,IdProductor)
    response=dbVinoService.insertVino(vinoObj.__json__())
    return response