function factory(library, orders){
    arr = new Array;
    for(let i = 0; i < orders.length; i++){
        let copied = {...orders[i].template};
        for(let j = 0; j < orders[i].parts.length; j++){
            let method = orders[i].parts[j];
            copied[method] = library[method];
        }
        arr.push(copied);
    }
    return arr
}