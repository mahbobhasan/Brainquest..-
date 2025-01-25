import jwt
def decrypt(token):
    data=jwt.decode(jwt=token,key="bhung",algorithms="HS384")
    return data["payload"]


def get_students_authority(request):
    data=decrypt(request.headers.get("token"))
    if data['role_id']==3 or data['role_id']==2:
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
