function solve(a, b){
    while (true){
        if (b == 0){
            console.log(a); break;
        }    
        a %= b;
        if (a == 0){
            console.log(b); break;
        }    
        b %= a;
    }
}