function solve(len, count){
    arr = []
    arr.push(1)
    let num
    let reducer = (acum, current) => acum + current
    for (let i = 2; i <= len; i++){
        if (i <= count) {
            num = arr.reduce(reducer);
        }
        else {
            num = arr.slice(-count).reduce((acc, val) => acc + val);
        }
        arr.push(num)
    }
    return(arr)
}