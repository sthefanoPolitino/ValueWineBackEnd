from .dbUsuarioService import get_db
from ..Models.vinoModel import vino
def insertVino(vino):
    print(vino)
    DB,c=get_db()
    if DB==False:
        return 500;
    try:
        query=("INSERT INTO Vino "
                    "(Nombre, VolatileAcidity, FixedAcidity, CitricAcid"
                    ",FreeSulfurDioxide,Chlorides,Density,TotalSulfurDioxide,PH,Sulphates,Alcohol,Quality,IdProductor)"
                    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        c.execute(query,(vino["Nombre"],vino["VolatileAcidity"],vino["FixedAcidity"]
               ,vino["CitricAcid"],vino["FreeSulfurDioxide"],vino["Chlorides"],vino["Density"], 
               vino["TotalSulfurDioxide"],vino["PH"],vino["Sulphates"],vino["Alcohol"]
               ,vino["Quality"],vino["IdProductor"]))
        status=DB.commit();
        c.close()
        DB.close()
        print("vino insertado")
        return 200
    except Exception as e:
        print(e)
        return 500
    return ""

def getVinosByIdProductor(id):
    DB,c=get_db()
    if DB==False:
        return 500;
    try:
        query=("SELECT * from Vino WHERE idProductor = %s")
        c.execute(query,(id,))
        vinos=c.fetchall()
        if len(vinos) is 0:
            return 404 
        c.close()
        DB.close()
        return vinos
    except Exception as e:
        print(e)
        return 500
    return ""
    
def deleteVino(id):
    DB,c=get_db()
    if DB==False:
        return 500;
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
        return 500
    return ""