function solve() {
   let divs = document.getElementsByClassName('product');
   for (let i = 0; i < divs.length; i++){
      divs[i].addEventListener('click', additem);
   }
   let cena = 0;
   let items = [];
   function additem(evt){
      let name = evt.currentTarget.getElementsByClassName('product-title')[0].innerHTML;
      let price = evt.currentTarget.getElementsByClassName('product-line-price')[0].innerHTML;
      cena += parseFloat(price);
      if (!(items.includes(name))){
         items.push(name);
      }
      document.getElementsByTagName('textarea')[0].innerHTML += `Added ${name} for ${price} to the cart.\n`;
   }
   let btn = document.getElementsByClassName('checkout')[0];
   btn.addEventListener('click', checkout);
   function checkout(){
      document.getElementsByTagName('textarea')[0].innerHTML += `You bought ${items.join(', ')} for ${cena.toFixed(2)}.`;
      let buttons = document.getElementsByClassName('add-product');
      for (let i = 0; i < buttons.length; i++){
         buttons[i].setAttribute('disabled', true);
      }
      document.getElementsByClassName('checkout')[0].setAttribute('disabled', true);
   }
}