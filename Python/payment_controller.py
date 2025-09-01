from flask import make_response
from queries import add_query
def add_new_transaction(connector,data):
    print(data)
    cursor=connector.cursor
    query=add_query(data=data,table="transaction")
    try:
        cursor.execute(query)
        connector.connection.commit()
        return True
    except Exception as e:
        print(e)
        return make_response({'ERROR':f'{e}'},400)
 
def update_transaction(connector,status,id):
    cursor=connector.cursor
    query=f"UPDATE transaction SET status='{status}' where id='{id}'"
    try:
        cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":status},200)
    except Exception as e:
        print(e)
        return make_response({'ERROR':f'{e}'},400)

def get_status(cursor,user_id,course_id):
    query=f"SELECT status from transaction where student_id={user_id} and course_id={course_id}"
    try:
        cursor.execute(query)
        status=cursor.fetchone()
        return make_response({"status":status},200)
    except Exception as e:
        print(e)
        return make_response({'ERROR':f'{e}'},400)
    
    
def get_price_of_course(cursor,id):
    query=f"select price from courses where id='{id}'"
    try:
        cursor.execute(query)
        amount=cursor.fetchone()
        if amount is not None:
            return make_response(amount,200)
        else:
            return make_response({"ERROR":"Something went wrong?"},200)
    except Exception as e:
        print(e)
        return make_response({"ERROR":f"{e}"},400)