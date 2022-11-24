import {html} from '../../../../../../node_modules/lit-html/lit-html.js';
import {getAllItem} from '../../api/data.js';

export async function catalogView(ctx){
    let items = await getAllItem();
    ctx.render(catalogTemp(items))
}

function catalogTemp(data){
    return html`
    <div class="row space-top">
        <div class="col-md-12">
            <h1>Welcome to Furniture System</h1>
            <p>Select furniture from the catalog to view details.</p>
        </div>
    </div>
    <div class="row space-top">
        ${Object.values(data).map(x => createItemTemp(x))}
    </div>
    `
}

function createItemTemp(itemDetails){
    return html`
    <div class="col-md-4">
        <div class="card text-white bg-primary">
            <div class="card-body">
                    <img src="/JS advanced/JS applications/Routing/01.Furniture/${itemDetails.img}" />
                    <p>${itemDetails.description}</p>
                    <footer>
                        <p>Price: <span>${itemDetails.price} $</span></p>
                    </footer>
                    <div>
                        <a href="/details/${itemDetails._id}" class="btn btn-info">Details</a>
                    </div>
            </div>
        </div>
    </div>
    `
}