function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let rows = document.getElementsByTagName('tr');
      for(let i = 2; i < rows.length; i++){
         document.getElementsByTagName('tr')[i].classList.remove('select');
      }
      let search_text = document.getElementById('searchField').value;
      document.getElementById('searchField').value = '';
      if (search_text.length > 0){
         for(let i = 2; i < rows.length; i++){
            let cells = rows[i].getElementsByTagName('td').length;
            for (let j = 0; j < cells; j++){
               if ((rows[i].getElementsByTagName('td')[j].innerHTML).includes(search_text)){
                  document.getElementsByTagName('tr')[i].classList.add('select')
                  break;
               }
            }
         }
      }
   }
}