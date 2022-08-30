function focused() {
    let divs = document.getElementsByTagName('div')[0].getElementsByTagName('div');
    for (let i = 0; i < divs.length; i++){
        divs[i].addEventListener('focus', mousemove);
        divs[i].addEventListener('blur', mouseout);
    }


    function mousemove(evt){
        evt.currentTarget.classList.add('focused');
    }
    function mouseout(evt){
        evt.currentTarget.classList.remove('focused');
    }
}