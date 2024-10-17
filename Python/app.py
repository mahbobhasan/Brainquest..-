from flask import Flask,json,request,jsonify,make_response,send_file
from flask_cors import CORS
from datetime import datetime
app= Flask(__name__)
app.config['DEBUG']=True
CORS(app)
from connection import DB_Connector
from user_controller import get_students,add_user as a_user, update_user as u_user, delete_user as d_user, get_user_details as user_details


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
    image=request.files['image']
    dict={}
    file_location=upload_file(data=image)
    for key in data:
        dict[key]=data[key]
    if image.filename!="":
        dict['image']=f"{request.scheme}://{request.host}/{file_location}"
    return {"main":dict,"file":file_location}

# Convention Ends

@app.route("/home")
def home():
    return "Hello world"

@app.route("/students")
def student():
    return (get_students(connector.cursor))

@app.route("/user/<int:id>",methods=["GET"])
def get_user_details(id):
    return user_details(connector.cursor,id)

@app.route("/uploads/<filename>")
def get_file(filename):
    return send_file(f"uploads/{filename}")
    

@app.route("/add-user", methods=["POST"])
def add_student():
    img=request.files['image']
    final=final_dict(request=request)
    res=a_user(connector,final["main"])
    if res.status=="201 CREATED" and img.filename!="":
        img.save(final["file"])
    return res

@app.route("/update-user/<int:id>", methods=["PUT"])
def update_user(id):
    final=final_dict(request=request)
    image=request.files['image']
    res=u_user(connector,final['main'],id)
    if res.status=="200 OK" and image.filename!="":
        image.save(final['file'])
    return res

@app.route("/delete-student/<int:id>",methods=["DELETE"])
def delete_student(id):
    return (d_user(connector,id))

from course_controller import add_course as a_course , update_course as u_course, get_courses as g_courses, get_course_details as course_details,delete_course as d_course 

@app.route("/add-course",methods=["POST"])
def add_course():
    image=request.files['image']
    final=final_dict(request=request)
    res=a_course(connector=connector,data=final['main'])
    if res.status=="201 CREATED" and image.filename!="":
        image.save(final['file'])
    return res

@app.route("/update-course/<int:id>",methods=["PUT"])
def update_course(id):
    image=request.files['image']
    final=final_dict(request=request)
    res=u_course(connector=connector,data=final['main'],id=id)
    if res.status=="200 OK" and image.filename!="":
        image.save(final['file'])

@app.route("/delete-course/<int:id>",methods=["DELETE"])
def delete_coruse(id):
    return d_course(connector=connector,id=id)

@app.route("/get-courses")
def get_coruses():
    return g_courses(cursor=connector.cursor)

@app.route("/course/<int:id>")
def get_course_details(id):
    return course_details(cursor=connector.cursor,id=id)

from videos_controller import add_video as a_video, delete_video as d_video, update_video as u_video, video_details as v_details
@app.route("/add-video",methods=["POST"])
def add_video():
    image=request.files["image"]
    final=final_dict(request=request)
    final["main"]["thumbnail"]=final["main"].pop("image")
    res=a_video(connector=connector,data=final["main"])
    if res.status=="201 CREATED" and image.filename!="":
        image.save(final["file"])
    return res

@app.route("/update-video/<int:id>",methods=["PUT"])
def update_video(id):
    image=request.files["image"]
    final=final_dict(request=request)
    final["main"]["thumbnail"]=final["main"].pop("image")
    res=u_video(connector=connector,data=final["main"],id=id)
    if res.status=="200 CREATED" and image.filename!="":
        image.save(final["file"])
    return res

@app.route("/delete-video/<int:id>",methods=["DELETE"])
def delete_video(id):
    return d_video(connector=connector,id=id)

@app.route("/video-details/<int:id>")
def video_details(id):
    return v_details(cursor=connector.cursor,id=id)

if __name__=="__main__":
    app.run();