function attachEventsListeners() {
    document.getElementById('daysBtn').addEventListener('click', daysbtn);
    document.getElementById('hoursBtn').addEventListener('click', hoursbtn);
    document.getElementById('minutesBtn').addEventListener('click', minutesbtn);
    document.getElementById('secondsBtn').addEventListener('click', secondsbtn);

    function daysbtn(){
        let days = parseFloat(document.getElementById('days').value);
        let hours = days * 24;
        let minutes = hours * 60;
        let seconds = minutes * 60;
        document.getElementById('hours').value = hours;
        document.getElementById('minutes').value = minutes;
        document.getElementById('seconds').value = seconds;
    }
    function hoursbtn(){
        let hours = parseFloat(document.getElementById('hours').value);
        let days = hours / 24;
        let minutes = hours * 60;
        let seconds = minutes * 60;
        document.getElementById('days').value = days;
        document.getElementById('minutes').value = minutes;
        document.getElementById('seconds').value = seconds;
    }
    function minutesbtn(){
        let minutes = parseFloat(document.getElementById('minutes').value);
        let hours = minutes / 60;
        let days = hours / 24;
        let seconds = minutes * 60;
        document.getElementById('hours').value = hours;
        document.getElementById('days').value = days;
        document.getElementById('seconds').value = seconds;
    }
    function secondsbtn(){
        let seconds = parseFloat(document.getElementById('seconds').value);
        let minutes = seconds / 60;
        let hours = minutes / 60;
        let days = hours / 24;
        document.getElementById('hours').value = hours;
        document.getElementById('minutes').value = minutes;
        document.getElementById('days').value = days;
    }
}