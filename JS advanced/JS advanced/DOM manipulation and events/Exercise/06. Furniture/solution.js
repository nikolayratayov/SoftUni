function solve() {
    function generate(){
        let objs = JSON.parse(document.getElementsByTagName('textarea')[0].value);
        let tbody = document.getElementsByTagName('tbody')[0];
        for (const obj of objs){
            let row = document.createElement('tr');
            let img = document.createElement('img');
            img.src = obj.img;
            let tdimg = document.createElement('td');
            tdimg.appendChild(img);
            row.appendChild(tdimg);
            let pname = document.createElement('p');
            pname.innerHTML = obj.name;
            let tdname = document.createElement('td');
            tdname.appendChild(pname);
            row.appendChild(tdname);
            let pprice = document.createElement('p');
            pprice.innerHTML = obj.price;
            let tdprice = document.createElement('td');
            tdprice.appendChild(pprice);
            row.appendChild(tdprice);
            let pfactor = document.createElement('p');
            pfactor.innerHTML = obj.decFactor;
            let tdfactor = document.createElement('td');
            tdfactor.appendChild(pfactor);
            row.appendChild(tdfactor);
            let input = document.createElement('input');
            input.type = 'checkbox';
            let tdinput = document.createElement('td');
            tdinput.appendChild(input);
            row.appendChild(tdinput);
            tbody.appendChild(row);
        }
    }

    function buy(){
        let inputs = document.getElementsByTagName('input');
        let rows = document.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
        let arr_names = [];
        let price = 0;
        let arr_dec = [];
        for (let i = 1; i < inputs.length; i++){
            if(inputs[i].checked){
                let ptags = rows[i].getElementsByTagName('p');
                arr_names.push(ptags[0].innerHTML);
                price += parseFloat(ptags[1].innerHTML);
                arr_dec.push(parseFloat(ptags[2].innerHTML));
            }
        }
        let output = '';
        let sum_fac = arr_dec.reduce((partialSum, a) => partialSum + a, 0);
        let res_fac = sum_fac / arr_dec.length;
        output += `Bought furniture: ${arr_names.join(', ')}\nTotal price: ${price.toFixed(2)}\nAverage decoration factor: ${res_fac}`;
        document.getElementsByTagName('textarea')[1].innerHTML = output;
    }


    let btn_gen = document.getElementsByTagName('button')[0];
    let btn_buy = document.getElementsByTagName('button')[1];
    btn_gen.addEventListener('click', generate);
    btn_buy.addEventListener('click', buy);
}