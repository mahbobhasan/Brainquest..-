
from connection import DB_Connector

obj=DB_Connector()

def is_admin(id,cursor):
    query=f"select role_id from users where id={id}"
    try:
        cursor.execute(query)
        info=cursor.fetchone()
        if cursor.rowcount==0:
            return -1
        if info["role_id"]==3:
            return True
        return False
    except:
        return False

def is_teacher(teacher,cursor):
    query=f"select role_id from users where id={teacher}"
    try:
        cursor.execute(query)
        info=cursor.fetchone()
        if cursor.rowcount==0:
            return -1
        if info["role_id"]==2 or info["role_id"]==3:
            return True
        return False
    except:
        return False

from flask import make_response
from queries import add_query,update_query,delete_query,course_details_query
def add_course(data,connector):
    teacher=data["teacher_id"]
    check=is_teacher(teacher,connector.cursor)
    if check==False or check==-1:
        # print(check)
        return make_response({"ERROR":"The selected user is not a teacher"},400)
    if check is None:
        # print(0)
        return make_response({"ERROR":"There is a problem in internal server"},500)
    cursor=connector.cursor
    query=add_query(data=data,table="courses")
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"successful"},201)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)
# add_course(data={"teacher_id":2},connector=obj)

def update_course(data,connector,id):
    cursor=connector.cursor
    query=update_query(data=data,table="courses",id=id)
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"successful"},200)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)

def get_courses(cursor,id=0):
    query=""
    if id==0 or is_admin(id=id,cursor=cursor):
        query="select c.id as id, c.name as name, c.image as image, c.upload_date as upload_date, t.name as teacher_name, t.image as teacher_image from courses c join users t on c.teacher_id=t.id"
    elif is_teacher(id,cursor):
        query=f"select c.id as id, c.name as name, c.image as image, c.upload_date as upload_date, t.name as teacher_name, t.image as teacher_image from courses c join users t on c.teacher_id=t.id where t.id={id}"
    else:
        query=f"select c.id as id, c.name as name, c.image as image, c.upload_date as upload_date, t.name as teacher_name, t.image as teacher_image from courses c join users t on c.teacher_id=t.id where c.session=(select session from users where id={id})"
    try:
        cursor.execute(query)
        courses=cursor.fetchall()
        data={
            "message":"successful",
            "data":courses
        }
        return make_response(data,200)
    except Exception as e:
        print(e)
        return make_response({"ERROR":f"{e}"}, 400)
    

def get_course_details(cursor,id):
    query=course_details_query(id=id)
    query1=query["q1"]
    query2=query["q2"]
    try:
        cursor.execute(query1)
        course=cursor.fetchone()
        cursor.execute(query2)
        videos=cursor.fetchall()
        details={"course":course,"videos":videos}
        data={
            "message":"successful",
            "data":details
        }
        return make_response(data,200)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)
    
def delete_course(connector,id):
    cursor=connector.cursor
    query=delete_query(table="courses",id=id)
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Successful"},200)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)