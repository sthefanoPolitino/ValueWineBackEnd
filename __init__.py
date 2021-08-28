from flask import Flask
from ValueWIneBack import usuarioApis
app = Flask(__name__)
app.register_blueprint(usuarioApis.usuario)
@app.route("/")
def hello_world():
    return "Iniciado el microservicio"