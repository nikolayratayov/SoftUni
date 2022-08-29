/* function generateReport() {
    let result = [];
    let arr_nums = [];
    let keys = [];
    let inputs = document.querySelectorAll('table>thead>tr>th>input');
    for(let i = 0; i < inputs.length; i++){
        if(inputs[i].checked){
            arr_nums.push(i);
            keys.push(inputs[i].name)
        }
    }
    let rows = document.querySelectorAll('tbody>tr');
    for(let i = 0; i < rows.length; i++){
        let row = rows[i].getElementsByTagName('td');
        let obj = {};
        for(let j = 0; j < row.length; j++){
            if (arr_nums.includes(j)){
                obj[keys[j]] = row[j].textContent;
            }
        }
        result.push(obj);
    }
    let json_text = JSON.stringify(result, null, 2);
    document.getElementById('output').innerHTML = json_text;
} */
function generateReport() {
    let checkboxes = document.querySelectorAll('table>thead>tr>th>input');
    let rows = document.querySelectorAll('tbody>tr');
    let output = [];
    for (let i = 0; i < rows.length; i++) {
        let obj = {};
        let values = Array.from(rows[i].getElementsByTagName('td')).map(el => el.textContent);
        for (let j = 0; j < checkboxes.length; j++) {
            if (checkboxes[j].checked) {
                obj[checkboxes[j].name] = values[j];
            }
        }
        output.push(obj);
    }
    document.querySelector('#output').value = JSON.stringify(output, null, 2);
}