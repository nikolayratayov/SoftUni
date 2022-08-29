function attachGradientEvents() {
    let gradient = document.getElementById('gradient');
    gradient.addEventListener('mousemove', mousemove);
    gradient.addEventListener('mouseout', mouseout);
    let result = document.getElementById('result');
    
    function mousemove(evt){
        let pos = parseInt(evt.offsetX / evt.target.clientWidth * 100);
        result.innerHTML = `${pos}%`;
    }

    function mouseout(){
        result.innerHTML = '';
    }
}