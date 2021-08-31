class Usuario:
    def __init__(self,Nombre:str,Telefono:int,Rol:bool,Direccion:str,Email:str,Password:str):
        self.Nombre=Nombre,
        self.Telefono=Telefono,
        self.Rol=Rol,
        self.Direccion=Direccion,
        self.Email=Email,
        self.Password=Password,
    def __json__(self):
        return {"Nombre":self.Nombre[0],"Telefono":self.Telefono[0],"Rol":self.Rol[0],
                "Direccion":self.Direccion[0],"Email":self.Email[0],"Password":self.Password[0]}
    
class UsuarioLogueado:
    
     def __init__(self,Rol:bool,Email:str,Token): 
        self.Rol=Rol,
        self.Email=Email,
        self.Token=Token
     def __json__(self):
        return {"Rol":self.Rol[0],"Email":self.Email[0],"Token":self.Token}
    