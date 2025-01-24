const login_form=document.getElementById("login-form")
const message=document.getElementById('message');
message.style.display='none'
console.log("inside the login")
login_form.addEventListener('submit', function(event){
    event.preventDefault()
    form=event.target
    const payload=new FormData(form)
    fetch_login(payload)
})

const fetch_login=async (payload) =>{
    try{
        const res=await fetch(`http://127.0.0.1:5000/login`,{
            method:"POST",
            body:payload
        })  
        const data=await res.json()
        console.log(data)
        sessionStorage.setItem("token",data["token"])
        if (!data["ERROR"]){
            localStorage.setItem("id",data['id'])
            window.location.href=`../profile.html?id=${data['id']}`
        }
        else{
            message.style.display='block';
            message.textContent=data["ERROR"]
            message.classList='error'
            setTimeout(function() {
            message.style.display = 'none'; // Hide the message after 10 seconds
            message.classList.remove('error')
        }, 10000);
        }
    }
    catch(error){
        message.style.display='block';
        message.textContent="Something went wrong. Please try again later."
        message.classList='error'
        setTimeout(function() {
            message.style.display = 'none'; // Hide the message after 10 seconds
        }, 10000);
        
    }
    
}