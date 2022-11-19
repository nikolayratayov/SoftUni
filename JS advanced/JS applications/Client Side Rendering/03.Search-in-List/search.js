import {towns} from './towns.js'
import {html, render} from '../../../../node_modules/lit-html/lit-html.js'

let root = document.getElementById('towns');
let btn = document.getElementsByTagName('button')[0];
btn.addEventListener('click', search);
let resCount = 0;

let townsContainer = html`
   <ul>
      ${towns.map(x => getli(x, null))}
   </ul>
   `;

function getli(town, substr){
   if (town.includes(substr)){
      resCount += 1;
      return html`<li class='active'>${town}</li>`
   }
   return html`<li>${town}</li>`
   
}

render(townsContainer, root);

function search(e) {
   let textNode = document.getElementById("searchText");
   let text = textNode.value;
   if (text == ''){text = null}
   textNode.value = '';
   resCount = 0;
   townsContainer = html`
   <ul>
      ${towns.map(x => getli(x, text))}
   </ul>
   `;
   render(townsContainer, root);
   document.getElementById('result').innerHTML = `${resCount} matches found`;

}
