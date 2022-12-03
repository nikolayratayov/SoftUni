import {html, nothing} from '../api/lib.js';
import { searchShoe } from '../api/shoes.js';
import {createSubmitHandler, getUserData} from '../util.js'

let user = getUserData();

let searchTemplate = (searchFunc) => html`
<section id="search">
<h2>Search by Brand</h2>

<form @submit=${searchFunc} class="search-wrapper cf">
  <input
    id="#search-input"
    type="text"
    name="search"
    placeholder="Search here..."
    required
  />
  <button type="submit">Search</button>
</form>

<h3>Results:</h3>

</section>
`;

let searchResults = (shoes) => html`
<section id="search">
<h2>Search by Brand</h2>

<form class="search-wrapper cf">
  <input
    id="#search-input"
    type="text"
    name="search"
    placeholder="Search here..."
    required
  />
  <button type="submit">Search</button>
</form>

<h3>Results:</h3>

<div id="search-container">
  <ul class="card-wrapper">
    <!-- Display a li with information about every post (if any)-->
    ${
        shoes ? 
    shoes.map(shoeTemplate): nothing}
  </ul>

  <!-- Display an h2 if there are no posts -->
  ${shoes.length == 0 ? html`
  <h2>There are no results found.</h2>
  `: nothing}
</div>
</section>
`;

let shoeTemplate = (shoe) => html`
<li class="card">
<img src=${shoe.imageUrl} alt="travis" />
<p>
  <strong>Brand: </strong><span class="brand">${shoe.brand}</span>
</p>
<p>
  <strong>Model: </strong
  ><span class="model">${shoe.model}</span>
</p>
<p><strong>Value:</strong><span class="value">${Number(shoe.value)}</span>$</p>
${user ? html`
<a class="details-btn" href="/catalog/${shoe._id}">Details</a>
`: nothing}
</li>
`;


export async function showSearch(ctx){

    ctx.render(searchTemplate(createSubmitHandler(searchFunc)));

    async function searchFunc({search}){
        if (search == ''){
            return alert('Field is required!');
        }
        
        let results = await searchShoe(search);
        

        ctx.render(searchResults(results))
    }
}