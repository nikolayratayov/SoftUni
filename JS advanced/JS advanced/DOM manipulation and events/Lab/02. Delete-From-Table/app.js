function deleteByEmail() {
    let email = document.getElementsByTagName('input')[0].value;
    let rows = document.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
    let result = '';
    for (let i = 0; i < rows.length; i++){
        let cell = rows[i].getElementsByTagName('td')[1].innerHTML;
        if (email == cell){
            rows[i].remove();
            result = 'Deleted.';
            break
        }
    }
    if (result == ''){result = 'Not found.'}
    document.getElementById('result').innerHTML = result;
}