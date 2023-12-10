const csrftoken = document.cookie.match(/csrftoken=(\w+)/)[1]
let option = {
    "method":"post",
    "credentials": 'include',
    "headers":{
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
    },
}


async function fetchData(url) {
    const response = await fetch(url);
    const data = await response.json();
    return data;
}

async function postData(url, option) {
    const response = await fetch(url, option);
    const data = await response.json();
    return data;
}

async function renderModelList(url) {
    const data = await fetchData(url);
    // Render your model data here
    let itemElement = document.querySelector('#tbody');
    const paginationContainer = document.getElementById('pagination-ul');
    itemElement.innerHTML = '';
    data.results.forEach(player => {
        
        itemElement.insertAdjacentHTML("afterbegin", `
            <tr class="border-bottom p-3 py-5 align-items-center align-self-center">
                <td>
                    <a href="#" class="player__name nav-link">
                        <img class="img player__name-image" data-player="${player.code}" data-size="40x40" src="https://resources.premierleague.com/premierleague/photos/players/40x40/p${player.code}.png" alt="Photo for ${player.player}" onerror="setDefaultImage(${player.code});">
                        ${player.player}
                    </a> 
                </td>
                <td>${player.position}</td>
                <td>${player.team_id}</td>
                <td><button data-codeid="${player.code}" class="btn-primary p-1 add-player" style="font-size:10px;">Add</button></td>
            </tr>
            
            `
        )

    });

    // Render pagination links
    paginationContainer.innerHTML = '';

    if (data.previous) {
        paginationContainer.innerHTML += `
            <li class="page-item">
                <a class="page-link" href="${data.previous}">&laquo; Previous</a>
            </li>
        `
    }

    //stepLinks.innerHTML += `<span class="current">Page ${data.current_page} of ${data.num_pages}.</span>`;

    if (data.next) {

        paginationContainer.innerHTML += `
            <li class="page-item">
                <a class="page-link" href="${data.next}">Next</a>
            </li>
        `
    }
    

    postPlayerData()

}

// Example: Fetch on pagination link click
const paginationContainer = document.getElementById('pagination-ul');

paginationContainer.addEventListener('click', (event) => {
    if (event.target.tagName === 'A') {
        event.preventDefault();
        renderModelList(event.target.href);
    }
});




function setDefaultImage(id) {
    let imgEl = document.querySelector(`[data-player="${id}"]`)
    imgEl.src = 'https://resources.premierleague.com/premierleague/photos/players/40x40/Photo-Missing.png';
    
}
async function postPlayerData(){
    let addPlayerToTeamEl = document.querySelectorAll('.add-player')
    for(let i of addPlayerToTeamEl){
        i.addEventListener("click", ()=>{
            let code = i.dataset.codeid
            option["body"] = JSON.stringify({"code":code,})
            let endpoint = "/api/squad/add/"
            postData(endpoint, option)
            .then((data)=>{
                console.log(data)
                if (data.error){  
                    let items = data.team                 
                    let createSquadForm = `
                        <div class="modal fade" id="exampleModalCenteredScrollable" tabindex="-1" aria-labelledby="exampleModalCenteredScrollableTitle" style="display: none;" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalCenteredScrollableTitle">Create Team</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <p class="text-danger">You must first create a team name before adding players</p>
                                <form method="post" enctype="multipart/form-data"  novalidate="" class="needs-validation" id="form-team">

                                    <p class="form-text error-text text-danger">
                                    </p>        
                                    
                                    <div class="input-group mb-3">
                                        <input type="text" name="my_team" class="form-control" placeholder="Team Name" required="" value="">
                                        <div class="input-group-append">
                                            <div class="input-group-text">
                                                <span class="fas fa-users-cog"></span>
                                            </div>
                                        </div>
                                        <div class="invalid-feedback">
                                            Enter a Valid Name
                                        </div>

                                    </div>

                                    <div class="input-group mb-3">
                                        <select name="team_id" class="form-control">
                                        ${items.map(item => `<option value="${item}">${item}</option>`).join('')}
                                        
                                        </select>
                                        <div class="input-group-append">
                                            <div class="input-group-text">
                                                <span class="fas fa-users"></span>
                                            </div>
                                        </div>
                                        <div class="invalid-feedback">
                                            Enter a Valid Team Name
                                        </div>

                                    </div>
                                    
                                    
                                    
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button type="submit" class="btn btn-primary">save</button>
                                    </div>
                                </form>
                            </div>
                            
                        </div>
                        </div>
                    </div>
                    `

                    document.body.insertAdjacentHTML('beforebegin', createSquadForm) 
                    $('#exampleModalCenteredScrollable').modal('show');
                    creatUserTeam()
                }
                if (data.error_message){
                    errorMessage(data.error_message)
                }
                if(data.message){
                    window.location.reload()
                }
            })
            
        })
    }
}

async function creatUserTeam(){
    let form_team_el = document.querySelector('#form-team')
    form_team_el.addEventListener("submit", (event)=>{
        event.preventDefault()
        if(form_team_el.checkValidity()){
            let formData = new FormData(form_team_el)
            let formDataObj = Object.fromEntries(formData)
            console.log(formDataObj)
            let endpoint = "/api/squad/create-user-team/"
            option["body"] = JSON.stringify(formDataObj)
            postData(endpoint, option)
            .then((data)=>{
                console.log(data)
                if(data.message){
                    $('#exampleModalCenteredScrollable').modal('hide');
                }
                
            })
            
        }
        
    })
}


function errorMessage(error_message){            
    let createSquadForm = `
        <div class="modal fade" id="error-message" tabindex="-1" aria-labelledby="errorMessageTitle" style="display: none;" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
            <div class="modal-header">
            <h5 class="modal-title" id="errorMessageTitle">Create Team</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <p class="text-danger">${error_message}</p>
                
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
        </div>
        </div>
        </div>
    `

    document.body.insertAdjacentHTML('beforebegin', createSquadForm) 
    $('#error-message').modal('show');
}