import { del, get, post, put } from "./api.js";

export async function getAll(){
    return get('/data/offers?sortBy=_createdOn%20desc');

}

export async function getById(id){
    return get('/data/offers/' + id);
}

export async function deleteById(id){
    return del('/data/offers/' + id);
}

export async function createJob(jobData){
    return post('/data/offers', jobData)
}

export async function editJob(id, jobData){
    return put('/data/offers/' + id, jobData)
}