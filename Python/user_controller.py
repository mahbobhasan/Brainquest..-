# User Controller.py


from flask import make_response
import jwt
from datetime import datetime,timedelta
from queries import add_query,update_query,delete_query,login_query


def login(data,cursor):
    print(data)
    query=login_query(data=data)
    try:
        cursor.execute(query)
        info=cursor.fetchone()
        if info is not None:
            print(info)
            exp_time=datetime.now()+timedelta(minutes=15)
            epoch_time=int(exp_time.timestamp())
            payload={
                "payload":info,
                "exp":epoch_time
            }
            tok=jwt.encode(payload=payload,key="bhung",algorithm="HS384")
            token={
                "message":"Successful",
                "id":info["id"],
                "token":tok
            }
            return make_response(token,200)
        return make_response({"ERROR":"Invalid email or password."},400)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)

def get_students(cursor):
    query="select id, image, name, role_id from Users where role_id=1"

    try:
        cursor.execute(query)
        students=cursor.fetchall()
        if len(students)>0:
            data={
                "message":"Successfull",
                "data":students
            }
            for dic in students:
                if dic["role_id"]==3:
                    dic["role_id"]="admin"
                elif dic["role_id"]==1:
                    dic["role_id"]="student"
                else:
                    dic["role_id"]="teacher"
            return make_response(data,200)
        else:
            return make_response({},200)
    except Exception as e:
        data={
            "ERROR":f"{e}",
            "data":""
        }
        return data

def add_user(connector,data):
    print(data)
    curso=connector.cursor
    query=add_query(data=data,table="users")
    try:
        curso.execute(query)
        connector.connection.commit()
        return make_response({'message':"Successfull"},201)
    except Exception as e:
        print(e)
        return make_response({'ERROR':f'{e}'},400)
    

def update_user(connector,data,id):

    cursor=connector.cursor
    for key in data.keys():
        if key=="username" or key=="email" or key=="id" :
            message={"ERROR":f"you can't update your {key}"}
            return make_response(message,400)
        elif key!="name" and key!="image" and key!="password":
            message={"ERROR":f"unknown field name {key}"}
            return make_response(message,400)
    query=update_query(data=data,table="users",id=id)
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Successfully updated."},200)
    except Exception as e:
        print(e)
        return make_response({'ERROR':f'{e}'},400)
    
def delete_user(connector,id):
    cursor=connector.cursor
    query=delete_query(table="users", id=id)
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Successfully Deleted!"},200)
    except Exception as e:
        print(e)
        return {'ERROR':f'{e}'}


def get_user_details(cursor,id):
    query=f"select id, image, name, email, username, session, role_id from Users where id={id}"
    try:
        cursor.execute(query)
        student=cursor.fetchone()
        print(student)
        if student is not None:
            if student["role_id"]==3:
                student["role_id"]="admin"
            elif student["role_id"]==1:
                student["role_id"]="student"
            else:
                student["role_id"]="teacher"
            data={
                "message":"Successful",
                "data":student
            }
            return make_response(data,200)
        else:
            return make_response({"ERROR":"No user found"},200)
    except Exception as e:
        data={
            "ERROR":f"{e}",
        }
        return data