function solve(a, crit){
    let arr = a;
    let sorted_arr = [];
    if (crit == 'asc'){
        return arr.sort(function(a, b){return a - b})
    }
    else{
        return arr.sort(function(a, b){return b - a})
    }
}
