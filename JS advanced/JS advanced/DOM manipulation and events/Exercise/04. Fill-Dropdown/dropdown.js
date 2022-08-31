function addItem() {
    let text = document.getElementById('newItemText').value;
    let val = document.getElementById('newItemValue').value;
    let op = document.createElement('option');
    op.setAttribute('value', val);
    op.innerHTML = text;
    document.getElementById('menu').appendChild(op);
    document.getElementById('newItemText').value = '';
    document.getElementById('newItemValue').value = '';
}