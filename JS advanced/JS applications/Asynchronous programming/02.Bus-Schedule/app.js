function solve() {
    let currentStop = '';
    let nextStopId = 'depot';

    async function depart() {
        try{
            document.getElementById('depart').disabled = true;
            document.getElementById('arrive').disabled = false;

            let result = await fetch(`http://localhost:3030/jsonstore/bus/schedule/${nextStopId}`);
            let data = await result.json();
            
            nextStopId = data.next
            currentStop = data.name

            document.getElementsByClassName('info')[0].innerHTML = `Next stop ${currentStop}`

            
        }
        catch(e){
            document.getElementById('depart').disabled = true;
            document.getElementById('arrive').disabled = true;
            document.getElementsByClassName('info')[0].innerHTML = `Error`
        }
        
    }

    async function arrive() {
        try{
            document.getElementsByClassName('info')[0].innerHTML = `Arriving at ${currentStop}`;
    
            document.getElementById('depart').disabled = false;
            document.getElementById('arrive').disabled = true;
        }
        catch(e){
            document.getElementById('depart').disabled = true;
            document.getElementById('arrive').disabled = true;
            document.getElementsByClassName('info')[0].innerHTML = `Error`
        }
    }

    return {
        depart,
        arrive
    };
}

let result = solve();