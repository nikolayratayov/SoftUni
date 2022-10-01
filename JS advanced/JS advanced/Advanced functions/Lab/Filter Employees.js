function solve(a, b){
    let data = JSON.parse(a);
    let criteria = b;
    if (criteria === 'all') {
        for(let i = 0; i < data.length; i++){
            console.log(`${i}. ${data[i].first_name} ${data[i].last_name} - ${data[i].email}`)
        }
    }
    else{
        let [key, crit] = criteria.split('-')
        let counter = -1
        for (let i = 0; i < data.length; i++){
            if (data[i][key] === crit){
                counter++
                console.log(`${counter}. ${data[i].first_name} ${data[i].last_name} - ${data[i].email}`)
            }
        }
    }
}   
