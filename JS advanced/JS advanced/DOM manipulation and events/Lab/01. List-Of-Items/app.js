function addItem() {
    let new_item_text = document.getElementById('newItemText').value;
    let new_li = document.createElement('li');
    new_li.innerHTML = new_item_text;
    document.getElementById('items').appendChild(new_li);
}