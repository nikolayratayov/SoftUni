function solve(a){
    let left_diag = []
    let right_diag = []
    for (let i = 0; i < a.length; i++){
        left_diag.push(a[i][i])
        right_diag.push(a[(a.length) - i - 1][i])
    }
    let sum_left = left_diag.reduce((acum, current) => acum + current)
    let sum_right = right_diag.reduce((acum, current) => acum + current)
    console.log(`${sum_left} ${sum_right}`)
}