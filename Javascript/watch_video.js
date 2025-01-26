document.addEventListener("DOMContentLoaded", async(event)=>{
    const fetch_api= async (id)=>{
        try{
            const res=await fetch(`http://127.0.0.1:5000/user/${id}`,{
                method:"GET",
                headers:{
                    "token":sessionStorage.getItem("token"),
                    "Content-Type":"application/json"
                }
            });
            return res.json()
        }
        catch(error){
            return {"ERROR":`${error.message}`}
        }
    }
    const header=document.getElementById("header")
    header.innerHTML=`
            <section class="flex" >
                <a href="index.html" class="logo">BrainQuest..!</a>
                <form action=" " method="post" class="search-form" >         <!-- user input-->
                    <input type="text" name="search_box" placeholder="Search Courses...." required maxlength="100">     
                    <button type="submit" class="fas fa-search" name="search_box" ></button>
                </form>
                <div class="icons">
                    <div id="menu-btn" class="fas fa-bars"></div>
                    <div id="search-btn" class="fas fa-search"></div>
                    <div id="user-btn" class="fas fa-user"></div>
                    <div id="toggle-btn" class="fas fa-sun"></div>
                </div>
                <div class="profile" id="header-profile">
                    <a href="Login.html" class="option-btn">Login</a>
                    <a href="Register.html" class="delete-btn">Register</a>
                </div>
            </section>
`
    let sidebar=document.getElementById("sidebar")
    sidebar.innerHTML=`
        <div class="close-sidebar">
            <i class="fas fa-times"></i>
        </div>
        <div class="profile" id="sidebar-profile">
            <img src="Images/Pic-1.png" alt="">
            <!-- need to add database -->
            <h3>Username</h3>
            <span>Student</span>
        </div>
        <nav class="navbar" id="navbar">
            <a href="index.html"><i class="fas fa-home"></i><span>Home</span></a>
            <a href="about.html"><i class="fas fa-question"></i><span>About Us</span></a>
            <a href="contact.html"><i class="fas fa-headset"></i><span>Contact Us</span></a>
        </nav>
`
        if(localStorage.getItem("id")){

            const div=document.getElementById('header-profile')
            const div2=document.getElementById('sidebar-profile')
            const navbar=document.getElementById('navbar')
            const data= await fetch_api(localStorage.getItem("id"))
            console.log( data)
            if(!data["ERROR"]){
                div.innerHTML=`
                    <img src="${data['data']['image']}" alt="" id="header-profile-img">
                    <!-- need to add database -->
                    <h3>${data['data']['name']}</h3>
                    <span>${data['data']['role_id']}</span>
                    <a href="Profile.html?id=${data['data']['id']}" class="btn">Viewprofile</a>
                    <div class="flex-btn">
                        <a href="Login.html" class="option-btn" id="logout-btn">Logout</a>
                    </div>
                `
                div2.innerHTML=`
                    <img src="${data['data']['image']}" alt="">
                    <!-- need to add database -->
                    <h3>${data['data']['name']}</h3>
                    <span>${data['data']['role_id']}</span>
                    <a href="Profile.html?id=${data['data']['id']}" class="btn">Viewprofile</a>
                `

                navbar.innerHTML=`
                    <a href="index.html"><i class="fas fa-home"></i><span>Home</span></a>
                    <a href="about.html"><i class="fas fa-question"></i><span>About Us</span></a>
                    <a href="courses.html"><i class="fas fa-graduation-cap"></i><span>Our Courses</span></a>
                    <a href="teachers.html"><i class="fas fa-chalkboard-user"></i><span>Our Teachers</span></a>
                    <div class="dropdown-container">
                        <a href="Users.html"><i class="fas fa-users"></i> <span>Our Students</span></a>
                    </div>
                    <a href="contact.html"><i class="fas fa-headset"></i><span>Contact Us</span></a>
                `
    
                const logout_btn=document.getElementById("logout-btn");
                logout_btn.addEventListener("click",(event)=>{
                    localStorage.removeItem("id")
                    sessionStorage.removeItem("token")
                    window.location.href="../home.html"
                })
            }
        }
        let body= document.body;
    
    let prof = document.querySelector('.header .flex .profile');
    document.querySelector('#user-btn').onclick = () =>{
        prof.classList.toggle('active');
        search.classList.remove('active');
    
    }
    
    
    let search = document.querySelector('header .flex .search-form');
    document.querySelector('#search-btn').onclick = () =>{
        search.classList.toggle('active');
        prof.classList.remove('active');
    }
    
    let side = document.querySelector('.sidebar');
    document.querySelector('#menu-btn').onclick = () =>{
        side.classList.toggle('active');
        body.classList.toggle('active');
        console.log(side.classList)
    }
    document.querySelector('.sidebar .close-sidebar').onclick =() =>{
                          
        side.classList.toggle('active');
        body.classList.toggle('active');
    }
    
    
    // document.querySelector(' .close-sidebar').onclick =() =>{
    //     side.classList.remove('active');
    //     body.classList.remove('active');
     
    // }
    
    
    //console.log("ideclassList");
    
    window.onscroll = () =>{
        prof.classList.remove('active');
        search.classList.remove('active');
        if(innerWidth<1200){
            side.classList.remove('active');
            body.classList.remove('active');
        }
    }
    
    // toggle button eikhane
    let toggleBtn = document.querySelector('#toggle-btn');
    let darkMode = localStorage.getItem('dark-mode');
    // body = document.querySelector('body');
    
    
    const enableDarkMode = () => {
        toggleBtn.classList.replace('fa-sun', 'fa-moon');
        body.classList.add('dark');
        localStorage.setItem('dark-mode', 'enabled');
    };
    
    const disableDarkMode = () => {
        toggleBtn.classList.replace('fa-moon', 'fa-sun');
        body.classList.remove('dark');
        localStorage.setItem('dark-mode', 'disabled');
    };
    
    if (darkMode === 'enabled') {
        enableDarkMode();
    }
    
    toggleBtn.onclick = () => {
        let darkMode = localStorage.getItem('dark-mode');
        if (darkMode === 'disabled') {
            enableDarkMode();
        } else {
            disableDarkMode();
        }
    };
   
    const fetch_video= async(id) =>{
        try{

            const res= await fetch(`http://127.0.0.1:5000/video-details/${id}`,{
                method:"GET",
                headers:{
                    "token":sessionStorage.getItem("token"),
                    "Content-Type":"application/json"
                }
            })
            const js= await res.json()
            console.log(js)
            if(!js["ERROR"]){
                const data= await js['data']
                const video_details=document.getElementById("video-details")
                video_details.innerHTML=`
                    <iframe width="560" height="315" src="${data['url']};
                    start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
                    encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin"
                    allowfullscreen></iframe>
                    <h3 class="title">${data['title']}</h3>
                    <div class="info">
                        <p><i class="fas fa-calendar"></i><span>${data['upload_date']}</span></p>
                        <p><i class="fas fa-heart"></i><span>3k Likes</span></p>
                    </div>
                    <hr style="height:2px; border-width:0; color:rgb(145, 145, 145); background-color:rgb(145, 145, 145)">
                    <div class="tutor">
                        <img src="${data['teacher_image']}" alt="">
                        <div>
                            <h3>${data['teacher']}</h3>
                            <span>Physics Co-ordinator</span>
                        </div>
                    </div>
                    <div class="flex">
                        <a href="playlist.html?id=${data['course_id']}" class="inline-btn">View Playlist</a>
                        <button><i class="fas fa-heart"></i><span> </span><span> Like</span></button>
                    </div>

                    <div class="description">
                        <p>${data.description}.
                        </p>
                    </div>
                `
            }
        }
        catch(error){
            console.log(error.message)
        }
    }
    const fetch_comment_post= async(payload,id,user_id)=>{
        try{
            const res= await fetch(`http://127.0.0.1:5000/add-comment/${id}/${user_id}`,{
                method:"POST",
                body:payload,
                headers:{
                    "token":sessionStorage.getItem("token")
                }
            })
            const data= await res.json()
        }
        catch(error){

        }
    }
    const comment_container=document.getElementById("show-comments")
    const fetch_comment_get= async(id)=>{
        const res= await fetch(`http://127.0.0.1:5000/get-comments/${id}`,{
            method:"GET",
            headers:{
                "token":sessionStorage.getItem("token"),
                "Content-Type":"application/json"
            }
        })
        const data= await res.json()
        console.log(data)
        if(!data["ERROR"]){
            const comments=data['data']
            comments.map(comment=>{
                const div=document.createElement("div")
                div.classList="box"
                div.innerHTML=`
                    <div class="user">
                        <img src="${comment.user_image}" alt="">
                        <div>
                            <h3>${comment.name}</h3>
                            <span>${comment.upload_date}</span>
                        </div>
                    </div>
                    <div class="text">${comment.description}</div>
                `
                comment_container.appendChild(div)
            })
            
        }
    }
    const params=new URLSearchParams(window.location.search)
    await fetch_video(params.get("id"))
    await fetch_comment_get(params.get("id"))
    const comment_form=document.getElementById("add-comment")
    comment_form.addEventListener("submit",async(event)=>{
        event.preventDefault()
        const frm=event.target
        const payload=new FormData(frm)
        await fetch_comment_post(payload,params.get("id"),localStorage.getItem("id"))
        await fetch_comment_get(params.get("id"))
    })
})