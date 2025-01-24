console.log("hello")
const fetch_dashboard=async (id)=>{
    const res=await fetch(`http://127.0.0.1:5000/user/${id}`,{
        method:"GET",
        headers:{
            "token":sessionStorage.getItem("token"),
            "Content-Type":"application/json"
        }
    })
    const data=await res.json()
    console.log(data)
    if (!data["ERROR"]){
        console.log(data)
        return data["data"]
    }
    else{
        return false
    }
}

document.addEventListener("DOMContentLoaded",async () => {
    console.log(sessionStorage.getItem("token"))
    const params = new URLSearchParams(window.location.search);
    const id=params.get('id')
    const data=await fetch_dashboard(id)
    console.log(id)
    if(data!=false){
        const div=document.getElementById("user")
        div.innerHTML=`
             <img src="${data["image"]}" alt="Images/Pic-1.png" >
                <h3>${data["name"]}</h3>
            <!-- .............................. -->
            <p>${data['role_id']}</p>
            <button class="inline-btn" id="update-btn">Update Profile</button>
        `
    }

    const update_btn=document.getElementById("update-btn")
    update_btn.addEventListener('click',()=>{
    window.location.href=`update.html?id=${id}`
})
});


