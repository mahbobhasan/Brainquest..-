const frm=document.getElementById("add-course-form")
fetch("http://127.0.0.1:5000/get-teacher-nameID")
.then(res=>res.json())
.then(data=>{
    const select_teacher_dropdown=document.getElementById("teachers")
    data['data'].map(teacher=>{
        const option=document.createElement('option')
        option.value=`${teacher['id']}`
        option.innerText=`${teacher['name']}`
        select_teacher_dropdown.appendChild(option)

    })
})
.then(console.error());

const fetch_add_course=async (payload) =>{
    const res=await fetch("http://127.0.0.1:5000/add-course",{
        method:"POST",
        body:payload,
        headers:{
            "token":sessionStorage.getItem("token")
        }
    })
    return res.json()
}


frm.addEventListener("submit",async(event)=>{
    event.preventDefault();
    const message=document.getElementById("message")
    const add_form=event.target
    const payload=new FormData(add_form)
    console.log(payload.get("image"))
    const data = await fetch_add_course(payload)
    console.log(await data)
    if(!data["ERROR"]){
        message.classList='success'
        // message.classList.add('error')
        message.textContent=data["message"]

    }
    else
    {
        message.classList='error'
        // message.classList.add("success")
        message.textContent=data["ERROR"]
    }
})