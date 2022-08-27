function extractText() {
    let a = document.getElementById('items').getElementsByTagName('li');
    let text = ''
    for (let i = 0; i < a.length; i++){
        text += a[i].innerHTML + '\n';
    }
    document.getElementById('result').innerHTML = text;
}