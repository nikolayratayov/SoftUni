async function viewposts(){
    let response = await fetch(`http://localhost:3030/jsonstore/blog/comments`);
    let data = await response.json();

    post_id = document.getElementById('posts').value;
    let response_title = await fetch(`http://localhost:3030/jsonstore/blog/posts/${post_id}`);
    let data_title = await response_title.json();

    document.getElementById('post-title').innerHTML = data_title.title;
    document.getElementById('post-body').innerHTML = data_title.body;

    document.getElementById('post-comments').innerHTML = '';
    for (let i in data){
        if (data[i]['postId'] == post_id){
            let li = document.createElement('li');
            li.id = data[i]['id'];
            li.innerHTML = data[i]['text'];
            document.getElementById('post-comments').appendChild(li);
        }
    }
}


async function loadposts (){
    let response_ = await fetch('http://localhost:3030/jsonstore/blog/posts');
    let data_ = await response_.json();

    document.getElementById('posts').innerHTML = '';

    for (let i in data_){
        let option = document.createElement('option');
        option.value = i;
        option.innerHTML = data_[i]['title'];

        document.getElementById('posts').appendChild(option);
    }

    let response = await fetch(`http://localhost:3030/jsonstore/blog/comments`);
    let data = await response.json();

    post_id = document.getElementById('posts').value;
    let response_title = await fetch(`http://localhost:3030/jsonstore/blog/posts/${post_id}`);
    let data_title = await response_title.json();

    document.getElementById('post-title').innerHTML = data_title.title;
    document.getElementById('post-body').innerHTML = data_title.body;

    document.getElementById('post-comments').innerHTML = '';
    for (let i in data){
        if (data[i]['postId'] == post_id){
            let li = document.createElement('li');
            li.id = data[i]['id'];
            li.innerHTML = data[i]['text'];
            document.getElementById('post-comments').appendChild(li);
        }
    }

}


function attachEvents() {
    document.getElementById('btnLoadPosts').addEventListener('click', loadposts)
    document.getElementById('btnViewPost').addEventListener('click', viewposts)
}
attachEvents();