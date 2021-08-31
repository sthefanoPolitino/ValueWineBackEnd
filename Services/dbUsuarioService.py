import mysql.connector
import os
from ValueWIneBack.Models import usuarioModel
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
        print("problema al acceder a la DB")
        return False;
    
def insertUser(Nombre,Telefono,Rol,Direccion,Email,Password):
    DB,c=get_db()
    if DB==False:
        return False;
    resp=getUser(Email)
    print(resp)
    if resp == True: #controla que no exista ese email en la db para no volver a insertarlo
        return None
    try:
        query=("INSERT INTO Usuario "
                    "(Nombre, Telefono, Rol, Direccion,Email,Password)"
                    "VALUES (%s, %s, %s, %s,%s,%s)")
        c.execute(query,(Nombre,Telefono,Rol,Direccion,Email,Password))
        status=DB.commit();
        c.close()
        DB.close()
        print("insertado")
        return True
    except Exception as e:
        
        return False
    
def login(email,ps):
    secret=os.getenv("KEY")
    DB,c=get_db()
    print(ps)
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
        payload={"email":email,
                 "rol":user["Rol"]}
        token=jwt.encode(payload, secret, algorithm="HS256")
        usuario=usuarioModel.UsuarioLogueado(user["Rol"],user["Email"],token)
        return usuario.__json__()
    except Exception as e:
        
        return False
    
    
def checkSesion(token):
    secret=os.getenv("KEY")
    try:
        decodeToken=jwt.decode(token, secret, algorithms="HS256")
        print("Token is still valid and active")
        return True;
    except jwt.InvalidTokenError as e:
        return False;
    
def getUser(email):
    DB,c=get_db()
    if DB==False:
        return False;
    query=("SELECT * FROM Usuario "
               "WHERE Email = %s")
    c.execute(query,(email,))
    user=c.fetchone()
    c.close()
    DB.close()
    if user != None:
        return True 
    return None