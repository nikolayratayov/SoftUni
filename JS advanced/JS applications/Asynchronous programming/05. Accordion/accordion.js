async function button_click(evt){
    let id = evt.currentTarget.id;

    let response = await fetch(`http://localhost:3030/jsonstore/advanced/articles/details/${id}`);
    let data = await response.json();

    if (evt.target.innerHTML == 'More'){
        evt.target.innerHTML = 'Less';
        evt.target.parentElement.parentElement.getElementsByTagName('p')[0].innerHTML = data.content;
        evt.target.parentElement.parentElement.getElementsByTagName('div')[1].setAttribute('style', 'display: block');
    }
    else{
        evt.target.innerHTML = 'More';
        evt.target.parentElement.parentElement.getElementsByTagName('p')[0].innerHTML = '';
        evt.target.parentElement.parentElement.getElementsByTagName('div')[1].setAttribute('style', 'display: none');
    }
}


async function solution() {
    let response = await fetch('http://localhost:3030/jsonstore/advanced/articles/list');
    let data = await response.json();

    

    for (let i of data){
        let div_accordion = document.createElement('div');
        div_accordion.className = 'accordion';

        let span = document.createElement('span');
        span.innerHTML = i.title;

        let button = document.createElement('button');
        button.setAttribute('id', i._id);
        button.className = 'button';
        button.innerHTML = 'More';
        button.addEventListener('click', button_click);


        let div = document.createElement('div');
        div.className = 'head';

        div.appendChild(span);
        div.appendChild(button);

        div_accordion.appendChild(div);

        let p = document.createElement('p');

        let div_extra = document.createElement('div');
        div_extra.className = 'extra';
        div_extra.appendChild(p);

        div_accordion.appendChild(div_extra);

        document.getElementById('main').appendChild(div_accordion);

    }

    
}

solution();