function validate() {
    document.getElementById('email').addEventListener('change', func);
    function func(){
        let email = document.getElementById('email').value;
        let re = /[a-z]+@[a-z]+\.[a-z]+/;
        if (re.test(email)){
            document.getElementById('email').setAttribute('class', '')
        }
        else{
            document.getElementById('email').setAttribute('class', 'error')
        }
    }
}