from flask import make_response
import queries
def add_comment(connector,data,video_id,user_id):
    final_data={}
    for key in data.keys():
        final_data[key]=data[key]
    final_data["video_id"]=video_id
    final_data["user_id"]=user_id
    query=queries.add_query(data=final_data,table="comment")
    cursor=connector.cursor
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Successfully created"},201)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)

def update_comment(connector,data,id):
    try:
        query=queries.update_query(data={"description":data["description"]},table="comment",id=id)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)
    try:
        connector.cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"Updated Successfully!"},200)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)

def get_comments(cursor,video_id):
    query=queries.get_comments_query(video_id=video_id)
    try:
        cursor.execute(query)
        data=cursor.fetchall()
        final_data={
            "message":"Successfull!",
            "data":data
        }
        return make_response(final_data,200)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)

def delete_comment(connector,id):
    query=queries.delete_query(table="comment",id=id)
    try:
        connector.cursor.excecute(query)
        connector.connection.commit()
        return make_response({"message":"Deleted Successfully!"},200)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},400)