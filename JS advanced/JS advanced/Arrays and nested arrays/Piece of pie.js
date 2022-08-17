function solve(arr, start, end){
    go = false
    let new_arr = []
    for (let i = 0; i < arr.length; i++){
        if (arr[i] === start){
            go = true
        }
        if (go){
            new_arr.push(arr[i])
        }
        if (arr[i] === end){
            go = false
        }
    }
    return(new_arr)
}