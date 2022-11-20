import {html, render} from '../../../../node_modules//lit-html/lit-html.js'


let url = 'http://localhost:3030/jsonstore/advanced/dropdown';
let form = document.querySelector('form');
form.addEventListener('submit', onSubmit)
onLoadContent();

async function onLoadContent(){
    
    let response = await fetch(url);
    let data = await response.json();
    let root = document.getElementById('menu');
    let container = Object.values(data).map(x => createOptioTemplate(x));
    render(container, root);
}

function createOptioTemplate(option){
    return html`<option value=${option._id}>${option.text}</option>`
}

function onSubmit(e){
    e.preventDefault();
    let value = document.getElementById('itemText').value;
    addItem(value);
    document.getElementById('itemText').value = '';
    onLoadContent();
}

async function addItem(data) {
    let response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({text: data})
    })
}