function solve(a){
    new_arr = []
    for (let i = 0; i < a.length; i++){
        if (a[i] < 0){
            new_arr.unshift(a[i])
        }
        else{
            new_arr.push(a[i])
        }
    }
    for (let i = 0; i < new_arr.length; i++){
        console.log(new_arr[i])
    }
}