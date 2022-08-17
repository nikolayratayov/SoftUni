function solve(a){
    new_arr = []
    for (let i = 0; i < a.length; i++){
        if (i % 2 != 0){
            new_arr.unshift(a[i] * 2)
        }
    }
    return new_arr
}