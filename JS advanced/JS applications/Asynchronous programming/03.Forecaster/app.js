async function go(){

    function get_symbol(cond){
        if (cond == 'Sunny'){return '&#x2600'}
        else if (cond == 'Partly sunny'){return '&#x26C5'}
        else if (cond == 'Overcast'){return '&#x2601'}
        else if (cond == 'Rain'){return '&#x2614'}
    }

    try{
        let response = await fetch('http://localhost:3030/jsonstore/forecaster/locations');
        let data = await response.json();
        
        let target = document.getElementById('location').value;

    for (let i of data){
        if (i.name == target){
            try{
                
                let responseWeather = await fetch(`http://localhost:3030/jsonstore/forecaster/today/${i.code}`);
                let dataWeather = await responseWeather.json();
                
                let response3dyas = await fetch(`http://localhost:3030/jsonstore/forecaster/upcoming/${i.code}`);
                let data3days = await response3dyas.json();
                
                document.getElementById('forecast').setAttribute('style', 'display:block');

                let span_location = document.createElement('span');
                span_location.className = 'forecast-data';
                span_location.innerHTML = dataWeather.name;
                
                let span_temp = document.createElement('span');
                span_temp.className = 'forecast-data';
                span_temp.innerHTML = `${dataWeather.forecast.low}&#176/${dataWeather.forecast.high}&#176`;

                let span_condition = document.createElement('span');
                span_condition.className = 'forecast-data';
                span_condition.innerHTML = dataWeather.forecast.condition;
                
                let span_for_3spans = document.createElement('span');
                span_for_3spans.className = 'condition';
                span_for_3spans.appendChild(span_location);
                span_for_3spans.appendChild(span_temp);
                span_for_3spans.appendChild(span_condition);

                let span_symbol = document.createElement('span');
                span_symbol.className = 'condition symbol';
                let symbol = get_symbol(dataWeather.forecast.condition)
                span_symbol.innerHTML = symbol

                let div = document.createElement('div');
                div.className = 'forecasts';
                div.appendChild(span_symbol);
                div.appendChild(span_for_3spans);

                document.getElementById('current').appendChild(div);

                let div_upcoming = document.createElement('div');
                div_upcoming.className = 'forecast-info';

                for (let i of data3days.forecast){
                    let span_symbol_up = document.createElement('span');
                    span_symbol_up.className = 'symbol';
                    span_symbol_up.innerHTML = get_symbol(i.condition);

                    let span_temp_up = document.createElement('span');
                    span_temp_up.className = 'forecast-data';
                    span_temp_up.innerHTML = `${i.low}&#176/${i.high}&#176`;

                    let span_cond_up = document.createElement('span');
                    span_cond_up.className = 'forecast-data';
                    span_cond_up.innerHTML = i.condition;

                    let span_to_append = document.createElement('span');
                    span_to_append.className = 'upcoming';
                    span_to_append.appendChild(span_symbol_up);
                    span_to_append.appendChild(span_temp_up);
                    span_to_append.appendChild(span_cond_up);

                    div_upcoming.appendChild(span_to_append);
                }

                document.getElementById('upcoming').appendChild(div_upcoming);

            }
            catch(e){
                document.getElementById('forecast').setAttribute('style', 'display:block')
                document.getElementById('forecast').innerHTML = 'Error';
            }
        }
    }
    }
    catch(e){
        document.getElementById('forecast').setAttribute('style', 'display:block')
        document.getElementById('forecast').innerHTML = 'Error';
    }
}

function attachEvents() {
    document.getElementById('submit').addEventListener('click', go)
}
attachEvents();