# ValueWIneBack
# AutoInstaller -> PuntoSalud

## Descripción
Micro-servicio creado para ser consumido por el frontend Mobile.


* **URL**= a definir 


## Guía de inicio
Para obtener una copia del proyecto se deberá hacer click en el botón "Clonar" y copiar la dirección ssh o https dependiendo si se tiene una clave ssh vinculada con el proyecto o no. Ejemplo de una dirección https es: "https://gitlab.com/itcsoluciones/autoinstallerback.git". Luego, se deberá clonar el proyecto con el comando "git clone + la dirección https copiada", luego hay que abrir una terminal en la dirección del proyecto, ejecutar "git checkout + el nombre de la rama a la que se quiere ir".

Instalar dependencias:
pip install -r requirements.txt

Poner a correr entornos virtuales
source venv/bin/activate

Correr el servidor accesible desde localhost
export FLASK_APP=app/__init__.py 
flask run --host=0.0.0.0

## Requisitos
Para poder ver la librería se necesitará tener instalado Git para poder clonarse el proyecto.

### Configuración
Es necesario configurar las siguientes variables de entorno

*USERDB=root
*PASSDB=root
*HOSTDB=localhost
*PORTHOSTDB=3307
*KEY=qJdkOKZkOPxxeIYgi1l0kAJMlHtVN9oKAjIH0gsQ


## APIs ValueWineBack

### Usuario 

### PUT Insertar Usuario

Nos conectamos con mysql para insertar un Usuario

#### URL
```
${URL}/usuario/insertUsuario
```

#### BODY

{"nombre":"Prueba","direccion":"CalleDePrueba123","rol":0,"telefono":12345,"email":"prueba@user.com","password":"1234"}

### GET LOGIN Usuario

Nos conectamos con mysql para loguear a un Usuario y devolverle un jwt si existe ese usuario en la DB

#### URL
```
${URL}/usuario/loginUsuario
```

#### BODY

{"email":"prueba@user.com","password":"1234"}

### GET Check Sesion

Recibe un token el el header y chequea si esta expirado, y luego si el secret coincide

#### URL
```
${URL}/usuario/checkSesion
```

#### HEADER

Bearer Token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InBydWViYUB1c2VyLmNvbSIsInJvbCI6MCwiZXhwIjoxNjMwNjIwMjMyfQ.b2AMUJymtNu5ewOgH-_Xc3J58WkRtQUw9l_2Fm0MTI0

### Vino

### PUT Insert Vino

Nos conectamos con mysql insertamos un Vino

#### URL
```
${URL}/vino/insertVino
```
#### HEADER

Bearer Token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InBydWViYUB1c2VyLmNvbSIsInJvbCI6MCwiZXhwIjoxNjMwNjIwMjMyfQ.b2AMUJymtNu5ewOgH-_Xc3J58WkRtQUw9l_2Fm0MTI0

#### BODY

{
    "nombre":"vino de prueba", "VolatileAcidity":1,"FixedAcidity":2,"CitricAcid":2,"FreeSulfurDioxide":0,
    "Chlorides":1,"Density":0.3,"TotalSulfurDioxide":0.6,"PH":0.7,"Sulphates":1, "Alcohol":1.2,"Quality":1.2,"idProductor":2
}

### GET Vinos By id Productor

Nos conectamos con mysql para buscar vinos de un productor por su ID

#### URL
```
${URL}/vino/getVinosByIdProductor?idProductor=2
```
#### HEADER

Bearer Token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InBydWViYUB1c2VyLmNvbSIsInJvbCI6MCwiZXhwIjoxNjMwNjIwMjMyfQ.b2AMUJymtNu5ewOgH-_Xc3J58WkRtQUw9l_2Fm0MTI0

#### Params

idProductor 2, concatenarlo en la url
