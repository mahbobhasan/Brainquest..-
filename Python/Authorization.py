import jwt
from pprint import pprint
def decrypt(token):
    data=jwt.decode(jwt=token,key="bhung",algorithms="HS384")
    return data["payload"]
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
        if stat=="success":
            return True
        else:
            False
    except Exception as e:
        pprint({"ERROR":e})
        return False