function solve(num, op1, op2, op3, op4, op5){
    function check(num, op){
        switch (op){
            case 'chop': num /= 2;
            number = num;
            break;
            case 'dice': num = Math.sqrt(num);
            number = num;
            break;
            case 'spice': num += 1;
            number = num;
            break;
            case 'bake': num *= 3;
            number = num;
            break;
            case 'fillet': num -= 0.2 * num;
            number = num;
            break;
        }
        console.log(number);
    }
    let number = num;
    check(number, op1);
    check(number, op2);
    check(number, op3);
    check(number, op4);
    check(number, op5);
}