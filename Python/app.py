from flask import Flask,request,make_response,send_file
from flask_cors import CORS
from datetime import datetime
app= Flask(__name__)
app.config['DEBUG']=True
CORS(app)
from connection import DB_Connector
from user_controller import get_students,add_user as a_user, update_user as u_user, delete_user as d_user, get_user_details as user_details , login as user_login
from Authentication import Authenticate
import Authorization

connector=DB_Connector()

# Convention Starts

def upload_file(data):
    uniquefilename= str(datetime.now().timestamp()).replace(".","")
    filename=str(data.filename).split(".")
    extension=filename[len(filename)-1]
    file_location=f"uploads/{uniquefilename}.{extension}"
    return file_location

def final_dict(request):
    data=request.form
    print(request.files)
    image=request.files["image"]
    dict={}
    file_location=upload_file(data=image)
    for key in data:
        dict[key]=data[key]
    if image.filename!="":
        dict['image']=f"{request.scheme}://{request.host}/{file_location}"
    return {"main":dict,"file":file_location}

# Convention Ends

@app.route("/login",methods=["POST"])
def login():
    data=request.form
    return user_login(data=data,cursor=connector.cursor)

@app.route("/students")
@Authenticate("/students")
def student():
    if Authorization.get_students_authority(request=request)==True:
        return (get_students(connector.cursor,role=1))
    return make_response({"Error":"You are not Authorized"},401)
@app.route("/teachers",methods=['GET'])
@Authenticate()
def teacher():
    if Authorization.get_students_authority(request=request)==True:
        return (get_students(connector.cursor,role=2))
    return make_response({"Error":"You are not Authorized"},401)

@app.route("/user/<int:id>",methods=["GET"])
@Authenticate()
def get_user_details(id):
    return user_details(connector.cursor,id)

@app.route("/uploads/<filename>")
def get_file(filename):
    return send_file(f"..//uploads//{filename}")
    

@app.route("/add-user", methods=["POST"])
def add_student():
    img=request.files['image']
    final=final_dict(request=request)
    res=a_user(connector,final["main"])
    if res.status=="201 CREATED" and img.filename!="":
        img.save(final["file"])
    return res

@app.route("/update-user/<int:id>", methods=["PUT"])
@Authenticate()
def update_user(id):
    if Authorization.update_user_authority(request=request,id=id)==True:
        image=request.files['image']
        data=request.form
        print(data)
        print("inside")
        query= f"select * from users where id={id} and password='{data['password']}'"
        try:  
            connector.cursor.execute(query)
            user=connector.cursor.fetchone()
            if user is not None:
                if data['con_pass']!="":
                    new_dict={}
                    for key in data:
                        if key=='password' :
                            continue
                        elif key=='con_pass':
                            new_dict['password']=data[key]
                        else:
                            new_dict[key]=data[key]
                    if image.filename!="":
                        file_location=upload_file(data=image)
                        new_dict['image']=f"{request.scheme}://{request.host}/{file_location}"
                    res=u_user(connector=connector,data=new_dict,id=id)
                    if res.status=="200 OK" and image.filename!="":
                        image.save(file_location)
                    return res
                else:
                    new_dict={}
                    for key in data:
                        if key=='con_pass' :
                            continue
                        else:
                            new_dict[key]=data[key]
                    if image.filename!="":
                        file_location=upload_file(data=image)
                        new_dict['image']=f"{request.scheme}://{request.host}/{file_location}"
                    res=u_user(connector=connector,data=new_dict,id=id)
                    if res.status=="200 OK" and image.filename!="":
                        image.save(file_location)
                    return res
            else:
                return make_response({'ERROR':'your old password is incorrect'},400)
        
        except Exception as e:
                return make_response({"ERROR":f"{e}"},500)  
    return make_response({"ERROR":"You are not Authorized"},401)

@app.route("/delete-user/<int:id>",methods=["DELETE"])
@Authenticate()
def delete_user(id):
    if Authorization.delete_user_authority(request=request,id=id)==True:
        return (d_user(connector,id))
    return make_response({"ERROR":"You are not Authorized"},401)

@app.route("/get-teacher-nameID")
def get_teacher_nameID():
    query="select name, id from users where role_id=2"
    try:
        connector.cursor.execute(query)
        teachers=connector.cursor.fetchall()
        print(teachers)
        data={
            "data":teachers,
            "message":"successful"
        }
        return make_response(data,200)
    except Exception as e:
        return make_response({"ERROR":f"{e}"},500)

from course_controller import add_course as a_course , update_course as u_course, get_courses as g_courses, get_course_details as course_details,delete_course as d_course 

@app.route("/add-course",methods=["POST"])
@Authenticate()
def add_course():
    if Authorization.admin_authority(request=request):
        print("hello")
        image=request.files['image']
        print(request.form)
        print(image)
        final=final_dict(request=request)
        res=a_course(connector=connector,data=final['main'])
        if res.status=="201 CREATED" and image.filename!="":
            image.save(final['file'])
        return res
    return make_response({"ERROR":"You ar not Authorized"},401)

@app.route("/update-course/<int:id>",methods=["PUT"])
@Authenticate()
def update_course(id):
    if Authorization.admin_authority(request=request):
        image=request.files['image']
        final=final_dict(request=request)
        res=u_course(connector=connector,data=final['main'],id=id)
        if res.status=="200 OK" and image.filename!="":
            image.save(final['file'])
    return make_response({"ERROR":"You ar not Authorized"},401)

@app.route("/delete-course/<int:id>",methods=["DELETE"])
@Authenticate()
def delete_coruse(id):
    if Authorization.admin_authority(request=request):
        return d_course(connector=connector,id=id)
    return make_response({"ERROR":"You ar not Authorized"},401)

@app.route("/get-courses")
def get_coruses():
    return g_courses(cursor=connector.cursor)

@app.route("/courses-with-id")
def courses_with_id():
    query="select id, name from courses"
    try:
        connector.cursor.execute(query)
        courses=connector.cursor.fetchall()
        if len(courses)>0:
            return make_response({"data":courses,"message":"successful"},200)
        else:
            return make_response({"ERROR":"empty"},200)
    except Exception as e:
        return make_response({"ERROR":e},500)
    
@app.route("/get-courses-with-id-matching-session/<int:user_id>")
def get_courses_with_id_matching_session(user_id):
    query=f'select c.id, c.name from courses c join users s on c.session=s.session where s.id={user_id}'
    print(query)
    try:
        connector.cursor.execute(query)
        course=connector.cursor.fetchall()
        if course is not None:
            data={
                "data":course,
                "message":"successful"
            }
            return make_response(data,200)
        else:
            return make_response({"ERROR":"No data"},200)
    except Exception as e:
        return make_response({"ERROR":e},500)
@app.route("/get-courses/<int:user_id>")
@Authenticate()
def get_courses(user_id):
    return g_courses(cursor=connector.cursor,id=user_id)
@app.route("/course/<string:id>")
@Authenticate()
def get_course_details(id):
    if Authorization.admin_authority(request=request) or Authorization.teacher_authority(request=request) or Authorization.student_authority(request=request):
        return course_details(cursor=connector.cursor,id=id)

from videos_controller import add_video as a_video, delete_video as d_video, update_video as u_video, video_details as v_details
@app.route("/add-video",methods=["POST"])
@Authenticate()
def add_video():
    if Authorization.admin_authority(request=request)==True:
        image=request.files["image"]
        final=final_dict(request=request)
        final["main"]["thumbnail"]=final["main"].pop("image")
        res=a_video(connector=connector,data=final["main"])
        if res.status=="201 CREATED" and image.filename!="":
            image.save(final["file"])
        return res
    return make_response({"ERROR":"You are not Authorized"},401)

@app.route("/update-video/<int:id>",methods=["PUT"])
@Authenticate()
def update_video(id):
    if Authorization.admin_authority(request=request)==True:
        image=request.files["image"]
        final=final_dict(request=request)
        final["main"]["thumbnail"]=final["main"].pop("image")
        res=u_video(connector=connector,data=final["main"],id=id)
        if res.status=="200 OK" and image.filename!="":
            image.save(final["file"])
        return res
    return make_response({"ERROR":"You are not Authorized"},401)

@app.route("/delete-video/<int:id>",methods=["DELETE"])
@Authenticate()
def delete_video(id):
    if Authorization.admin_authority(request=request)==True:
        return d_video(connector=connector,id=id)
    return make_response({"ERROR":"You are not Authorized"},401)

@app.route("/video-details/<int:id>")
@Authenticate()
def video_details(id):
    return v_details(cursor=connector.cursor,id=id)


# Comments Route
from comment_controller import add_comment as a_comment, update_comment as u_comment , delete_comment as d_comment, get_comments as all_comments
@app.route("/add-comment/<int:video_id>/<int:user_id>",methods=["POST"])
@Authenticate()
def add_comment(video_id,user_id):
    return a_comment(connector=connector,data=request.form,video_id=video_id,user_id=user_id)

@app.route("/update-comment/<int:id>/<int:user_id>",methods=["PUT"])
@Authenticate()
def update_comment(id,user_id):
    if Authorization.update_user_authority(request=request,id=user_id):
        return u_comment(connector=connector,data=request.form,id=id)
    return make_response({"ERROR":"You are not Authorized"},401)

@app.route("/delete-comment/<int:id>/<int:user_id>",methods=["DELETE"])
@Authenticate()
def delete_comment(id,user_id):
    if Authorization.update_user_authority(request=request,id=user_id):
        return d_comment(connector=connector,id=id)
    return make_response({"ERROR":"You are not Authorized"},401)

@app.route("/get-comments/<int:id>",methods=["GET"])
@Authenticate()
def get_comments(id):
    return all_comments(cursor=connector.cursor,video_id=id)



@app.route("/add-review/<int:user_id>",methods=["POST"])
@Authenticate()
def add_review(user_id):
    data=request.form
    print(data)
    query=f"insert into reviews (student,course,description,rating) values({user_id},'{data['course']}','{data['description']}',{data['rating']})"
    try:
        connector.cursor.execute(query)
        connector.connection.commit()
        return make_response({"message":"successful"},201)
    except Exception as e:
        return make_response({"ERROR":e},500)
    # return make_response({"data":query},200)

@app.route("/get-review/<string:course_id>",methods=["GET"])
def get_reviews(course_id):
    query=f"select s.name as name, s.image as image, r.rating as rating, r.description as description from reviews r join users s on r.student=s.id where r.course='{course_id}'"
    try:
        connector.cursor.execute(query)
        reviews=connector.cursor.fetchall()
        if len(reviews)>0:
            data={
                "data":reviews,
                "message":"successful"
            }
            return make_response(data,200)
        else:
            return make_response({"ERROR":"No reviews"},200)
    except Exception as e:
        return make_response({"ERROR":e},500)
if __name__=="__main__":
    app.run();