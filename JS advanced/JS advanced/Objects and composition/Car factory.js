function solve(a){
    car = {};
    car['model'] = a['model'];
    if (a['power'] <= 90){
        car['engine'] = {power: 90, volume: 1800}
    }
    else if (a['power'] > 90 && a['power'] <= 120){
        car['engine'] = {power: 120, volume: 2400}
    }
    else{
        car['engine'] = {power: 200, volume: 3500}
    }
    car['carriage'] = {type: a['carriage'], color: a['color']}
    let wheel = Math.floor(parseFloat(a['wheelsize']))
    if (wheel % 2 == 0){
        wheel -= 1
    }
    car['wheels'] = [wheel, wheel, wheel, wheel]
    return car;
}