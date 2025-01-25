from flask import make_response
from queries import add_query,delete_query,update_query,video_details_query


def add_video(connector,data):
    cursor=connector.cursor
    new_data={}
    for key in data:
        if key!="url":
            new_data[key]=data[key]
    str=data['url']
    str=str.split("youtu.be")
    new_url=str[0]+"www.youtube.com/embed"+str[1]
    new_data['url']=new_url
    print(new_url)
    query=add_query(data=new_data,table="videos")
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Insertion Successful!"},201)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)
    
def update_video(connector,data,id):
    cursor=connector.cursor
    query=update_query(data=data,table="videos",id=id)
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Successfully Updated!"},200)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)
    
def delete_video(connector,id):
    cursor=connector.cursor
    query=delete_query(table="videos",id=id)
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Successfully Deleted!"},200)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)
    


def video_details(cursor,id):
    query=video_details_query(id=id)
    try:
        cursor.execute(query)
        details=cursor.fetchone()
        data={
            "message":"Successful",
            "data":details
        }
        return make_response(data,200)

    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)
    