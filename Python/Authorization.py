import jwt
from pprint import pprint
from flask import make_response
def decrypt(token):
    try:
        data=jwt.decode(jwt=token,key="bhung",algorithms="HS384")
        # print(jwt.decode(jwt=authorization,key="bhung",algorithms="HS384"))
        return data['payload']
    except jwt.ExpiredSignatureError:
        return make_response({"ERROR":"Token Expired!"},401)
    except jwt.InvalidTokenError as e:
        return make_response({"ERROR":"Invalid Token!"},401)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},401)
def get_students_authority(request):
    data=decrypt(request.headers.get("token"))
    if data['role_id']==3 or data['role_id']==2 or data['role_id']==1:
        return True
    return False

def update_user_authority(request,id):
    data=decrypt(request.headers.get("token"))
    if data["id"]==id:
        return True
    return False

def delete_user_authority(request,id):
    data=decrypt(token=request.headers.get("token"))
    if data['id']==id or data['role_id']==3:
        return True
    return False

def admin_authority(request):
    data=decrypt(request.headers.get("token"))
    if data["role_id"]==3:
        return True 
    return False

def student_authority(request):
    data=decrypt(request.headers.get("token"))
    if data["role_id"]==1:
        return True
    return False
def teacher_authority(request):
    data=decrypt(request.headers.get("token"))
    if data["role_id"]==2:
        return True
    return False

def enrolled_course_authority(request,course_id,cursor):
    data=decrypt(request.headers.get("token"))
    query=f"select status from transaction where student_id={data['id']} and course_id='{course_id}'"
    try:
        cursor.execute(query)
        stat=cursor.fetchone()
        print(stat)
        if stat is not None and stat['status']=="success":
            return True
        else:
            False
    except Exception as e:
        pprint({"ERROR":e})
        return False
    
def get_self_id(request):
    data=decrypt(request.headers.get("token"))
    """
    eikhane aro validation lagbe
    """
    return data['id']