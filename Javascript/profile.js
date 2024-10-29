
console.log("hello")
async function fetch_api_data(){
    try {
        const params = new URLSearchParams(window.location.search); 

        const id=Number(params.get('id'));
        const response=await fetch(`http://127.0.0.1:5000/user/${id}`)
        api_data= await response.json()
        api_data=api_data['data']
        console.log(api_data)
        show_details(api_data)
    } catch (error) {
        // console.log(error)
    }
}
fetch_api_data()

const show_details=(data)=>{
    const container=document.querySelector('.details')
    container.innerHTML=`
        <div class="tutor">
                <img src="${data.image}" alt="">
                <h3>${data.name}</h3>
                <span>Physics Co-ordinator</span>
            </div>
            <div class="flex">
                <p>Total Playlist :   <span>4</span></p>
                <p>Total Videos :   <span>11</span></p>
                <p>Total Likes : <span>998</span></p>
                <p>Total Comments : <span>52</span></p>
            </div>
    `
}