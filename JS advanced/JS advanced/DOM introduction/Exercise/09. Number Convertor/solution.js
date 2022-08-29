function solve() {
    let fop = document.getElementById('selectMenuTo').getElementsByTagName('option')[0];
    fop.innerHTML = 'Binary';
    fop.setAttribute('value', 'binary');
    let sop = document.createElement('option');
    sop.innerHTML = 'Hexadecimal';
    sop.setAttribute('selected', '');
    sop.setAttribute('value', 'hexadecimal');
    document.getElementById('selectMenuTo').appendChild(sop);
    document.getElementsByTagName('button')[0].addEventListener('click', onclick)
    function onclick(){
        let num = parseFloat(document.getElementById('input').value);
        let dest = document.getElementById('selectMenuTo').value;
        let result;
        if (dest == 'binary'){
            result = num.toString(2);
        }
        else{
            result = (num.toString(16)).toUpperCase();
        }
        document.getElementById('result').value = result;
    }
}