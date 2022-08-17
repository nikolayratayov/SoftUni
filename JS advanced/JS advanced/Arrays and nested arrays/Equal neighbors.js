function solve(a){
    let count = 0
    for (let i = 0; i < a.length; i++){
        for (let j = 0; j < (a[0].length) - 1; j++){
            if (a[i][j] === a[i][j + 1]){
                count += 1
            }
        }
    }
    for (let i = 0; i < a.length - 1; i++){
        for (let j = 0; j < a[0].length; j++){
            if (a[i][j] === a[i + 1][j]){
                count += 1
            }
        }
    }
    return count
}