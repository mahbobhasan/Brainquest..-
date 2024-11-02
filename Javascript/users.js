console.log("hello")
let api_data="";


async function fetch_api_data(){
    try {
        const response=await fetch("http://127.0.0.1:5000/students",{
            method:"GET",
            headers:{
                "token":sessionStorage.getItem("token"),
                "Content-Type":"applicaton/json"
            }
        })
        api_data= await response.json()
        api_data=api_data['data']
        show_users(api_data)
        console.log(api_data)
    } catch (error) {
        console.log(error)
    }
}
fetch_api_data()


function show_users(data){
    const box_container=document.getElementById('box-container')
    box_container.classList='box-container'
    box_container.innerHTML=``
    for(user of data){
        const div=document.createElement('div')
        div.classList.add("box")
        console.log(user.name)
        div.innerHTML=`
            <div class="tutor">
                <img src="${user.image}" alt="">
                <div>
                    <h3>${user.name}</h3>
                </div>
            </div>
            <a href="tutors_profile.html?id=${user.id}" class="inline-btn" >View Profile</a>
        
        `
        box_container.appendChild(div)
    }
    // const view_profile_btns=document.querySelectorAll(".inline-btn")
    // view_profile_btns.forEach(button=>{
    //     button.addEventListener('click',function(event){
    //         localStorage.setItem('pk',button.id)
    //     })
    // })
    

}
