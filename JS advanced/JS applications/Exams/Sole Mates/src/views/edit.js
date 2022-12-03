import {html} from '../api/lib.js';
import { getById, editShoe } from '../api/shoes.js';
import {createSubmitHandler} from '../util.js'

let editTemplate = (shoe, onEdit) => 
html`
<section id="edit">
<div class="form">
  <h2>Edit item</h2>
  <form @submit=${onEdit} class="edit-form">
    <input
      type="text"
      name="brand"
      id="shoe-brand"
      placeholder="Brand"
      .value=${shoe.brand}
    />
    <input
      type="text"
      name="model"
      id="shoe-model"
      placeholder="Model"
      .value=${shoe.model}
    />
    <input
      type="text"
      name="imageUrl"
      id="shoe-img"
      placeholder="Image url"
      .value=${shoe.imageUrl}
    />
    <input
      type="text"
      name="release"
      id="shoe-release"
      placeholder="Release date"
      .value=${shoe.release}
    />
    <input
      type="text"
      name="designer"
      id="shoe-designer"
      placeholder="Designer"
      .value=${shoe.designer}
    />
    <input
      type="text"
      name="value"
      id="shoe-value"
      placeholder="Value"
      .value=${shoe.value}
    />

    <button type="submit">post</button>
  </form>
</div>
</section>
`;

export async function showEdit(ctx){
let id = ctx.params.id;
let shoe = await getById(id);

    ctx.render(editTemplate(shoe, createSubmitHandler(onEdit)));

    async function onEdit({brand, imageUrl, model, release, designer, value}){
        if (brand == '' || imageUrl == '' || model == '' || release == '' || designer == '' || value == ''){
            return alert('All fields are required!');
        }
        await editShoe(id, {brand, imageUrl, model, release, designer, value});
        ctx.page.redirect('/catalog/' + id);
    }
}