function solve(a){
    let type = typeof(a);
    if (type == 'number'){
        console.log((a * a * Math.PI).toFixed(2));
    }else {
        console.log(`We can not calculate the circle area, because we receive a ${type}.`);
    }
}