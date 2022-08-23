function solve(a){
    let arr = [];
    let obj = {};
    for (let iterator of a){
        let [name, price] = iterator.split(' : ');
        price = parseFloat(price);
        arr.push(name);
        obj[name] = price;
    }
    arr.sort();
    let pattern = /[A-Z]/;
    let letter = arr[0].match(pattern);
    console.log(letter[0]);
    for (let item of arr){
        if(letter[0] == item[0]){
            console.log(`${item}: ${obj[item]}`)
        }
        else{
            letter = item.match(pattern);
            console.log(letter[0]);
            console.log(`${item}: ${obj[item]}`);
        }
    }
}