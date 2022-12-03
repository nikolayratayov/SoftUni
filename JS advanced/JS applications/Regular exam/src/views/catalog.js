import {html, nothing} from '../api/lib.js';
import { getAll } from '../api/albums.js';

let catalogTemplate = (albums) => html`
<section id="dashboard">
<h2>Albums</h2>
<ul class="card-wrapper">
  <!-- Display a li with information about every post (if any)-->
    ${albums.length != 0 ? html`
    ${albums.map(albumCardTemplate)}
    `:nothing}
</ul>

<!-- Display an h2 if there are no posts -->
${albums.length == 0 ? html`
<h2>There are no albums added yet.</h2>
`:nothing}
</section>
`;

let albumCardTemplate = (album) => {
    let alt = album.imageUrl.split('/');
    alt = alt[alt.length - 1];
    alt = alt.split('.');
    alt = alt[0];
    return html`
    <li class="card">
    <img src=${album.imageUrl} alt=${alt} />
    <p>
      <strong>Singer/Band: </strong><span class="singer">${album.singer}</span>
    </p>
    <p>
      <strong>Album name: </strong><span class="album">${album.album}</span>
    </p>
    <p><strong>Sales:</strong><span class="sales">${album.sales}</span></p>
    <a class="details-btn" href="/catalog/${album._id}">Details</a>
  </li>
    `;
}

export async function showCatalog(ctx){
    let jobs = await getAll();
    ctx.render(catalogTemplate(jobs));
}