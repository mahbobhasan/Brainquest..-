console.log("hello")
const fetch_api=async (id)=>{
    const res=await fetch(`http://127.0.0.1:5000/user/${id}`,{
        method:"GET",
        headers:{
            "token":sessionStorage.getItem("token"),
            "Content-Type":"application/json"
        }
    })
    const data=await res.json()
    console.log(data)
    if (data["message"]==="Successful"){
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
    const data=await fetch_api(id)
    console.log(id)
    if(data!=false){
        const div=document.getElementById("user")
        div.innerHTML=`
             <img src="${data["image"]}" alt="Images/Pic-1.png" >
                <h3>${data["username"]}</h3>
            <!-- .............................. -->
            <p>Student</p>
            <button class="inline-btn" id="update-btn">Update Profile</button>
        `
    }

    const update_btn=document.getElementById("update-btn")
    update_btn.addEventListener('click',()=>{
    window.location.href=`update.html?id=${id}`
})
});


