function attachEventsListeners() {
function convert(){
    let input = document.getElementById('inputUnits');
    let output = document.getElementById('outputUnits');
    let num = parseFloat(document.getElementById('inputDistance').value);
    let meters;
    let distance;
    if (input.value == 'km'){meters = num * 1000}
    else if (input.value == 'm'){meters = num}
    else if (input.value == 'cm'){meters = num / 100}
    else if (input.value == 'mm'){meters = num / 1000}
    else if (input.value == 'mi'){meters = num * 1609.344}
    else if (input.value == 'yrd'){meters = num * 0.9144}
    else if (input.value == 'ft'){meters = num * 0.3048}
    else if (input.value == 'in'){meters = num * 0.0254}

    if (output.value == 'km'){distance = meters / 1000}
    else if (output.value == 'm'){distance = meters}
    else if (output.value == 'cm'){distance = meters * 100}
    else if (output.value == 'mm'){distance = meters * 1000}
    else if (output.value == 'mi'){distance = meters * 0.00062137119223733}
    else if (output.value == 'yrd'){distance = meters * 1.0936132983377}
    else if (output.value == 'ft'){distance = meters * 3.2808398950131}
    else if (output.value == 'in'){distance = meters * 39.370078740157}

    document.getElementById('outputDistance').value = distance;
}

    let btn = document.getElementById('convert')
    btn.addEventListener('click', convert)
}