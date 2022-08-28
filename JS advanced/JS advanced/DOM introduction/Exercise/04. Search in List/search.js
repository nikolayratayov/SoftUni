function search() {
   let towns = document.getElementsByTagName('li').length;
   for(let i = 0; i < towns; i++){
      document.getElementsByTagName('li')[i].setAttribute('style', 'font-weight:normal; font-style:normal');
   }
   let search_value = document.getElementById('searchText').value;
   let res = 0;
   for(let i = 0; i < towns; i++){
      let text_inner = document.getElementsByTagName('li')[i].innerHTML;
      if (text_inner.includes(search_value)){
         res += 1;
         document.getElementsByTagName('li')[i].setAttribute('style', 'font-weight:bold; font-style:italic');
      }
   }
   document.getElementById('result').innerHTML = `${res} matches found`
}