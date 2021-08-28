import mysql.connector
import os
from dotenv import load_dotenv
import jwt
load_dotenv()
def get_db():
    user=os.getenv('USERDB')
    password=os.getenv('PASSDB')
    host=os.getenv('HOSTDB')
    port=os.getenv('PORTHOSTDB')
    try:
        db = mysql.connector.connect(user=user, password=password,
                              host=host,
                              database='valuewine',port=int(port))
        cursor=db.cursor(dictionary=True)
        print('DB conectada')
        return db,cursor
    except Exception as e:
        print("problema al acceder a la DB",e)
        return False;
    
def insertUser(Nombre,Telefono,Rol,Direccion,Email,Password):
    DB,c=get_db()
    
    if DB==False:
        return False;
    try:
        query=("INSERT INTO Usuario "
                    "(Nombre, Telefono, Rol, Direccion,Email,Password)"
                    "VALUES (%s, %s, %s, %s,%s,%s)")
        c.execute(query,(Nombre,Telefono,Rol,Direccion,Email,Password))
        status=DB.commit();
        c.close()
        DB.close()
        print("insertado")
        return status
    except Exception as e:
        print(e)
        return False
    
def login(email,ps):
    #trabajar en que la pass se debe desencriptar
    secret=os.getenv("KEY")
    DB,c=get_db()
    if DB==False:
        return False;
    try:
        query=("SELECT * FROM Usuario "
               "WHERE Email = %s AND Password = %s")
        c.execute(query,(email,ps))
        user=c.fetchone()
        if user is None:
           return None 
        c.close()
        DB.close()
        print(user,type(user))
        payload={"email":email,
                 "rol":user["Rol"]}
        token=jwt.encode(payload, secret, algorithm="HS256")
        print("encontrado")
        return token
    except Exception as e:
        print(e)
        return False