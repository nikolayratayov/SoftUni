function toggle() {
    let button = document.getElementsByClassName('button')[0].innerHTML;
    if (button == 'More'){
        document.getElementsByClassName('button')[0].innerHTML = 'Less';
        document.getElementById('extra').setAttribute('style', 'display:block');
    }
    else{
        document.getElementsByClassName('button')[0].innerHTML = 'More';
        document.getElementById('extra').setAttribute('style', 'display:none');
    }
}