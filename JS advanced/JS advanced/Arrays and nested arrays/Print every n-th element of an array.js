function solve(arr, n){
    let new_arr = []
    for (let i = 0; i < arr.length; i += n){
        new_arr.push(arr[i])
    }
    return new_arr
}