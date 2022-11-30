import {html} from '../api/lib.js';
import { getAll } from '../api/jobs.js';

let catalogTemplate = (jobs) => html`
<section id="dashboard">
<h2>Job Offers</h2>
    ${jobs.length == 0 ? html`
    <h2>No offers yet.</h2>
    ` : jobs.map(jobCardTemplate)}

</section>
`;

let jobCardTemplate = (job) => {
    let alt = job.imageUrl.split('/');
    alt = alt[alt.length - 1];
    alt = alt.split('.');
    alt = alt[0];
    return html`
<div class="offer">
<img src=${job.imageUrl} alt=${alt} />
<p>
  <strong>Title: </strong><span class="title">${job.title}</span>
</p>
<p><strong>Salary:</strong><span class="salary">${Number(job.salary)}</span></p>
<a class="details-btn" href="/catalog/${job._id}">Details</a>
</div>
`}

export async function showCatalog(ctx){
    let jobs = await getAll();
    ctx.render(catalogTemplate(jobs));
}