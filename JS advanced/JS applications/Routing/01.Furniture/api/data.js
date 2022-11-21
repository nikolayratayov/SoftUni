import * as api from './api.js'

let endpoint = {
    'login': 'users/login',
    'register': 'users/register',
    'logout': 'users/logout',
    'createItem': 'data/catalog',
    'getAllItem': 'data/catalog',
    'getItemBbyId': 'data/catalog/',
    'myItem': 'data/catalog?where=_ownerId%3D%22'
}

export async function login(email, password){
    let res = await api.post(endpoint.login, {email, password});
    sessionStorage.setItem('userData', JSON.stringify(res));
    return res;
}

export async function register(email, password){
    let res = await api.post(endpoint.register, {email, password})
    sessionStorage.setItem('userData', JSON.stringify(res));
    return res;
}

export async function logout(){
    let res = await api.get(endpoint.logout);
    sessionStorage.removeItem('userData');
    return res
}

export async function createItem(data){
    let res = await api.post(endpoint.createItem, data);
    return res;
}

export async function getAllItem(){
    let res = await api.get(endpoint.getAllItem);
    return res;
}

export async function getItemById(id){
    let res = await api.get(endpoint.getItemBbyId + id);
    return res;
}

export async function updateById(id, data){
    let res = await api.put(endpoint.getItemBbyId + id, data);
    return res;
}

export async function deleteItem(id){
    let res = await api.del(endpoint.getItemBbyId + id);
    return res;
}

export async function getMyItems(){
    let userData = JSON.parse(sessionStorage.getItem('userData'))
    let userId = userData._id
    let id = `${userId}%22`
    let res = await api.get(endpoint.myItem + id);
    return res;
}