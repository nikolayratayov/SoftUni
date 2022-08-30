function create(words) {
   function displayp(evt){
      evt.target.firstElementChild.style = 'display:inline';
   }
   let div_to_append = document.getElementById('content');
   for (let word of words){
      let div = document.createElement('div');
      let p = document.createElement('p');
      p.setAttribute('style', 'display:none');
      p.innerHTML = word;
      div.addEventListener('click', displayp);
      div.appendChild(p);
      div_to_append.appendChild(div);
   }
}