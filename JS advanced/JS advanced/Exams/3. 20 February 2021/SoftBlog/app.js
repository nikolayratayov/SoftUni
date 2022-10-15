function solve(){
   function delete_post(evt){
      evt.currentTarget.parentElement.parentElement.remove();
   }
   function archive(evt){
      let li = document.createElement('li');
      li.innerHTML = evt.currentTarget.parentElement.parentElement.getElementsByTagName('h1')[0].innerHTML;
      let li_array = document.getElementsByTagName('ol')[0].getElementsByTagName('li');
      document.getElementsByTagName('ol')[0].appendChild(li);

      let sorted_li_els = Array.from(li_array).sort((a, b) => a.innerHTML.localeCompare(b.innerHTML));
      document.getElementsByTagName('ol')[0].innerHTML = '';

      for (let i of sorted_li_els){
         document.getElementsByTagName('ol')[0].appendChild(i);
      }
      evt.currentTarget.parentElement.parentElement.remove();
   }

   document.getElementsByClassName('btn create')[0].addEventListener('click', create);
   document.getElementsByClassName('btn create')[0].addEventListener('click', (evt) => evt.preventDefault());

   function create(){
      let h1 = document.createElement('h1');
      h1.innerHTML = document.getElementById('title').value;

      let ptag_category = document.createElement('p');
      ptag_category.innerHTML = 'Category:'
      let str_ptag = document.createElement('strong');
      str_ptag.innerHTML = document.getElementById('category').value;
      ptag_category.appendChild(str_ptag);

      let ptag_creator = document.createElement('p');
      ptag_creator.innerHTML = 'Creator:'
      let str = document.createElement('strong');
      str.innerHTML = document.getElementById('creator').value;
      ptag_creator.appendChild(str);

      let ptag_content = document.createElement('p');
      ptag_content.innerHTML = document.getElementById('content').value;

      let div = document.createElement('div');
      div.className = 'buttons';
      let btn_delete = document.createElement('button');
      btn_delete.className = 'btn delete';
      btn_delete.innerHTML = 'Delete';
      btn_delete.addEventListener('click', delete_post);
      let btn_archive = document.createElement('button');
      btn_archive.className = 'btn archive';
      btn_archive.innerHTML = 'Archive';
      btn_archive.addEventListener('click', archive);
      div.appendChild(btn_delete);
      div.appendChild(btn_archive);

      let article = document.createElement('article');
      article.appendChild(h1);
      article.appendChild(ptag_category);
      article.appendChild(ptag_creator);
      article.appendChild(ptag_content);
      article.appendChild(div);

      document.getElementsByTagName('section')[1].appendChild(article);
   }
}
