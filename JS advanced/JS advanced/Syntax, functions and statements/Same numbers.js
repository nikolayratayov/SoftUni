function solve(a){
    let text = a.toString();
    let check = true;
    let sum = 0;
    for (let i in text){
        if (text[i] != text[0]){
            check = false;
        }
        sum += parseInt(text[i]);
    }
    console.log(check);
    console.log(sum);
}