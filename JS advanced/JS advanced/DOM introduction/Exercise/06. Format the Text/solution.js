function solve() {
    let text = document.getElementById('input').value;
    let sentances = text.split('.');
    let count = 0;
    let text_to_append = '';
    for(let sent of sentances){
        if (sent.length < 1){
          continue
        }
        count += 1;
        if (count <= 3){
          text_to_append += `${sent}.`;
        }
        else{
          document.getElementById('output').innerHTML += `<p>${text_to_append}</p>`;
          count = 1;
          text_to_append = '';
          text_to_append = `${sent}.`;
        }
    }
    document.getElementById('output').innerHTML += `<p>${text_to_append}</p>`;
}