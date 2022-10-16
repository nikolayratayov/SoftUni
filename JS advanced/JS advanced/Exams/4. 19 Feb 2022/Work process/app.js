function solve() {

    function fired(evt){
        let salary = Number(evt.currentTarget.parentElement.parentElement.getElementsByTagName('td')[5].innerHTML);
        let budget = Number(document.getElementById('sum').innerHTML);
        budget = (budget - salary).toFixed(2);
        document.getElementById('sum').innerHTML = budget;
        evt.currentTarget.parentElement.parentElement.remove();
    }

    function edit(evt){
        let fname = evt.currentTarget.parentElement.parentElement.getElementsByTagName('td')[0].innerHTML;
        let lname = evt.currentTarget.parentElement.parentElement.getElementsByTagName('td')[1].innerHTML;
        let email = evt.currentTarget.parentElement.parentElement.getElementsByTagName('td')[2].innerHTML;
        let birht = evt.currentTarget.parentElement.parentElement.getElementsByTagName('td')[3].innerHTML;
        let position = evt.currentTarget.parentElement.parentElement.getElementsByTagName('td')[4].innerHTML;
        let salary = Number(evt.currentTarget.parentElement.parentElement.getElementsByTagName('td')[5].innerHTML);
        fired(evt);

        document.getElementById('fname').value = fname;
        document.getElementById('lname').value = lname;
        document.getElementById('email').value = email;
        document.getElementById('birth').value = birht;
        document.getElementById('position').value = position;
        document.getElementById('salary').value = salary;
        
    }

    document.getElementById('add-worker').addEventListener('click', (evt) => evt.preventDefault());
    document.getElementById('add-worker').addEventListener('click', add);

    function add(){
        let firstName = document.getElementById('fname').value;
        let td_fname = document.createElement('td');
        td_fname.innerHTML = firstName;
        
        let lastName = document.getElementById('lname').value;
        let td_lname = document.createElement('td');
        td_lname.innerHTML = lastName;

        let email = document.getElementById('email').value;
        let td_email = document.createElement('td');
        td_email.innerHTML = email;

        let birth = document.getElementById('birth').value;
        let td_birth = document.createElement('td');
        td_birth.innerHTML = birth;

        let position = document.getElementById('position').value;
        let td_position = document.createElement('td');
        td_position.innerHTML = position;

        let salary = Number(document.getElementById('salary').value);
        let td_salary = document.createElement('td');
        td_salary.innerHTML = salary;
        
        if (firstName && lastName && email && birth && position && salary){
            document.getElementById('fname').value = '';
            document.getElementById('lname').value = '';
            document.getElementById('email').value = '';
            document.getElementById('birth').value = '';
            document.getElementById('position').value = '';
            document.getElementById('salary').value = '';

            let budget = Number(document.getElementById('sum').innerHTML);
            let new_budjet = (budget + salary).toFixed(2);
            document.getElementById('sum').innerHTML = new_budjet;

            let btn_fired = document.createElement('button');
            btn_fired.className = 'fired';
            btn_fired.innerHTML = 'Fired';
            btn_fired.addEventListener('click', fired);

            let btn_edit = document.createElement('button');
            btn_edit.className = 'edit';
            btn_edit.innerHTML = 'Edit';
            btn_edit.addEventListener('click', edit);

            let td_buttons = document.createElement('td');
            td_buttons.appendChild(btn_fired)
            td_buttons.appendChild(btn_edit)


            let new_tr = document.createElement('tr');
            new_tr.appendChild(td_fname)
            new_tr.appendChild(td_lname)
            new_tr.appendChild(td_email)
            new_tr.appendChild(td_birth)
            new_tr.appendChild(td_position)
            new_tr.appendChild(td_salary)
            new_tr.appendChild(td_buttons)

            document.getElementById('tbody').appendChild(new_tr);
        }
    }
}
solve()