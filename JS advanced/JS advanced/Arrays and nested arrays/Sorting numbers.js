function solve(arr){
    new_arr = []
    let len = arr.length
    for (let i = 0; i < len; i++){
        if (i % 2 == 0){
            let a = Math.min(...arr)
            let idx = arr.indexOf(a)
            arr.splice(idx, 1)
            new_arr.push(a)
        }
        else{
            let a = Math.max(...arr)
            let idx = arr.indexOf(a)
            arr.splice(idx, 1)
            new_arr.push(a)
        }
    }
    return new_arr
}