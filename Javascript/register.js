
const my_form=document.getElementById("register-form")
my_form.addEventListener('submit', function(event){
    event.preventDefault()
    const form=event.target
    const payload=new FormData(form)
    console.log(payload.get('con_pass'))
    payload.delete('con_pass')
    console.log(payload.get('con_pass'))
    console.log('con_pass')
    fetch("http://127.0.0.1:5000/add-user", {
        method: "POST",
        body: payload
    })
    .then(res=>res.json())
    .then(data=>console.log(data))
})
