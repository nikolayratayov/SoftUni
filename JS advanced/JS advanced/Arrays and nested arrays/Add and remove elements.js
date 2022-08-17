function solve(arr){
    let num = 0
    new_arr = []
    for (let i = 0; i < arr.length; i++){
        num += 1
        if (arr[i] == 'add'){
            new_arr.push(num)
        }
        else{
            new_arr.pop()
        }
    }
    if (new_arr.length == 0){
        console.log('Empty')
    }
    else{
        console.log(new_arr.join('\n'))
    }
}