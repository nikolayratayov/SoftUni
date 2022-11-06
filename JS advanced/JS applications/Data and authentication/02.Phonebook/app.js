/* function attachEvents() {
    document.getElementById('btnLoad').addEventListener('click', load);
    document.getElementById('btnCreate').addEventListener('click', create);

    async function load(){
        let response = await fetch('http://localhost:3030/jsonstore/phonebook');
        let data = await response.json();

        document.getElementById('phonebook').innerHTML = '';
        for (let i in data){
            let li = document.createElement('li');
            li.innerHTML = `${data[i]['person']}: ${data[i]['phone']}`

            let btn = document.createElement('button');
            btn.innerHTML = 'Delete'
            btn.id = i;
            btn.addEventListener('click', delete_record)

            li.appendChild(btn)

            document.getElementById('phonebook').appendChild(li);
        }
    }

    async function create(){
        let person = document.getElementById('person').value;
        let phone = document.getElementById('phone').value;
        document.getElementById('person').value = '';
        document.getElementById('phone').value = '';

        let response = await fetch('http://localhost:3030/jsonstore/phonebook', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json'
            },
            body: JSON.stringify({'person': person, 'phone': phone})
        })
        let data = await response.json();
        
        load();
        return data
    }

    async function delete_record(evt){
        let id = evt.currentTarget.id
        let response = await fetch(`http://localhost:3030/jsonstore/phonebook/${id}`, {
            method: 'DELETE'
        })
        let data = await response.json();
        evt.target.parentElement.remove();
        return data
    }
}

attachEvents(); */

function attachEvents(){
    document.getElementById('btnLoad').addEventListener('click', onLoadAllRecords);
    document.getElementById('btnCreate').addEventListener('click', handleCreateRecord)
}

function handleCreateRecord(){
    const personEl = document.getElementById('person');
    const phoneEl = document.getElementById('phone');

    onCreateRecord(personEl.value, phoneEl.value)
    personEl.value = '';
    phoneEl.value = '';
}

function renderRecord(data){
    const ul = document.getElementById('phonebook');
    ul.innerHTML = '';
    Object.values(data).forEach(rec => {
        const li = document.createElement('li');
        li.textContent = `${rec.person}: ${rec.phone}`;
        li.setAttribute('data-id', rec._id);

        const btn = document.createElement('button');
        btn.textContent = 'Delete';
        btn.addEventListener('click', handleDelete)
        li.appendChild(btn);
        ul.appendChild(li);
    })
}

function handleDelete(e){
    const li = e.target.parentElement;
    const id = li.getAttribute('data-id');
    onDeleteRecord(id);
    li.remove();
}

async function onLoadAllRecords(){
    const url = 'http://localhost:3030/jsonstore/phonebook';
    const response = await fetch(url);
    const data = await response.json();
    return renderRecord(data)
}

async function onCreateRecord(person, phone){
    const url = 'http://localhost:3030/jsonstore/phonebook';
    const body = {
        person,
        phone
    }
    const header = getHeader('POST', body);
    const response = await fetch(url, header);
    const data = await response.json();
    onLoadAllRecords();
    return data
}

async function onDeleteRecord(id){
    const url = `http://localhost:3030/jsonstore/phonebook/${id}`;
    const header = getHeader('DELETE', null);
    const response = await fetch(url, header);
    const data = await response.json();;
    return data;
}

function getHeader(method, body){
    return {
        method: `${method}`,
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(body)
    }
}

attachEvents()