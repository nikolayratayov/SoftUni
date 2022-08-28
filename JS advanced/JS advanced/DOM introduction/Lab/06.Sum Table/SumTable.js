function sumTable() {
    let table = document.getElementsByTagName('table');
    let row = table[0].getElementsByTagName('tr');
    let sum = 0
    for (let i = 1; i < row.length - 1; i++){
        let cell = row[i].getElementsByTagName('td');
        let num = parseFloat(cell.item(cell.length - 1).innerHTML);
        sum += num;
    }
    document.getElementById('sum').innerHTML = sum;
}