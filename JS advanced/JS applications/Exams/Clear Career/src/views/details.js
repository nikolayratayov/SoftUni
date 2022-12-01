import { apply, getApplications, getOwnApplication } from '../api/applications.js';
import {html,nothing} from '../api/lib.js';
import { deleteById, getById } from '../api/offers.js';

let detailstemplate = (offer, applications, hasUser, canApply, isOwner, onDelete, onApply) => html`
<section id="details">
<div id="details-wrapper">
  <img id="details-img" src=${offer.imageUrl} alt="example1" />
  <p id="details-title">${offer.title}</p>
  <p id="details-category">
    Category: <span id="categories">${offer.category}</span>
  </p>
  <p id="details-salary">
    Salary: <span id="salary-number">${Number(offer.salary)}</span>
  </p>
  <div id="info-wrapper">
    <div id="details-description">
      <h4>Description</h4>
      <span>${offer.description}</span>
    </div>
    <div id="details-requirements">
      <h4>Requirements</h4>
      <span>${offer.requirements}</span>
    </div>
  </div>
  <p>Applications: <strong id="applications">${applications}</strong></p>
  ${offerControls(offer, hasUser, canApply, isOwner, onDelete, onApply)}
</div>
</section>
`;

function offerControls(offer, hasUser, canApply, isOwner, onDelete, onApply){
    if (!hasUser){
        return nothing;
    }
    if (canApply){
        return html`
        <div id="action-buttons">
            <a @click=${onApply} href="" id="apply-btn">Apply</a>
        </div>
        `;
    }
    if(isOwner){
        return html`
        <div id="action-buttons">
            <a href="/edit/${offer._id}" id="edit-btn">Edit</a>
            <a @click=${onDelete} href="javascript:void(0)" id="delete-btn">Delete</a>
        </div>
        `;
    }
}

export async function showDetails(ctx){
    let id = ctx.params.id;
    let requests = [
        getById(id),
        getApplications(id)
    ];
    let hasUser = ctx.user;

    if(hasUser){
        requests.push(getOwnApplication(id, ctx.user._id))
    }
    let [offer, applications, hasApplication] = await Promise.all(requests);

    let isOwner = hasUser && ctx.user._id == offer._ownerId;
    let canApply = !isOwner && hasApplication == 0;
    
    
    ctx.render(detailstemplate(offer, applications, hasUser, canApply, isOwner, onDelete, onApply))

    async function onDelete(){
        let choice = confirm('Are you sure you want to delete this pet?');
        if (choice){
            await deleteById(id);
            ctx.page.redirect('/catalog');
        }
    }

    async function onApply(){
        await apply(id);
        ctx.page.redirect('/catalog/' + id);
    }
}