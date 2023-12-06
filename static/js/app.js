
// Store the previously accessed URL in session storage
let previousURL = sessionStorage.getItem('previousURL') || document.referrer;

// Update session storage with the current URL
sessionStorage.setItem('previousURL', window.location.href);

let preveNav = document.querySelector('#prev-nav')

preveNav.addEventListener('click', ()=>{
    window.location.href = `${previousURL}`
})
