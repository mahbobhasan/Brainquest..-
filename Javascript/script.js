let body= document.body;


const header=document.getElementById("header")
header.innerHTML=`
            <section class="flex" >
                <a href="Home.html" class="logo">BrainQuest..!</a>

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

                <div class="profile">
                    <img src="Images/Pic-1.png" alt="">
                    <!-- need to add database -->
                    <h3>Username</h3>
                    <span>Student</span>
                    <a href="Profile.html" class="btn">Viewprofile</a>

                    <div class="flex-btn">
                        <a href="Login.html" class="option-btn">Login</a>
                        <a href="Register.html" class="delete-btn">Register</a>
                    </div>
                </div>


            </section>
`

let sidebar=document.getElementById("sidebar")
sidebar.innerHTML=`
        <div class="close-sidebar">
            <i class="fas fa-times"></i>
        </div>

        <div class="profile">
            <img src="Images/Pic-1.png" alt="">
            <!-- need to add database -->
            <h3>Username</h3>
            <span>Student</span>
            <a href="Profile.html" class="btn">Viewprofile</a>
        </div>
        <nav class="navbar">
            <a href="Home.html"><i class="fas fa-home"></i><span>Home</span></a>
            <a href="about.html"><i class="fas fa-question"></i><span>About Us</span></a>
            <a href="courses.html"><i class="fas fa-graduation-cap"></i><span>Our Courses</span></a>
            <a href="teachers.html"><i class="fas fa-chalkboard-user"></i><span>Our Teachers</span></a>
            <div class="dropdown-container">
                <a href="#"><i class="fas fa-users"></i> <span>Our Students</span></a>
                <div class="dropdown-content">
                    <a href="Users.html"id="2020-21">Session <span >2020-21</span></a>
                    <a href="Users.html"id="2021-22">Session <span >2021-22</span></a>
                    <a href="Users.html"id="2022-23">Session <span >2022-23</span></a>
                    <a href="Users.html"id="2023-24">Session <span >2023-24</span></a>
                </div>
            </div>
            <a href="contact.html"><i class="fas fa-headset"></i><span>Contact Us</span></a>
        </nav>
`


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




//    // document.addEventListener('DOMContentLoaded', function() {
            //     let body=document.body;
            //     let prof = document.querySelector('.header .flex .profile');
            //     document.querySelector('#user-btn').onclick = () => {
            //         prof.classList.toggle('active');
            //         search.classList.remove('active');
            //     }
            //     let search = document.querySelector('header .flex .search-form');
            //     document.querySelector('#search-btn').onclick = () =>{
            //         search.classList.toggle('active');
            //         prof.classList.remove('active');
            //     }               
            //     let side = document.querySelector('.sidebar');
            //     document.querySelector('#menu-btn').onclick = () =>{
            //         side.classList.toggle('active');
            //         body.classList.toggle('active');
            //     }   
            //     document.querySelector('.sidebar .close-sidebar').onclick =() =>{
            //         side.classList.toggle('active');
            //         body.classList.toggle('active');
            //     }
             
            //     window.onscroll = () => {
            //         prof.classList.remove('active');
            //         search.classList.remove('active');
            //         if(innerWidth<1200){
            //             side.classList.remove('active');
            //             body.classList.remove('active');
            //         }
            //     }
            // });
            // let toggleBtn = document.querySelector('#toggle-btn');
            //     let darkMode = localStorage.getItem('dark-mode');
            //     let body = document.querySelector('body');

            //     const enableDarkMode = () => {
            //         toggleBtn.classList.replace('fa-sun', 'fa-moon');
            //         body.classList.add('dark');
            //         localStorage.setItem('dark-mode', 'enabled');
            //     };

            //     const disableDarkMode = () => {
            //         toggleBtn.classList.replace('fa-moon', 'fa-sun');
            //         body.classList.remove('dark');
            //         localStorage.setItem('dark-mode', 'disabled');
            //     };

            //     if (darkMode === 'enabled') {
            //         enableDarkMode();
            //     }

            //     toggleBtn.onclick = () => {
            //         let darkMode = localStorage.getItem('dark-mode');
            //         if (darkMode === 'disabled') {
            //             enableDarkMode();
            //         } else {
            //             disableDarkMode();
            //         }
            //     };  