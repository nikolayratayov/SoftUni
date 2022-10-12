function solve(a){
    let juices = {};
    let bottles = {};
    for (let i of a){
        let [juice, quantity] = i.split(' => ')
        quantity = Number(quantity);
        if (juice in juices){ juices[juice] += quantity}
        else{juices[juice] = quantity}
        if (juices[juice] >= 1000){
            let left_juice = juices[juice] % 1000;
            let new_bottles = parseInt(juices[juice] / 1000);
            juices[juice] = left_juice;
            if (juice in bottles){bottles[juice] += new_bottles}
            else{bottles[juice] = new_bottles}
        }
    }
    for (let key in bottles){
        console.log(`${key} => ${bottles[key]}`)
    }
}
