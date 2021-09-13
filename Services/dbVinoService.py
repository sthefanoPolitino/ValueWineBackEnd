from .dbUsuarioService import get_db

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
        return 500
    return ""