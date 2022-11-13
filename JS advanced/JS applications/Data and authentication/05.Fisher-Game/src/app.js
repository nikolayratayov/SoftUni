window.addEventListener('DOMContentLoaded', onLoadHTML)
document.getElementById('logout').addEventListener('click', onLogout)

async function onLogout(){
    let url = 'http://localhost:3030/users/logout';
    let header = getHeader('GET', null);
    let response = await fetch(url, header);
    sessionStorage.clear();
    onLoadHTML();
    
}

function onLoadHTML(){
    let token = sessionStorage.getItem('accessToken');
    if (token){
        document.getElementById('guest').style.display = 'none';
        document.getElementById('user').style.display = 'inline-block';
    }
    else{
        document.getElementById('guest').style.display = 'inline-block';
        document.getElementById('user').style.display = 'none';
    }
}

function getHeader(method, body, ){
    let token = sessionStorage.getItem('accessToken')
    let header = {
        method: `${method}`,
        headres: {
            'Content-type': 'application/json',
            'X-Authorization': token
        }
    }
    if (body){
        header.body = JSON.stringify(body)
    }
    return header
}