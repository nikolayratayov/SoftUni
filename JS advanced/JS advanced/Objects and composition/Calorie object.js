function solve(arr){
    obj = new Object;
    for (let i = 0; i< arr.length; i++){
        if(i % 2 == 0){
            let ime = arr[i];
            obj[ime] = 0;
    }
    }
    for (let i = 0; i< arr.length; i++){
        if(i % 2 != 0){
            let prop = parseInt(arr[i]);
            obj[arr[i - 1]] += prop;
    }
    
    }
    console.log(obj);
}