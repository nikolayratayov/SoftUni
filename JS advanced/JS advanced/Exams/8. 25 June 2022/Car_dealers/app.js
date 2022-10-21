window.addEventListener("load", solve);

function solve() {

  document.getElementById('publish').addEventListener('click', (evt) => evt.preventDefault());
  document.getElementById('publish').addEventListener('click', publish);


  function publish(){
    let make = document.getElementById('make').value;
    let model = document.getElementById('model').value;
    let year = document.getElementById('year').value;
    let fuel = document.getElementById('fuel').value;
    let original_cost = Number(document.getElementById('original-cost').value);
    let sell_price = Number(document.getElementById('selling-price').value);
    if (make && model && year && fuel && original_cost && sell_price && original_cost <= sell_price){
      document.getElementById('make').value = '';
      document.getElementById('model').value = '';
      document.getElementById('year').value = '';
      document.getElementById('fuel').value = '';
      document.getElementById('original-cost').value = '';
      document.getElementById('selling-price').value = '';

      let td_make = document.createElement('td');
      td_make.innerHTML = make;

      let td_model = document.createElement('td');
      td_model.innerHTML = model;

      let td_year = document.createElement('td');
      td_year.innerHTML = year;

      let td_fuel = document.createElement('td');
      td_fuel.innerHTML = fuel;

      let td_original_cost = document.createElement('td');
      td_original_cost.innerHTML = original_cost;

      let td_sell_price = document.createElement('td');
      td_sell_price.innerHTML = sell_price;

      let btn_edit = document.createElement('button');
      btn_edit.className = 'action-btn edit';
      btn_edit.innerHTML = 'Edit';
      btn_edit.addEventListener('click', edit);

      let btn_sell = document.createElement('button');
      btn_sell.className = 'action-btn sell';
      btn_sell.innerHTML = 'Sell';
      btn_sell.addEventListener('click', sell);

      let td_btns = document.createElement('td');
      td_btns.appendChild(btn_edit);
      td_btns.appendChild(btn_sell);

      let tr = document.createElement('tr');
      tr.className = 'row';
      tr.appendChild(td_make)
      tr.appendChild(td_model)
      tr.appendChild(td_year)
      tr.appendChild(td_fuel)
      tr.appendChild(td_original_cost)
      tr.appendChild(td_sell_price)
      tr.appendChild(td_btns)

      document.getElementById('table-body').appendChild(tr);

    }
  }

  function edit(evt){
    let tds = evt.currentTarget.parentElement.parentElement.getElementsByTagName('td');
    document.getElementById('make').value = tds[0].innerHTML
    document.getElementById('model').value = tds[1].innerHTML
    document.getElementById('year').value = tds[2].innerHTML
    document.getElementById('fuel').value = tds[3].innerHTML
    document.getElementById('original-cost').value = tds[4].innerHTML
    document.getElementById('selling-price').value = tds[5].innerHTML
    evt.currentTarget.parentElement.parentElement.remove();
  }

  function sell(evt){
    let tds = evt.currentTarget.parentElement.parentElement.getElementsByTagName('td');

    let span_make_mode = document.createElement('span');
    span_make_mode.innerHTML = tds[0].innerHTML + ' ' + tds[1].innerHTML;

    let span_year = document.createElement('span');
    span_year.innerHTML = tds[2].innerHTML;

    let span_profit = document.createElement('span');
    span_profit.innerHTML = Number(tds[5].innerHTML) - Number(tds[4].innerHTML);

    let current_total_profit = Number(document.getElementById('profit').innerHTML);
    current_total_profit += Number(tds[5].innerHTML) - Number(tds[4].innerHTML);

    document.getElementById('profit').innerHTML = current_total_profit.toFixed(2);

    let li = document.createElement('li');
    li.className = 'each-list';
    li.appendChild(span_make_mode)
    li.appendChild(span_year)
    li.appendChild(span_profit)

    document.getElementById('cars-list').appendChild(li);

    evt.currentTarget.parentElement.parentElement.remove();
  }
  

}
