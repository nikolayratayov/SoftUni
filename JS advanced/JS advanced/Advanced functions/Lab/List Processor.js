function solve(a){
    let arr = a;
    let list = []
    for (let i of arr){
        let [command, str] = i.split(' ')
        if (command == 'print') {
            console.log(list.join(','))
        }
        else{
            if (command == 'add'){
                list.push(str)
            }
            else if(command == 'remove'){
                list = list.filter(function(x){return x !== str})
            }
        }
    }
}
