function solve(arr){
    let a = []
    let didnt_break = true
    function operate(a, b, sign){
        if (sign == '+'){return a + b}
        else if (sign == '-'){return a - b}
        else if (sign == '*'){return a * b}
        else if (sign == '/'){return a / b}
    }
    for (let item of arr){
        if (typeof(item) == 'string'){
            if (a.length < 2){
                console.log('Error: not enough operands!');
                didnt_break = false
                break
            }
            else{
                let second = a.pop();
                let first = a.pop();
                a.push(operate(first, second, item))
            }
        }
        else{
            a.push(item);
        }
    }
    if (a.length > 1 && didnt_break){
        console.log('Error: too many operands!')
    }
    else if (didnt_break){
        console.log(a[0])
    }
}