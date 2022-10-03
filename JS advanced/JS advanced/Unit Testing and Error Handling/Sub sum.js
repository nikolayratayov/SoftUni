function solve(arr, s, e){
    if (typeof(arr) !== 'object'){return NaN}
    let start = s;
    let end = e;
    if (start < 0){start = 0}
    if (end >= arr.length){end = arr.length - 1}
    let sum = 0
    for (let i = start; i <= end; i++){
        sum += Number(arr[i])
    }
    return sum;
}
