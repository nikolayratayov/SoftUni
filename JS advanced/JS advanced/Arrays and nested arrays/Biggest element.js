function solve(a){
    new_arr = []
    for (let i = 0; i < a.length; i++){
        new_arr.push(Math.max(...a[i]))
    }
    max_el = Math.max(...new_arr)
    return max_el
}