console.log("hello")
const fetch_api=async(payload,id)=>{
    const res=await fetch(`http://127.0.0.1:5000/update-user/${id}`,{
        method:"PUT",
        body:payload,
        headers:{
            "token":sessionStorage.getItem("token")
        }
    })
    return res.json()
}

const check_equality_password= (new_pass,con_pass) =>{
    if (new_pass===con_pass){
        return true;
    }
    return false;
}

document.addEventListener("DOMContentLoaded",()=>{
    const update_form=document.getElementById("update-user-form")
    update_form.addEventListener('submit',async(event)=>{
        event.preventDefault()
        const form=event.target
        const payload=new FormData(form)

        const new_pass=payload.get("new_pass")
        const con_pass=payload.get("con_pass")
        if(check_equality_password(new_pass,con_pass)){
            payload.delete("new_pass")
            const params=new URLSearchParams(window.location.search)
            const id=params.get("id")
            const data=await fetch_api(payload,id)
            console.log(data)
        }
        else{
            const msg=document.getElementById("message")
            msg.classList=`error`;
            msg.innerText="Your new password and confirm password must be same."
        }
    })
})