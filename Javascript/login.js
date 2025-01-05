const login_form=document.getElementById("login-form")

login_form.addEventListener('submit', function(event){
    event.preventDefault()
    form=event.target
    const payload=new FormData(form)
    fetch_api(payload)
})

const fetch_api=async (payload) =>{
    const res=await fetch(`http://127.0.0.1:5000/login`,{
        method:"POST",
        body:payload
    })  
    const data=await res.json()
    console.log(data)
    sessionStorage.setItem("token",data["token"])
    if (data["message"]==="Successful"){
        window.location.href=`../profile.html?id=${data['id']}`
    }
    else{
        console.log(data["message"])
    }
}