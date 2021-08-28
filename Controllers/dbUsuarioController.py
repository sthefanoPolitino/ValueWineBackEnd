from ValueWIneBack.Services import dbUsuarioService
def insertUser(Nombre,Telefono,Rol,Direccion,Email,Password):
    #crear objeto
    response=dbUsuarioService.insertUser(Nombre,Telefono,Rol,Direccion,Email,Password)
    
    if response==False:
        return False
    return response

def loginUser(Email,Password):
    #crear objeto
    response=dbUsuarioService.login(Email,Password)
    if response==False:
        return False
    return response