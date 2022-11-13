function validate() {
    function checkbox(){
        let chk = document.getElementById('company').checked;
        if(chk){
            document.getElementById('companyInfo').setAttribute('style', 'display: block');
        }
        else{
            document.getElementById('companyInfo').setAttribute('style', 'display: none');
        }
    }
    document.getElementById('company').addEventListener('change', checkbox)

    document.getElementById('submit').addEventListener('click', function(event){event.preventDefault()})
    document.getElementById('submit').addEventListener('click', submit)
    function submit(){
        let username = document.getElementById('username').value;
        let username_re = /^[A-Za-z0-9]+$/;
        let username_check = username_re.test(username) && username.length > 2 && username.length < 21;
        if (username_check){
            document.getElementById('username').setAttribute('style', 'border: none')
        }
        else{
            document.getElementById('username').setAttribute('style', 'border-color: red')
        }

        let email = document.getElementById('email').value;
        let email_re = /@+.*\./;
        let email_check = email_re.test(email);
        if (email_check){
            document.getElementById('email').setAttribute('style', 'border: none')
        }
        else{
            document.getElementById('email').setAttribute('style', 'border-color: red')
        }

        let password1 = document.getElementById('password').value;
        let password1_re = /^[A-Za-z0-9_]+$/;
        let password1_check = password1_re.test(password1) && password1.length > 4 && password1.length < 16;
        if (password1_check){
            document.getElementById('password').setAttribute('style', 'border: none')
        }
        else{
            document.getElementById('password').setAttribute('style', 'border-color: red')
        }

        let password2 = document.getElementById('confirm-password').value;
        let password2_check = password1_re.test(password2) && password2.length > 4 && password2.length < 16;
        if (password2_check){
            document.getElementById('confirm-password').setAttribute('style', 'border: none')
        }
        else{
            document.getElementById('confirm-password').setAttribute('style', 'border-color: red')
        }

        if (password1 !== password2){
            document.getElementById('password').setAttribute('style', 'border-color: red')
            document.getElementById('confirm-password').setAttribute('style', 'border-color: red')
        }

        let company_number = document.getElementById('companyNumber').value;
        let company_number_check = company_number >= 1000 && company_number <= 9999;
        if (company_number_check && document.getElementById('company').checked){
            document.getElementById('companyNumber').setAttribute('style', 'border: none')
        }
        else if (document.getElementById('company').checked){
            document.getElementById('companyNumber').setAttribute('style', 'border-color: red')
        }
        
        if (document.getElementById('company').checked){
            if (!username_check || !email_check || !password1_check || !password2_check || !company_number_check){
                document.getElementById('valid').setAttribute('style', 'display: none');
            }
            else{
                document.getElementById('valid').setAttribute('style', 'display: inline');
            }
        }
        else{
            if (!username_check || !email_check || !password1_check || !password2_check){
                document.getElementById('valid').setAttribute('style', 'display: none');
            }
            else{
                document.getElementById('valid').setAttribute('style', 'display: inline');
            }
        }
    }
}
