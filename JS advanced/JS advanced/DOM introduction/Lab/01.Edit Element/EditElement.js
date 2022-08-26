function editElement(a, b, c) {
    let re = new RegExp(b, 'g');
    a.innerHTML = a.innerHTML.replace(re, c);
}