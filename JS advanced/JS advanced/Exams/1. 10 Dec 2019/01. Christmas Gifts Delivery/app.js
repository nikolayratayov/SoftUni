function solution() {
    function mydiscard(evt){
        let name_to_cut = evt.currentTarget.parentElement.innerText;
        let name = name_to_cut.substring(0, name_to_cut.length - 11)
        let new_item = document.createElement('li');
        new_item.innerHTML = name;
        new_item.className = 'gift';
        document.getElementsByTagName('ul')[2].appendChild(new_item);
        evt.currentTarget.parentElement.remove();
    }
    function mysend(evt){
        let name_to_cut = evt.currentTarget.parentElement.innerText;
        let name = name_to_cut.substring(0, name_to_cut.length - 11)
        let new_item = document.createElement('li');
        new_item.innerHTML = name;
        new_item.className = 'gift';
        document.getElementsByTagName('ul')[1].appendChild(new_item);
        evt.currentTarget.parentElement.remove();
    }

    function add(){
        let item_name = document.getElementsByTagName('input')[0].value;
        document.getElementsByTagName('input')[0].value = '';
        let list_item = document.createElement('li');
        list_item.innerHTML = item_name;
        list_item.className = 'gift';
        let but = document.createElement('button');
        but.innerHTML = 'Send';
        but.setAttribute('id', 'sendButton')
        but.addEventListener('click', mysend);
        let discard = document.createElement('button');
        discard.innerHTML = 'Discard';
        discard.setAttribute('id', 'discardButton')
        discard.addEventListener('click', mydiscard)
        list_item.appendChild(but);
        list_item.appendChild(discard);
        document.getElementsByTagName('ul')[0].appendChild(list_item);

        let li_els = document.getElementsByTagName('ul')[0].getElementsByTagName('li');
        let sorted_li_els = Array.from(li_els).sort((a, b) => a.innerHTML.localeCompare(b.innerHTML));
        document.getElementsByTagName('ul')[0].innerHTML = '';

        for (let i of sorted_li_els){
            document.getElementsByTagName('ul')[0].appendChild(i);
        }
    }
    document.getElementsByTagName('button')[0].addEventListener('click', add)
}