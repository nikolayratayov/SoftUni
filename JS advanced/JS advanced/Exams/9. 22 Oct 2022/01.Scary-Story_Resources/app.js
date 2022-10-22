window.addEventListener("load", solve);

function solve() {
  document.getElementById('form-btn').addEventListener('click', (evt) => evt.preventDefault())
  document.getElementById('form-btn').addEventListener('click', publish)

  function publish(){
    let first = document.getElementById('first-name').value;
    let last = document.getElementById('last-name').value;
    let age = document.getElementById('age').value;
    let title = document.getElementById('story-title').value;
    let genre = document.getElementById('genre').value;
    let story = document.getElementById('story').value;

    if (first && last && age && title && genre && story){
      document.getElementById('form-btn').disabled = true;
      document.getElementById('first-name').value = '';
      document.getElementById('last-name').value = '';
      document.getElementById('age').value = '';
      document.getElementById('story-title').value = ''
      document.getElementById('genre').value = '';
      document.getElementById('story').value = '';

      let h4 = document.createElement('h4');
      h4.innerHTML = 'Name: ' + first + ' ' + last;

      let p_age = document.createElement('p');
      p_age.innerHTML = 'Age: ' + age;

      let p_title = document.createElement('p');
      p_title.innerHTML = 'Title: ' + title;

      let p_genre = document.createElement('p');
      p_genre.innerHTML = 'Genre: ' + genre;

      let p_story = document.createElement('p');
      p_story.innerHTML = story;

      let article = document.createElement('article');
      article.appendChild(h4)
      article.appendChild(p_age)
      article.appendChild(p_title)
      article.appendChild(p_genre)
      article.appendChild(p_story)

      let btn_save = document.createElement('button');
      btn_save.className = 'save-btn';
      btn_save.innerHTML = 'Save Story';
      btn_save.addEventListener('click', save)

      let btn_edit = document.createElement('button');
      btn_edit.className = 'edit-btn';
      btn_edit.innerHTML = 'Edit Story';
      btn_edit.addEventListener('click', edit);

      let btn_delete = document.createElement('button');
      btn_delete.className = 'delete-btn';
      btn_delete.innerHTML = 'Delete Story';
      btn_delete.addEventListener('click', delete_story);

      let li = document.createElement('li');
      li.className = 'story-info';

      li.appendChild(article)
      li.appendChild(btn_save)
      li.appendChild(btn_edit)
      li.appendChild(btn_delete)

      document.getElementById('preview-list').appendChild(li);
    }
  }

  function save(){
    document.getElementById('main').innerHTML = '';
    let h1 = document.createElement('h1');
    h1.innerHTML = 'Your scary story is saved!'
    document.getElementById('main').appendChild(h1);
  }

  function edit(evt){
    document.getElementById('form-btn').disabled = false;

    let names = evt.currentTarget.parentElement.getElementsByTagName('article')[0].getElementsByTagName('h4')[0].innerHTML.substring(6);
    let [first, last] = names.split(' ');
    let age = Number(evt.currentTarget.parentElement.getElementsByTagName('article')[0].getElementsByTagName('p')[0].innerHTML.substring(5));
    let title = evt.currentTarget.parentElement.getElementsByTagName('article')[0].getElementsByTagName('p')[1].innerHTML.substring(7);
    let genre = evt.currentTarget.parentElement.getElementsByTagName('article')[0].getElementsByTagName('p')[2].innerHTML.substring(7);
    let story = evt.currentTarget.parentElement.getElementsByTagName('article')[0].getElementsByTagName('p')[3].innerHTML;

    evt.currentTarget.parentElement.remove();

    document.getElementById('first-name').value = first;
    document.getElementById('last-name').value = last;
    document.getElementById('age').value = age;
    document.getElementById('story-title').value = title;
    document.getElementById('genre').value = genre;
    document.getElementById('story').value = story;

  }

  function delete_story(evt){
    evt.currentTarget.parentElement.remove();
    document.getElementById('form-btn').disabled = false;
  }
}
