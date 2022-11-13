document.getElementById('register-form').addEventListener('submit', registerHandler);
document.querySelectorAll('a').forEach(x => x.classList.remove('active'))
document.getElementById('register').classList.add('active')
let errorP = document.querySelector('p.notification');

function registerHandler(e){
    e.preventDefault();
    let form = e.target;
    let formData = new FormData(form);
    let {email, password, rePass} = Object.fromEntries(formData)
    if (password !== rePass){
        errorP.textContent = 'Error';
        setTimeout(() => {
            errorP.textContent = ''
        }, 1000)
    }
    else{
        onRegister(email, password);
    }
}

async function onRegister(email, password){
    
    let url = 'http://localhost:3030/users/register';
    let body = {
        email,
        password
    }
    let header = getHeader('POST', body);
    try{
        let response = await fetch(url, header);
        let data = await response.json();
        if (data.code && data.code !== 200){
            throw new Error(data.message)
        }
        sessionStorage.setItem('email', data.email);
        sessionStorage.setItem('accessToken', data.accessToken);
        window.location = './index.html'
        return data
    }
    catch(e){
        errorP.textContent = e
        setTimeout(() => {
            errorP.textContent = '';
        }, 1000)
    }


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