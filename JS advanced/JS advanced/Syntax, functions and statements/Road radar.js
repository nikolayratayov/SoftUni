function solve(a, b){
    let limit;
    let overspeed;
    let status;
    switch (b){
        case 'motorway':
            limit = 130;
            break;
        case 'interstate':
            limit = 90;
            break;
        case 'city':
            limit = 50;
            break;
        case 'residential':
            limit = 20;
            break;
    }
    if (a <= limit){
        console.log(`Driving ${a} km/h in a ${limit} zone`)
    }
    else{
        overspeed = a - limit;
            if (overspeed <= 20){
                status = 'speeding';
            }
            else if (overspeed <= 40){
                status = 'excessive speeding';
            }
            else{
                status = 'reckless driving';
            }
            console.log(`The speed is ${overspeed} km/h faster than the allowed speed of ${limit} - ${status}`)
        }
}