function solve(arr){
    arr.sort(function(a, b){
        let len_a = a.length
        let len_b = b.length
        if (len_a === len_b){
            if (a < b){
                return -1
            }
            else{
                return 1
            }
        }
        return len_a - len_b
    })
    console.log(arr.join('\n'))
}