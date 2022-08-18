function solve(arr){
    arr.sort(function(a, b){
        var nameA = a.toLowerCase(), nameB = b.toLowerCase();
        if (nameA < nameB)
         return -1;
        if (nameA > nameB)
         return 1;
        return 0;
       });
    for (let i = 0; i < arr.length; i++){
        console.log(`${i + 1}.${arr[i]}`)
    }
}