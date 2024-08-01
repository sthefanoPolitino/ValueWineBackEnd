from functools import wraps
from flask import request
import jwt
import os
from ..Models.response import response


def checktoken(next):
    @wraps(next)
    def decorator(*args, **kwargs):
        secret = os.getenv("KEY")
        try:
            # obtenemos el authorization dentro de los headers
            reqHeaders = request.headers["Authorization"]
            token = str(reqHeaders).replace("Bearer ", "")
        except:
            return response('Token no valido', 401).__json__()
        try:
            decodeToken = jwt.decode(token, secret, algorithms="HS256")
            print("Token valido")
        except jwt.ExpiredSignatureError:
            return response('Token expirado', 401).__json__()
        except jwt.InvalidTokenError as e:
            return response('Token no valido', 401).__json__()
        return next(*args, **kwargs)
    return decorator
