function solve(steps, length_of_footprint, speed){
    let distance = steps * length_of_footprint;
    let time = distance / 1000 / speed;
    let hours = parseInt(time);
    let hours_left = time - hours;
    let minutes = parseInt(hours_left * 60);
    let minutes_left = hours_left * 60 - minutes;
    let seconds = Math.round(minutes_left * 60);
    let add_time = parseInt(distance / 500);
    hours_str = '';
    minutes_str = '';
    seconds_str = '';
    minutes += add_time
    if (hours >= 0 && hours <= 9){
        hours_str += '0' + hours;
    }
    else{
        hours_str += hours;
    }
    if (minutes >= 0 && minutes <= 9){
        minutes_str += '0' + minutes;
    }
    else{
        minutes_str += minutes;
    }    
    if (seconds >= 0 && seconds <= 9){
        seconds_str += '0' + seconds;
    }
    else{
        seconds_str += seconds;
    }
    console.log(`${hours_str}:${minutes_str}:${seconds_str}`);
}