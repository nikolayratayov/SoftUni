let host = 'http://localhost:3030/';


async function request(url, options){
    try{
        let response = await fetch(host + url, options)
        if (!response.ok){
            let err = await response.json();
            throw new Error(err.message);
        }
        try{
            if (response.status === 204){
                return response;
            }
            let data = await response.json();
            return data;
        }
        catch(error){
            alert(error.message)
            return error;
        }
    }
    catch(error){
        alert(error.message)
    }
}

function getOption(method, body){
    let options = {
        method,
        headers: {}
    }

    let user = JSON.parse(sessionStorage.getItem('userData'));
    
    if (user){
        let token = user.accessToken;
        options.headers['X-authorization'] = token;
    }

    if(body){
        options['body'] = JSON.stringify(body);
        options.headers['Content-type'] = 'application/json';

    }
    return options;
}

export async function get(url){
    return await request(url, getOption('GET'));
}

export async function post(url, data){
    return await request(url, getOption('POST', data));
}

export async function put(url, data){
    return await request(url, getOption('PUT', data));
}

export async function del(url){
    return await request(url, getOption('DELETE'));
}
