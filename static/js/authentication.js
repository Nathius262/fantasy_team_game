let formSigninEl = document.querySelector('#form-signin')
let formSignupEl = document.querySelector('#form-signup')
let option= {
    method:'post',
    headers:{"Content-Type":"application/json"},
}
let endpoint = '/api/auth/'

try {
    authenticate(formSigninEl, endpoint+"login/")
} catch (TypeError) {
    authenticate(formSignupEl, endpoint+"signup/")
}


// Store the previously accessed URL in session storage
let previousURL = sessionStorage.getItem('previousURL') || document.referrer;

// Update session storage with the current URL
sessionStorage.setItem('previousURL', window.location.href);

let preveNav = document.querySelector('#prev-nav')

preveNav.addEventListener('click', ()=>{
    window.location.href = `${previousURL}`
})

function authenticate(form, url) {
    form.addEventListener('submit', (event)=>{
        //let url = endpoint +"signup/"
        event.preventDefault()
        if(form.checkValidity()){
            let form_data = new FormData(form)
            let json_form = Object.fromEntries(form_data)
            option['body'] = JSON.stringify(json_form)
            errorMessage("")
            fetch(url, option)
            .then((response)=>{return response.json()})
            .then((data)=>{
                //console.log(data)
                if (data.non_field_errors){
                    errorMessage(data.non_field_errors)
                    
                }
                
                else if (data.username || data.password || data.password1 || data.email || data.password2){
                    
                    for (const key in data) {
                        if (data.hasOwnProperty(key)) {
                          const value = data[key];
                          errorMessage(`${key}: ${value}`);
                          //console.log(`${key}: ${value}`);
                        }
                    }
                    
                }
                
                else{
                   
                    window.location.href = '/'
                }
            })
            .catch((err)=>{
                errorMessage(err)
            })
        }
        
    })
}

function errorMessage(message){
    let err_message = document.querySelectorAll('.error-text')
    err_message.forEach(element => {
        element.insertAdjacentHTML('afterbegin', `<p>${message}<p>`)
    });
}