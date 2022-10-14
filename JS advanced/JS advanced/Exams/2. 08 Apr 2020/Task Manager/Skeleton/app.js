function solve() {
    let button = document.getElementById('add');
    button.addEventListener('click', add);
    button.addEventListener('click', function(event){event.preventDefault()});

    function delete_art(evt){
        evt.currentTarget.parentElement.parentElement.remove();
    }

    function finish(evt){
        let art = evt.currentTarget.parentElement.parentElement;
        art.getElementsByTagName('div')[0].remove();
        document.getElementsByTagName('section')[3].getElementsByTagName('div')[1].appendChild(art);
    }

    function start(evt){
        let art = evt.currentTarget.parentElement.parentElement;
        art.getElementsByTagName('div')[0].getElementsByTagName('button')[0].className = 'red';
        art.getElementsByTagName('div')[0].getElementsByTagName('button')[0].innerHTML = 'Delete';
        art.getElementsByTagName('div')[0].getElementsByTagName('button')[0].addEventListener('click', delete_art);
        art.getElementsByTagName('div')[0].getElementsByTagName('button')[1].className = 'orange';
        art.getElementsByTagName('div')[0].getElementsByTagName('button')[1].innerHTML = 'Finish';
        art.getElementsByTagName('div')[0].getElementsByTagName('button')[1].addEventListener('click', finish)
        document.getElementsByTagName('section')[2].getElementsByTagName('div')[1].appendChild(art);
    }

    function add(){
        let task = document.getElementById('task').value;
        let description = document.getElementById('description').value;
        let date = document.getElementById('date').value;
        if (!task || !description || !date){return}
        
        let btn_green = document.createElement('button');
        btn_green.className = 'green';
        btn_green.innerHTML = 'Start';
        btn_green.addEventListener('click', start)

        let btn_red = document.createElement('button');
        btn_red.className = 'red';
        btn_red.innerHTML = 'Delete';
        btn_red.addEventListener('click', delete_art)

        let div = document.createElement('div');
        div.className = 'flex';
        div.appendChild(btn_green);
        div.appendChild(btn_red);
        let h3 = document.createElement('h3');
        h3.innerHTML = task;
        let p_desc = document.createElement('p');
        p_desc.innerHTML = 'Description: ' + description;
        let p_date = document.createElement('p');
        p_date.innerHTML = 'Due Date: ' + date;

        let article = document.createElement('article');
        article.appendChild(h3);
        article.appendChild(p_desc);
        article.appendChild(p_date);
        article.appendChild(div);
        
        let div_to_append = document.getElementsByTagName('section')[1].getElementsByTagName('div')[1];
        div_to_append.appendChild(article);

    }
}