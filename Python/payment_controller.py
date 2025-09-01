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
