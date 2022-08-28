function solve() {
    let text = document.getElementById('text').value;
    let type = document.getElementById('naming-convention').value;
    text = text.toLowerCase();
    let arr = text.split(' ');
    let new_arr = [];
    if ( type == 'Camel Case'){
      new_arr.push(arr[0]);
      for (let i = 1; i < arr.length; i++){
        let first = arr[i].slice(0, 1);
        first = first.toUpperCase();
        let word = first + arr[i].slice(1);
        new_arr.push(word);
      }
    }
    else if (type == 'Pascal Case'){
      for (let i = 0; i < arr.length; i++){
        let first = arr[i].slice(0, 1);
        first = first.toUpperCase();
        let word = first + arr[i].slice(1);
        new_arr.push(word);
      }
    }
    else{
      new_arr.push('Error!');
    }
    document.getElementById('result').innerHTML = new_arr.join('');
}