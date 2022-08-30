function validate() {
    let email = document.getElementById('email');
    email.addEventListener('change', func);

    function func(){
        let email_content = document.getElementById('email').value;
        let re = /[a-z]+@[a-z]+\.[a-z]+/;
        let match = email_content.match(re);
        if (email_content == match){
            document.getElementById('email').classList.remove('error');
        }
        else{
            document.getElementById('email').classList.add('error');
        }
    }
}