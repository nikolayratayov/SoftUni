function solve(a){
    let min_1 = Math.min(...a)
    idx = a.indexOf(min_1)
    a.splice(idx, 1)
    let min_2 = Math.min(...a)
    console.log(`${min_1} ${min_2}`)
}