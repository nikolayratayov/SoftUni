function lockedProfile() {
    function showhide(evt){
        if (evt.target.innerHTML == 'Show more' && evt.target.parentElement.getElementsByTagName('input')[1].checked){
            evt.target.parentElement.getElementsByTagName('div')[0].style = 'display: inline';
            evt.target.innerHTML = 'Hide it';
        }
        else if (evt.target.innerHTML == 'Hide it' && evt.target.parentElement.getElementsByTagName('input')[1].checked){
            evt.target.parentElement.getElementsByTagName('div')[0].style = 'display: none';
            evt.target.innerHTML = 'Show more';
        }
    }

    let btns = document.getElementsByTagName('button');
    for (let i = 0; i < btns.length; i++){
        btns[i].addEventListener('click', showhide)
    }

}