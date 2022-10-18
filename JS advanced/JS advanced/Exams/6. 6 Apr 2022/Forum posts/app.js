window.addEventListener("load", solve);

function solve() {
    document.getElementById('publish-btn').addEventListener('click', (evt) => evt.preventDefault())
    document.getElementById('publish-btn').addEventListener('click', add)

    document.getElementById('clear-btn').addEventListener('click', clear)

    function add(){
        let title = document.getElementById('post-title').value;
        let category = document.getElementById('post-category').value;
        let content = document.getElementById('post-content').value;

        if (title && category && content){
          document.getElementById('post-title').value = '';
          document.getElementById('post-category').value = '';
          document.getElementById('post-content').value = '';

          let h4 = document.createElement('h4');
          h4.innerHTML = title;

          let p_category = document.createElement('p');
          p_category.innerHTML = 'Category: ' + category;

          let p_content = document.createElement('p');
          p_content.innerHTML = 'Content: ' + content;

          let article = document.createElement('article');
          article.appendChild(h4)
          article.appendChild(p_category)
          article.appendChild(p_content)

          let btn_edit = document.createElement('button');
          btn_edit.className = 'action-btn edit';
          btn_edit.innerHTML = 'Edit';
          btn_edit.addEventListener('click', edit);

          let btn_approve = document.createElement('button');
          btn_approve.className = 'action-btn approve';
          btn_approve.innerHTML = 'Approve';
          btn_approve.addEventListener('click', approve)

          let li = document.createElement('li');
          li.className = 'rpost';
          li.appendChild(article)
          li.appendChild(btn_edit)
          li.appendChild(btn_approve)

          document.getElementById('review-list').appendChild(li);
        }
    }

    function edit(evt){
      document.getElementById('post-title').value = document.getElementById('review-list').getElementsByTagName('h4')[0].innerHTML;
      document.getElementById('post-category').value = document.getElementById('review-list').getElementsByTagName('p')[0].innerHTML.substring(10)
      document.getElementById('post-content').value = document.getElementById('review-list').getElementsByTagName('p')[1].innerHTML.substring(9)

      evt.currentTarget.parentElement.remove()
    }

    function approve(evt){
      let art = document.getElementById('review-list').getElementsByTagName('article')[0];
      let li = document.createElement('li');
      li.className = 'rpost';
      li.appendChild(art)

      document.getElementById('published-list').appendChild(li)

      evt.currentTarget.parentElement.remove();

    }

    function clear(){
      document.getElementById('published-list').innerHTML = ''
    }
}
