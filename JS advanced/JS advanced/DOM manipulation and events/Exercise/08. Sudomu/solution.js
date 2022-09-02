function solve() {
    function check(){
        function check_nums(dim){
            let nums = document.getElementsByTagName('input');
            for (let i = 0; i < nums.length; i++){
                let num = parseFloat(nums[i].value);
                if ( num < 1 || num > dim){ return false}
            }
            return true
        }
        function check_different_nums(dim){
            let rows = document.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
            for (let i = 0; i < dim; i++){
                let arr = [];
                for (let j = 0; j < dim; j++){
                    let num = rows[i].getElementsByTagName('td')[j].getElementsByTagName('input')[0].value;
                    arr.push(num);
                }
                let set = new Set(arr);
                if (arr.length != set.size){return false}
            }
            for (let i = 0; i < dim; i++){
                let arr = [];
                for (let j = 0; j < dim; j++){
                    let num = rows[j].getElementsByTagName('td')[i].getElementsByTagName('input')[0].value;
                    arr.push(num);
                }
                let set = new Set(arr);
                if (arr.length != set.size){return false}
            }
            return true
        }
        let dimension = document.getElementsByTagName('tbody')[0].getElementsByTagName('tr').length;
        if (check_nums(dimension) && check_different_nums(dimension)){
            document.getElementsByTagName('table')[0].setAttribute('style', 'border: 2px solid green');
            let result = document.getElementById('check').getElementsByTagName('p')[0];
            result.setAttribute('style', 'color: green');
            result.innerHTML = 'You solve it! Congratulations!';
        }
        else{
            document.getElementsByTagName('table')[0].setAttribute('style', 'border: 2px solid red');
            let result = document.getElementById('check').getElementsByTagName('p')[0];
            result.setAttribute('style', 'color: red');
            result.innerHTML = 'NOP! You are not done yet...';
        }
    }
    function clear(){
        document.getElementsByTagName('table')[0].removeAttribute('style');
        document.getElementById('check').getElementsByTagName('p')[0].innerHTML = '';
        let inputs = document.getElementsByTagName('input');
        for (let i = 0; i < inputs.length; i++){
            inputs[i].value = null;
        }
    }
    let check_btn = document.getElementsByTagName('button')[0];
    let clear_btn = document.getElementsByTagName('button')[1];
    check_btn.addEventListener('click', check);
    clear_btn.addEventListener('click', clear);
}