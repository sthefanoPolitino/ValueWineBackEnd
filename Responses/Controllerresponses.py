from flask import jsonify
def make_response(statuscode,message):
    response = jsonify({'message': message,"status_code":statuscode})
    response.status_code = statuscode
    return response