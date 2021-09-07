from flask import Flask
from ValueWIneBack import usuarioApis
from ValueWIneBack import vinoApis
app = Flask(__name__)
app.register_blueprint(usuarioApis.usuario)
app.register_blueprint(vinoApis.vino)
@app.route("/")
def hello_world():
    return "Iniciado el microservicio"