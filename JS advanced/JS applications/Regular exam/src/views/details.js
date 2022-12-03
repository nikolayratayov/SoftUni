import { like, getLikes, getOwnLike } from '../api/likes.js';
import {html,nothing} from '../api/lib.js';
import { deleteById, getById } from '../api/albums.js';

let detailstemplate = (album, likes, hasUser, canLike, isOwner, onDelete, onLike) => html`
<section id="details">
<div id="details-wrapper">
  <p id="details-title">Album Details</p>
  <div id="img-wrapper">
    <img src=${album.imageUrl} alt="example1" />
  </div>
  <div id="info-wrapper">
    <p><strong>Band:</strong><span id="details-singer">${album.singer}</span></p>
    <p>
      <strong>Album name:</strong><span id="details-album">${album.album}</span>
    </p>
    <p><strong>Release date:</strong><span id="details-release">${album.release}</span></p>
    <p><strong>Label:</strong><span id="details-label">${album.label}</span></p>
    <p><strong>Sales:</strong><span id="details-sales">${album.sales}</span></p>
  </div>
  <div id="likes">Likes: <span id="likes-count">${likes}</span></div>
  ${albumControls(album, hasUser, canLike, isOwner, onDelete, onLike)}
</div>
</section>
`;

function albumControls(album, hasUser, canLike, isOwner, onDelete, onLike){
    if (!hasUser){
        return nothing;
    }
    if (canLike){
        return html`
        <div id="action-buttons">
            <a @click=${onLike} href="" id="like-btn">Like</a>
        </div>
        `;
    }
    if(isOwner){
        return html`
        <div id="action-buttons">
            <a href="/edit/${album._id}" id="edit-btn">Edit</a>
            <a @click=${onDelete} href="javascript:void(0)" id="delete-btn">Delete</a>
        </div>
        `;
    }
}

export async function showDetails(ctx){
    let id = ctx.params.id;
    let requests = [
        getById(id),
        getLikes(id)
    ];
    let hasUser = ctx.user;

    if(hasUser){
        requests.push(getOwnLike(id, ctx.user._id))
    }
    let [album, likes, hasLike] = await Promise.all(requests);

    let isOwner = hasUser && ctx.user._id == album._ownerId;
    let canLike = !isOwner && hasLike == 0;
    
    
    ctx.render(detailstemplate(album, likes, hasUser, canLike, isOwner, onDelete, onLike))

    async function onDelete(){
        let choice = confirm('Are you sure you want to delete this album?');
        if (choice){
            await deleteById(id);
            ctx.page.redirect('/catalog');
        }
    }

    async function onLike(){
        await like(id);
        ctx.page.redirect('/catalog/' + id);
    }
}