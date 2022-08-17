function solve(a){
    a.sort(function(a, b){return a - b})
    let idx = Math.floor(a.length / 2)
    let b = a.slice(idx, a.length)
    return b
}