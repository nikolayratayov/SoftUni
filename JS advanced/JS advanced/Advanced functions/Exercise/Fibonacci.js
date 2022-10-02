function solve(){
    let first = 0;
    let second = 0;
    return function(){
        if (first == 0 && second == 0){
            let next = 1
            first = second
            second = next
            return next
        }
        let next = first + second;
        first = second
        second = next
        return next
    }
}
