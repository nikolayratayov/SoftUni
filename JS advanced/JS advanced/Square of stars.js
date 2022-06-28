function solve(a){
    let x = '* '
    if (typeof(a) == 'undefined'){
        for (let i = 1; i <= 5; i++){
            console.log(x.repeat(5));
        }
    }
    else{
        for (let i = 1; i <= a; i++){
            console.log(x.repeat(a));
        }
    }
}