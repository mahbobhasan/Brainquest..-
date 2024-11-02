from flask import request,make_response
import jwt
from datetime import datetime
from functools import wraps
def Authenticate(endpoint=""):
    def Authenticate1(func):
        @wraps(func)
        def inner2(*args,**kwargs):
            authorization=request.headers.get("token")
            try:
                jwt.decode(jwt=authorization,key="bhung",algorithms="HS384")
                print(jwt.decode(jwt=authorization,key="bhung",algorithms="HS384"))
            except jwt.ExpiredSignatureError:
                return make_response({"ERROR":"Token Expired!"},401)
            except jwt.InvalidTokenError as e:
                return make_response({"ERROR":"Invalid Token!"},401)
            except Exception as e:
                return make_response({"ERROR":f"{e}"},401)
            return func(*args,**kwargs)
        return inner2
    return Authenticate1

