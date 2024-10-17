# Course Controller.py

from connection import DB_Connector

obj=DB_Connector()

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
        pass

from flask import make_response
from queries import add_query,update_query,delete_query,course_details_query
def add_course(data,connector):
    teacher=data["teacher_id"]
    check=is_teacher(teacher,connector.cursor)
    if check==False or check==-1:
        # print(check)
        return make_response({"message":"The selected user is not a teacher"},400)
    if check is None:
        # print(0)
        return make_response({"message":"There is a problem in internal server"},500)
    cursor=connector.cursor
    query=add_query(data=data,table="courses")
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Insertion Successful!"},201)
    except Exception as e:
        return make_response({"message":f"{e}"},400)
# add_course(data={"teacher_id":2},connector=obj)

def update_course(data,connector,id):
    cursor=connector.cursor
    query=update_query(data=data,table="courses",id=id)
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Successfully Updated!"},200)
    except Exception as e:
        return make_response({"message":f"{e}"},400)

def get_courses(cursor):
    query="select id, name, image from courses"
    try:
        cursor.execute(query)
        courses=cursor.fetchall()
        data={
            "message":"Successfull",
            "data":courses
        }
        return make_response(data,200)
    except Exception as e:
        return make_response({"message":f"{e}"}, 400)
    

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
            "message":"Successfull",
            "data":details
        }
        return make_response(data,200)
    except Exception as e:
        return make_response({"message":f"{e}"},400)
    
def delete_course(connector,id):
    cursor=connector.cursor
    query=delete_query(table="courses",id=id)
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Successfully Deleted!"},200)
    except Exception as e:
        return make_response({"message":f"{e}"},400)