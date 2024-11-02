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

document.addEventListener("DOMContentLoaded",()=>{
    const update_form=document.getElementById("update-user-form")
    update_form.addEventListener('submit',async(event)=>{
        event.preventDefault()
        const form=event.target
        const payload=new FormData(form)
        console.log(payload.get("image"))
        payload.delete("old_pass")
        payload.delete("new_pass")
        payload.delete("email")
        const params=new URLSearchParams(window.location.search)
        const id=params.get("id")
        const data=await fetch_api(payload,id)
        console.log(data)
    })
})