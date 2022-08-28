function extract(content) {
    let text = document.getElementById(content).innerHTML;
    let regex = /\((.+?)\)/g;
    let found = [...text.matchAll(regex)];
    let arr = [];
    for (let i = 0; i < found.length; i++){
        arr.push(found[i][1]);
    }
    let variable = arr.join('; ');
    return variable;
}