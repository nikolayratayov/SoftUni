function solve(a){
    let cars = {};
    for (let i of a){
        let [brand, model, nums] = i.split(' | ');
        if (brand in cars){
            if (model in cars[brand]){
                cars[brand][model] += Number(nums);
            }
            else{
                cars[brand][model] = Number(nums);
            }
            }
        else{
            cars[brand] = {};
            cars[brand][model] = Number(nums);
        }
    }
    for (let key in cars){
        console.log(key)
        for ( let i in cars[key]){
            console.log(`###${i} -> ${cars[key][i]}`)
        }
    }
}
