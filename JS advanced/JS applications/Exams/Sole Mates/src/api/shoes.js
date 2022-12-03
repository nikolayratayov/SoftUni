import { del, get, post, put } from "./api.js";

export async function getAll(){
    return get('/data/shoes?sortBy=_createdOn%20desc');
}

export async function getById(id){
    return get('/data/shoes/' + id);
}

export async function deleteById(id){
    return del('/data/shoes/' + id);
}

export async function createShoe(jobData){
    return post('/data/shoes', jobData)
}

export async function editShoe(id, jobData){
    return put('/data/shoes/' + id, jobData)
}

export async function searchShoe(query){
    return get(`/data/shoes?where=brand%20LIKE%20%22${query}%22`)
}