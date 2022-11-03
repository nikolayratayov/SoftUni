async function getInfo() {
    let id = document.getElementById('stopId').value;

    document.getElementById('buses').innerHTML = '';
    document.getElementById('stopId').value = '';

    try{
        let response = await fetch(`http://localhost:3030/jsonstore/bus/businfo/${id}`);
        let data = await response.json();

        document.getElementById('stopName').innerHTML = data.name;
        for (let key in data.buses) {
            let li = document.createElement('li');
            li.innerHTML = `Bus ${key} arrives in ${data.buses[key]} minutes`;
            document.getElementById('buses').appendChild(li);
        }
    }
    catch (error){
        document.getElementById('stopName').innerHTML = 'Error';
    }
}