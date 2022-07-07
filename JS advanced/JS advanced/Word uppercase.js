function solve(a){
    let pattern = /[a-zA-Z0-9]+/g
    let arr = a.match(pattern);
    let new_arr = [];
    for (let i = 0; i < arr.length; i++){
        let temp = arr[i].toUpperCase();
        new_arr.push(temp)
    }
    new_arr_sep = new_arr.join(', ')
    console.log(new_arr_sep);
}