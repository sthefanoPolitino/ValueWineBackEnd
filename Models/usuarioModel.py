class Usuario:
    def __init__(self,Nombre:str,Telefono:int,Rol:bool,Direccion:str,Email:str,Password:str):
        self.Nombre=Nombre
        self.Telefono=Telefono
        self.Rol=Rol
        self.Direccion=Direccion
        self.Email=Email
        self.Password=Password
    def __json__(self):
        return {"Nombre":self.Nombre,"Telefono":self.Telefono,"Rol":self.Rol,
                "Direccion":self.Direccion,"Email":self.Email,"Password":self.Password}
    
class UsuarioLogueado:
    
     def __init__(self,Rol:bool,Email:str,Token): 
        self.Rol=Rol,
        self.Email=Email,
        self.Token=Token
     def __json__(self):
        return {"Rol":self.Rol[0],"Email":self.Email[0],"Token":self.Token}
    