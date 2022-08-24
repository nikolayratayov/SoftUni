function solve(input){
    arr = [];
    for(const iterator of input){
        let check = false;
        let [town, product, price] = iterator.split(' | ');
        price = Number(price);
        for(let i = 0; i < arr.length; i++){
            if ( product == arr[i]['produkt']){
                if (price < arr[i]['cena']){
                    arr[i]['cena'] = price;
                    arr[i]['grad'] = town;
                }
                check = true;
            }
        }
        if (!check){
            let eee = {};
            eee['produkt'] = product;
            eee['cena'] = price;
            eee['grad'] = town;
            arr.push(eee);
        }
    }
    for (const iterator of arr){
        console.log(`${iterator['produkt']} -> ${iterator['cena']} (${iterator['grad']})`)
    }
}