function solve() {

    function delete_from_sent(evt){
        let span_1 = evt.currentTarget.parentElement.parentElement.getElementsByTagName('span')[0]
        let span_2 = evt.currentTarget.parentElement.parentElement.getElementsByTagName('span')[1]
        let new_li = document.createElement('li');
        new_li.appendChild(span_1)
        new_li.appendChild(span_2)
        document.getElementsByClassName('delete-list')[0].appendChild(new_li)
        evt.currentTarget.parentElement.parentElement.remove()
    }

    function reset(){
        document.getElementById('title').value = '';
        document.getElementById('recipientName').value = '';
        document.getElementById('message').value = '';
    }

    function delete_mail(evt){
        let span_1 = evt.currentTarget.parentElement.parentElement.getElementsByTagName('h4')[1]
        let span_2 = evt.currentTarget.parentElement.parentElement.getElementsByTagName('h4')[0]
        let new_li = document.createElement('li');
        new_li.appendChild(span_1)
        new_li.appendChild(span_2)
        document.getElementsByClassName('delete-list')[0].appendChild(new_li)
        evt.currentTarget.parentElement.parentElement.remove()
    }

    function send(evt){
        let to = evt.currentTarget.parentElement.parentElement.getElementsByTagName('h4')[1].innerHTML;
        let title = evt.currentTarget.parentElement.parentElement.getElementsByTagName('h4')[0].innerHTML;

        let span_to = document.createElement('span');
        span_to.innerHTML = to;

        let span_title = document.createElement('span');
        span_title.innerHTML = title;

        let btn_delete = document.createElement('button');
        btn_delete.className = 'delete';
        btn_delete.setAttribute('type', 'submit');
        btn_delete.addEventListener('click', delete_from_sent)
        btn_delete.innerHTML = 'Delete';

        let div = document.createElement('div');
        div.className = 'btn';
        div.appendChild(btn_delete);
        
        let new_li = document.createElement('li');
        new_li.appendChild(span_to)
        new_li.appendChild(span_title)
        new_li.appendChild(div)

        document.getElementsByClassName('sent-list')[0].appendChild(new_li)
        
        evt.currentTarget.parentElement.parentElement.remove();
    }

    function add(){
        let recipient = document.getElementById('recipientName').value;
        let title = document.getElementById('title').value;
        let message = document.getElementById('message').value;

        if(recipient && title && message){
            let h4_title = document.createElement('h4');
            h4_title.innerHTML = 'Title: ' + title;
            document.getElementById('title').value = '';

            let h4_recipient = document.createElement('h4');
            h4_recipient.innerHTML = 'Recipient Name: ' + recipient;
            document.getElementById('recipientName').value = '';

            let span_message = document.createElement('span');
            span_message.innerHTML = message;
            document.getElementById('message').value = '';

            let div = document.createElement('div');
            div.setAttribute('id', 'list-action');

            let btn_send = document.createElement('button');
            btn_send.setAttribute('type', 'submit');
            btn_send.setAttribute('id', 'send');
            btn_send.innerHTML = 'Send';
            btn_send.addEventListener('click', send)

            let btn_delete = document.createElement('button');
            btn_delete.setAttribute('type', 'submit');
            btn_delete.setAttribute('id', 'delete');
            btn_delete.innerHTML = 'Delete';
            btn_delete.addEventListener('click', delete_mail)

            div.appendChild(btn_send);
            div.appendChild(btn_delete);

            let new_li = document.createElement('li');
            new_li.appendChild(h4_title)
            new_li.appendChild(h4_recipient)
            new_li.appendChild(span_message)
            new_li.appendChild(div)

            document.getElementById('list').appendChild(new_li)
        }
    }

    document.getElementById('add').addEventListener('click', (evt) => evt.preventDefault())
    document.getElementById('add').addEventListener('click', add)

    document.getElementById('reset').addEventListener('click', reset)
    document.getElementById('reset').addEventListener('click', (evt) => evt.preventDefault())
}
solve()