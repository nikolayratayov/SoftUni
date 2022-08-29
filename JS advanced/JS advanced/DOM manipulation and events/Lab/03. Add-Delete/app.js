function addItem() {
    function delItem(event){
        event.currentTarget.remove();
    }
    let ul = document.getElementById('items');
    let item = document.getElementById('newItemText').value;
    let li = document.createElement('li');
    li.innerHTML = item;
    li.setAttribute('id', item);
    
    let atag = document.createElement('a');
    atag.setAttribute('href', '#');
    atag.innerHTML = '[Delete]';
    li.appendChild(atag);
    ul.appendChild(li);

    let evt_lis = document.getElementById('items').getElementsByTagName('li');
    for (let i = 0; i < evt_lis.length; i++){
        evt_lis[i].addEventListener('click', delItem, true)
    }
}