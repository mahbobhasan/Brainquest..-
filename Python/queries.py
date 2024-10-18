def login_query(data):
    query=f"select id, name, username, email,role_id from users where username='{data['username']}' and password='{data['password']}'"
    return query


def add_query(data,table):
    query=f"insert into {table} ("
    for key in data.keys():
        query+=key+","
    query=query[:-1]+") values("
    for key in data.keys():
        if type(data[key])==str:
            query+=f"'{data[key]}',"
        else:
            query+=f"{data[key]},"
    query=query[:-1]+")"

    return query


def update_query(data,table,id):
    query=f"UPDATE {table} SET "
    for key in data.keys():
        query+=f"{key}='{data[key]}',"
    query=query[:-1]+f" WHERE id={id}"
    return query


def delete_query(table,id):
    query=f"delete from {table} where id={id}"
    return query


def course_details_query(id):
    query=f"select name, description, teacher_id from courses where id={id}"
    query2=f"select id, title, thumbnail from videos where course_id={id}"
    return {"q1":query,"q2":query2}


def video_details_query(id):
    query=f"select title, url, description, upload_date from videos where id={id}"
    return query