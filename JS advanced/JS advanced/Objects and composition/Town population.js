function solve(a){
    const population = new Object;
    for (let i = 0; i < a.length; i++){
        let name_pop_arr = a[i].split(' <-> ');
        let name = name_pop_arr[0];
        let popul = parseInt(name_pop_arr[1]);
        if (name in population){
            population[name] += popul
        }
        else{
            population[name] = popul
        }
    }
    for (const key in population){
        console.log(`${key} : ${population[key]}`)
    }
}