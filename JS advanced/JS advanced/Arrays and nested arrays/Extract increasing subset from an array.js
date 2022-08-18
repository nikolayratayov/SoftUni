function solve(arr){
    let new_arr = []
    for (let i = 0; i < arr.length; i++){
        if (arr[i] >= Math.max(...new_arr)){
            new_arr.push(arr[i])
        }
    }
    return new_arr
}