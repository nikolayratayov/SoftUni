import {page, render} from './api/lib.js';

import { updateNav } from './views/nav.js';
import { getUserData } from './util.js';
import { showHome } from './views/home.js';
import { showLogin } from './views/login.js';
import { showRegister } from './views/register.js';
import { showCatalog } from './views/catalog.js';
import { showCreate } from './views/create.js';
import { showDetails } from './views/details.js';
import { showEdit } from './views/edit.js';


let main = document.querySelector('main');

page(decorateContext);
page('/', showHome);
page('/catalog', showCatalog);
page('/catalog/:id', showDetails);
page('/edit/:id', showEdit);
page('/create', showCreate);
page('/login', showLogin);
page('/register', showRegister);
updateNav();
page.start();

function decorateContext(ctx, next) {
    ctx.render = renderMain;
    ctx.updateNav = updateNav;
    let user = getUserData();
    if (user){
        ctx.user = user;
    }
    next();
}

function renderMain(content){
    render(content, main)
}