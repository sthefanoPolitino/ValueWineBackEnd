from flask import Flask
from . import usuarioApis
from . import vinoApis
from .Services.dbService import createSchema
app = Flask(__name__)
app.register_blueprint(usuarioApis.usuario)
app.register_blueprint(vinoApis.vino)

# Creacion de las tablas de vino e usuario
createSchema()


@app.route("/")
def hello_world():
    return "Iniciado el microservicio"
