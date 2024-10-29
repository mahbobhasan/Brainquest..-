import jwt
def decrypt(token):
    data=jwt.decode(jwt=token,key="bhung",algorithms="HS384")
    return data["payload"]


def get_students_authority(request):
    data=decrypt(request.headers.get("Authorization"))
    # print(data)
    if data['role_id']==3 or data['role_id']==2:
        return True
    return False

def update_user_authority(request,id):
    data=decrypt(request.headers.get("Authorization"))
    if data["id"]==id:
        return True
    return False

def delete_user_authority(request,id):
    data=decrypt(token=request.headers.get("Authorization"))
    if data['id']==id or data['role_id']==3:
        return True
    return False

def admin_authority(request):
    data=decrypt(request.headers.get("Authorization"))
    if data["role_id"]==3:
        return True 
    return False

def video_is_valid(id,course_id,cursor):
    query1=f"select session from users where id={id}"
    query2=f"select session from courses where id={course_id}"
    try:
        cursor.execute(query1)
        session1=cursor.fetchone()
        cursor.execute(query2)
        session2=cursor.fetchone()
        if session1["session"]==session2["session"]:
            return True
        return False
    except:
        return -1


def course_authority(request,course_id):
    data=decrypt(request.headers.get("Authorization"))
    id=data["id"]
    result=video_is_valid(id=id,course_id=course_id)
    return result
