function solve(arr){
    let heroes = [];
    for(let i = 0; i < arr.length; i++){
        name_level_items = arr[i].split(' / ');
        hero = name_level_items[0];
        if (name_level_items.length > 1){
            level = parseFloat(name_level_items[1]);
        }
        else{level = ''}
        if (name_level_items.length > 2){
            items = name_level_items[2].split(', ');
        }
        else{items = []}
        obj = {
            name: hero,
            level: level,
            items: items
        };
        heroes.push(obj);
    }
    let output = JSON.stringify(heroes);
    console.log(output);
}