window.addEventListener('load', solve);

function solve() {
    document.getElementsByTagName('button')[0].addEventListener('click', (evt) => evt.preventDefault());
    document.getElementsByTagName('button')[0].addEventListener('click', send);
    document.getElementsByClassName('clear-btn')[0].addEventListener('click', clear)

    function send(){
        let type = document.getElementById('type-product').value;
        let description = document.getElementById('description').value;
        let client_name = document.getElementById('client-name').value;
        let client_phone = document.getElementById('client-phone').value;

        if (description && client_name && client_phone){
            document.getElementById('description').value = '';
            document.getElementById('client-name').value = '';
            document.getElementById('client-phone').value = '';

            let h2 = document.createElement('h2');
            h2.innerHTML = 'Product type for repair: ' + type;

            let h3 = document.createElement('h3');
            h3.innerHTML = `Client information: ${client_name}, ${client_phone}`;

            let h4 = document.createElement('h4');
            h4.innerHTML = `Description of the problem: ${description}`;

            let btn_start = document.createElement('button');
            btn_start.className = 'start-btn';
            btn_start.innerHTML = 'Start repair';
            btn_start.addEventListener('click', repair);

            let btn_finish = document.createElement('button');
            btn_finish.className = 'finish-btn';
            btn_finish.innerHTML = 'Finish repair';
            btn_finish.addEventListener('click', finish)
            btn_finish.disabled = true;

            let div = document.createElement('div');
            div.className = 'container';
            div.appendChild(h2)
            div.appendChild(h3)
            div.appendChild(h4)
            div.appendChild(btn_start)
            div.appendChild(btn_finish)

            document.getElementById('received-orders').appendChild(div);
        }
    }

    function repair(evt){
        evt.currentTarget.parentElement.getElementsByTagName('button')[0].disabled = true;
        evt.currentTarget.parentElement.getElementsByTagName('button')[1].disabled = false;
    }

    function finish(evt){
        let div = evt.currentTarget.parentElement;
        evt.currentTarget.parentElement.remove();
        div.getElementsByTagName('button')[0].remove();
        div.getElementsByTagName('button')[0].remove();

        document.getElementById('completed-orders').appendChild(div);

    }

    function clear(){
        let h2 = document.getElementById('completed-orders').getElementsByTagName('h2')[0];
        let img = document.getElementById('completed-orders').getElementsByTagName('img')[0];
        let btn = document.getElementById('completed-orders').getElementsByTagName('button')[0];
        document.getElementById('completed-orders').innerHTML = '';
        document.getElementById('completed-orders').appendChild(h2);
        document.getElementById('completed-orders').appendChild(img);
        document.getElementById('completed-orders').appendChild(btn);
    }
}