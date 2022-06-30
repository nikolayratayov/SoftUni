function solve(a){
    sum = a.reduce(
        (previous, current) => previous + current
    );
    console.log(sum);

    let sum_rec = 0;
    for (let i = 0; i < a.length; i++){
        sum_rec += 1 / a[i];
    }
    console.log(sum_rec);

    let sum_str = '';
    for (let i = 0; i < a.length; i++){
        sum_str += a[i];
    }
    console.log(sum_str);
}