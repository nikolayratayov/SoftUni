function subtract() {
    let first = parseFloat(document.getElementById('firstNumber').value);
    let second = parseFloat(document.getElementById('secondNumber').value);
    let result = first - second;
    document.getElementById('result').innerHTML = result;
}