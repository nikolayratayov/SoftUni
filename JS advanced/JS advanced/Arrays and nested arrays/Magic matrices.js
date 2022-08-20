function solve(arr){
    let da = true
    for (let i = 0; i < arr[0].length; i++){
        let sum1 = arr[0].reduce(function(acum, curr){return acum + curr})
        let sum2 = 0
        for (let j = 0; j < arr.length; j++){
            sum2 += arr[j][i]
        }
        if (sum1 != sum2){
            da = false
            break
        }
    }
    console.log(da)
}