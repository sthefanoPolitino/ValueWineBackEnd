from .dbUsuarioService import get_db
from ..Controllers import Prediction


def insertVino(vino):
    print(vino)
    DB,c=get_db()
    if DB==False:
        return str(c) 
    try:
        
        query=("INSERT INTO Vino "
                    "(Nombre,Residualsugar,VolatileAcidity, FixedAcidity, CitricAcid"
                    ",FreeSulfurDioxide,Chlorides,Density,TotalSulfurDioxide,PH,Sulphates,Alcohol,Quality,IdProductor,Redwine)"
                    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        c.execute(query,(vino["Nombre"],vino["Residualsugar"],vino["VolatileAcidity"],vino["FixedAcidity"]
               ,vino["CitricAcid"],vino["FreeSulfurDioxide"],vino["Chlorides"],vino["Density"], 
               vino["TotalSulfurDioxide"],vino["PH"],vino["Sulphates"],vino["Alcohol"]
               ,vino["Quality"],vino["IdProductor"],vino["Redwine"]))
        status=DB.commit();
        c.close()
        DB.close()
        print("vino insertado")
        return 200
    except Exception as e:
        print(e)
        return str(e)
    

def getVinosByIdProductor(id):
    DB,c=get_db()
    if DB==False:
        return str(c);
    try:
        query=("SELECT * from Vino WHERE idProductor = %s")
        c.execute(query,(id,))
        vinos=c.fetchall()
        for vino in vinos:
            if vino["Redwine"]==1:
                vino["Redwine"]=True
            elif vino["Redwine"]==0:
                vino["Redwine"]=False    
        if len(vinos) is 0:
            return 404 
        c.close()
        DB.close()
        return vinos
    except Exception as e:
        print(e)
        return str(e)
    
def deleteVino(id):
    DB,c=get_db()
    if DB==False:
        return str(c);
    try:
        query=("DELETE  from Vino WHERE id = %s")
        c.execute(query,(id,))
        status=DB.commit();
        print(c.rowcount,"aca")
        if c.rowcount==0:
            return 404
        c.close()
        DB.close()
        return 200
    except Exception as e:
        print(e)
        return str(e)
    

def insertpredictionQuality(id):
    DB,c=get_db()
    if DB==False:
        return str(c);
    #busca el vino a predecir en la db
    vinoApredecir={}
    result=None
    try:
        c.execute("SELECT * From Vino Where id = %s",(id,))
        vinoApredecir=c.fetchone()
        if(vinoApredecir==None):
            return 404 
        result=Prediction.prediccion(vinoApredecir)
    except Exception as e:
        return str(e)
    #hace update del vino hiciste la prediccion
    try:
        query=("UPDATE Vino SET Quality=%s WHERE id = %s")
        c.execute(query,(result,id,))
        status=DB.commit();
    except Exception as e:
        return str(e)
    try:
        queryGetVino=("SELECT * from Vino WHERE id = %s")
        c.execute(queryGetVino,(id,))
        vino=c.fetchone()
        c.close()
        DB.close()
        return vino
    except Exception as e:
        print(e)
        return str(e)

