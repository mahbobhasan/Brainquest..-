document.addEventListener("DOMContentLoaded",async (event)=>{
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
    let params = new URLSearchParams(window.location.search);
    let id = params.get('id');
    // console.log(searchTerm)
    const fetch_course= async (id) =>{
        try{
            const res=await fetch(`http://127.0.0.1:5000/course/${id}`,{
                method:"GET",
                headers:{
                    "token":sessionStorage.getItem("token"),
                    "Content-Type":"application/json"
                }
            })
            return res.json()
        }
        catch(error){
            return {"ERROR":error.message}
        }
    }

    const data= await fetch_course(id)
    console.log(data)

    if(!data["ERROR"]){
        const course_desc=document.getElementById('course-description')
        const course=await data['data']['course']
        course_desc.classList='row'
        course_desc.innerHTML=`
            <div class="columns">
                <div class="thumb">
                    <span>${course['course_number']} Videos</span>
                    <img src="${course['image']}" alt="" >
                </div>
            </div>
            <div class="col">
                <div class="tutor">
                    <img src="${course['teacher_image']}" alt="">    
                    <div>
                        <h3>${course['teacher']}</h3>
                        <span>Physics Co-ordinator</span>
                    </div>

                </div>
                <div class="details">
                    <h3>${course['name']}</h3>
                    <p>${course['description']}</p>
                    <div class="date">
                        <i class="fas fa-calendar"></i>
                        <span>${course['upload_date']}</span>
                    </div>
                </div>
            </div>
        `
        const videos=await data['data']['videos']
        console.log(videos)
        const video_container=document.getElementById("video-container")
        videos.map(video => {
            const vid=document.createElement('a')
            vid.href=`watch-video.html?id=${video.id}`
            vid.classList='box'
            vid.innerHTML=`
                <i class="fas fa-play"></i>
                <img src="${video['thumbnail']}" alt="">
                <h3>${video['title']}</h3>
            `
            video_container.appendChild(vid)
        })
    }
})

