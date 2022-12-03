import {html} from '../api/lib.js';
import { createAlbum } from '../api/albums.js';
import {createSubmitHandler} from '../util.js'

let createTemplate = (onCreate) => html`
<section id="create">
<div class="form">
  <h2>Add Album</h2>
  <form @submit=${onCreate} class="create-form">
    <input type="text" name="singer" id="album-singer" placeholder="Singer/Band" />
    <input type="text" name="album" id="album-album" placeholder="Album" />
    <input type="text" name="imageUrl" id="album-img" placeholder="Image url" />
    <input type="text" name="release" id="album-release" placeholder="Release date" />
    <input type="text" name="label" id="album-label" placeholder="Label" />
    <input type="text" name="sales" id="album-sales" placeholder="Sales" />

    <button type="submit">post</button>
  </form>
</div>
</section>
`;

export function showCreate(ctx){
    ctx.render(createTemplate(createSubmitHandler(onCreate)));

    async function onCreate({singer, imageUrl, album, release, label, sales}){
        if (singer == '' || imageUrl == '' || album == '' || release == '' || label == '' || sales == ''){
            return alert('All fields are required!');
        }
        await createAlbum({singer, imageUrl, album, release, label, sales});
        ctx.page.redirect('/catalog');
    }
}