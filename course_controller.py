# Course Controller.py


from flask import make_response
from queries import add_query,update_query,delete_query
def add_course(data,connector):
    cursor=connector.cursor
    query=add_query(data=data,table="courses")
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Insertion Successful!"},201)
    except Exception as e:
        return make_response({"message":f"{e}"},400)

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
    query=f"slect name, teacher_id, description where id={id}"
    try:
        cursor.execute(query)
        course=cursor.fetchone()
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