function colorize() {
    let rows = document.getElementsByTagName('tr');
    for (let row = 0; row < rows.length; row++){
        if (row % 2 != 0){
            document.getElementsByTagName('tr')[row].setAttribute('style', 'background-color: teal');
        }   
    }
}