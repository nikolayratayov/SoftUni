import {html, render} from '../../../../node_modules/lit-html/lit-html.js'

let form = document.querySelector('form');
form.addEventListener('submit', onSubmit);
let root = document.getElementById('root');

function onSubmit(e){
    e.preventDefault();
    let towns = document.getElementById('towns').value.split(', ');
    renderTownList(towns);
    form.reset();
}

function renderTownList(data){
    let result = createTownList(data);
    render(result, root)
}

function createTownList(data){
    let ul = html`
        <ul>
            ${data.map(x => html`<li>${x}</li>`)}
        </ul>
    `
    return ul
}