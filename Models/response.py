from flask import jsonify
class response:
    def __init__(self,msg:str,code:int,nameEtiqueta=None,value=None):
        self.msg=msg
        self.code=code
        self.nameEtiqueta=nameEtiqueta
    def __json__(self,value=None):
        if(value):
            print(str(self.nameEtiqueta))
            response=jsonify({"msg":self.msg,"code":self.code,str(self.nameEtiqueta):value})
        else:
            response= jsonify({"msg":self.msg,"code":self.code})
        response.status_code = self.code
        return response