function notify(message) {
  function hide(){
    document.getElementById('notification').setAttribute('style', 'display: none');
  }
    document.getElementById('notification').innerHTML = message;
    document.getElementById('notification').setAttribute('style', 'display: block');
    document.getElementById('notification').addEventListener('click', hide);
    
}