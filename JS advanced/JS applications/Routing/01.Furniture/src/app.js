import * as api from '../api/data.js';
import {logout} from '../api/data.js';
import {render} from '../../../../../node_modules/lit-html/lit-html.js';
import page from '../../../../../node_modules/page/page.mjs';
import { catalogView } from './views/catalog.js';
import { createView } from './views/create.js';
import { detailsView } from './views/details.js';
import { editView } from './views/edit.js';
import { loginView } from './views/login.js';
import { myFurnitureView } from './views/myFurniture.js';
import { registerView } from './views/register.js';

let root = document.querySelector('.container');

page('/', renderMiddleware, catalogView);
page('/catalog', renderMiddleware, catalogView);
page('/create', renderMiddleware, createView);
page('/details/:id', renderMiddleware, detailsView);
page('/edit/:id', renderMiddleware, editView);
page('/login', renderMiddleware, loginView);
page('/register', renderMiddleware, registerView);
page('/my-furniture', renderMiddleware, myFurnitureView);
page('*', catalogView);
page.start();

updateNav();

document.getElementById('logoutBtn').addEventListener('click', async () => {
    await logout();
    updateNav();
    page.redirect('/')
})

function updateNav(){
    let userSection = document.getElementById('user');
    let guestSection = document.getElementById('guest');
    let userData = JSON.parse(sessionStorage.getItem('userData'));
    if (userData){
        userSection.style.display = 'inline-block';
        guestSection.style.display = 'none';
    }
    else{
        userSection.style.display = 'none';
        guestSection.style.display = 'inline-block';
    }
}

function renderMiddleware(ctx, next) {
    ctx.render = (content) => render(content, root);
    ctx.updateNav = updateNav;
    next();
}
