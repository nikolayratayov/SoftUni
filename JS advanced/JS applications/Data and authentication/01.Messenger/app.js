function attachEvents() {
    let url = 'http://localhost:3030/jsonstore/messenger';
    document.getElementById('refresh').addEventListener('click', refresh);
    document.getElementById('submit').addEventListener('click', submit);

    async function refresh(){
        let response = await fetch(url);
        let data = await response.json();
        
        let msgs = '';
        for (let i in data){
            msgs += `${data[i]['author']}: ${data[i]['content']}\n`;
        }

        msgs = msgs.substring(0, msgs.length - 1);
        document.getElementById('messages').innerHTML = msgs;
    }

    async function submit(){
        let author = document.getElementsByTagName('input')[0].value;
        let content = document.getElementsByTagName('input')[1].value;
        let obj = {
            'author': author,
            'content': content
        }

        let request = await fetch(url, {
            'method': 'POST',
            'headers': {
                'Content-type': 'application/json'
            },
            'body': JSON.stringify(obj)
        })
        let data = await request.json();
        return data;
    }
}

attachEvents();