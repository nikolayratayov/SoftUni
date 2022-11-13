document.getElementById('login-form').addEventListener('submit', loginHandler)
document.querySelectorAll('a').forEach(x => x.classList.remove('active'))
document.getElementById('login').classList.add('active')

function loginHandler(e){
    e.preventDefault();

    let form = e.target 
    let formData = new FormData(form)
    let {email, password} = Object.fromEntries(formData);

    onLogin(email, password)
}

async function onLogin(email, password){
    let url = 'http://localhost:3030/users/login';
    let body = {
        email,
        password
    }
    let header = getHeader('POST', body)
    let response = await fetch(url, header)
    let data = await response.json();

    sessionStorage.setItem('email', data.email);
    sessionStorage.setItem('accessToken', data.accessToken);
    window.location = './index.html'
    return data
}

function getHeader(method, body){
    return {
        method: `${method}`,
        headres: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(body)
    }
}