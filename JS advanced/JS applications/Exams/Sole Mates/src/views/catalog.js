import {html, nothing} from '../api/lib.js';
import { getAll } from '../api/shoes.js';

let catalogTemplate = (shoes) => html`
<section id="dashboard">
<h2>Collectibles</h2>
<ul class="card-wrapper">
  ${shoes.length != 0 ? 
    shoes.map(shoeCardTemplate)
    : nothing}
</ul>
${shoes.length == 0 ? html`
<h2>There are no items added yet.</h2>` : nothing}
</section>
`;


let shoeCardTemplate = (shoe) => {
    let alt = shoe.imageUrl.split('/');
    alt = alt[alt.length - 1];
    alt = alt.split('.');
    alt = alt[0];
    return html`
    <li class="card">
    <img src=${shoe.imageUrl} alt=${alt} />
    <p>
        <strong>Brand: </strong><span class="brand">${shoe.brand}</span>
    </p>
    <p>
        <strong>Model: </strong
        ><span class="model">${shoe.model}</span>
    </p>
    <p><strong>Value:</strong><span class="value">${Number(shoe.value)}</span>$</p>
    <a class="details-btn" href="/catalog/${shoe._id}">Details</a>
    </li>
    `;
    }

export async function showCatalog(ctx){
    let shoes = await getAll();
    ctx.render(catalogTemplate(shoes));
}