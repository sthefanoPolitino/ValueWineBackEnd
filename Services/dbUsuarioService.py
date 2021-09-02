import mysql.connector
import os
from ValueWIneBack.Models import usuarioModel
from dotenv import load_dotenv
import jwt,datetime
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
    except:
        print("problema al acceder a la DB")
        return False,False
    
def insertUser(Nombre,Telefono,Rol,Direccion,Email,Password):
    DB,c=get_db()
    if DB==False:
        return 500;
    resp=getUser(Email)
    if resp == True: #controla que no exista ese email en la db para no volver a insertarlo
        return 501
    try:
        query=("INSERT INTO Usuario "
                    "(Nombre, Telefono, Rol, Direccion,Email,Password)"
                    "VALUES (%s, %s, %s, %s,%s,%s)")
        c.execute(query,(Nombre,Telefono,Rol,Direccion,Email,Password))
        status=DB.commit();
        c.close()
        DB.close()
        print("insertado")
        return 200
    except Exception as e:
        return 500
    
def login(email,ps):
    secret=os.getenv("KEY")
    DB,c=get_db()
    print(ps)
    if DB==False:
        return 500;
    try:
        query=("SELECT * FROM Usuario "
               "WHERE Email = %s AND Password = %s")
        c.execute(query,(email,ps))
        user=c.fetchone()
        if user is None:
           return 404 
        c.close()
        DB.close()
        print(datetime.datetime.now()+datetime.timedelta(seconds=60))
        payload={"email":email,
                 "rol":user["Rol"],
                 "exp": datetime.datetime.utcnow()+datetime.timedelta(seconds=30)}
        token=jwt.encode(payload, secret, algorithm="HS256")
        usuario=usuarioModel.UsuarioLogueado(user["Rol"],user["Email"],token)
        return usuario.__json__()
    except Exception as e:
        
        return 500
    
    

    
def getUser(email):
    DB,c=get_db()
    query=("SELECT * FROM Usuario "
               "WHERE Email = %s")
    c.execute(query,(email,))
    user=c.fetchone()
    c.close()
    DB.close()
    if user != None:
        return True 
    return None