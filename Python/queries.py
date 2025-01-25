def login_query(data):
    query=f"select id, name, username, email,role_id from users where email='{data['email']}' and password='{data['password']}'"
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
    query=f"select c.name as name, c.image as image, c.description as description, c.upload_date as upload_date, t.name as teacher, t.image as teacher_image, (select count(*) from videos where course_id='{id}') as course_number from courses c join users t on c.teacher_id=t.id where c.id='{id}'"
    query2=f"select id, title, thumbnail from videos where course_id='{id}'"
    print(query)
    return {"q1":query,"q2":query2}


def video_details_query(id):
    query=f"select v.title as title, v.url as url, v.description as description, v.upload_date as upload_date, c.id as course_id, t.name as teacher, t.image as teacher_image from videos v join courses c on v.course_id=c.id join users t on c.teacher_id=t.id where v.id={id}"
    return query


def get_comments_query(video_id):
    query=f"select c.description as description ,c.upload_date as upload_date, c.user_id as user_id, u.image as user_image, u.name as name from comment c join users u on c.user_id=u.id where c.video_id={video_id}"
    return query