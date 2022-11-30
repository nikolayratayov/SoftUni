import {page, render} from './api/lib.js';
import { showCatalog } from './views/catalog.js';
import { showHome } from './views/home.js';
import { updateNav } from './views/nav.js';
import { getUserData } from './util.js';
import { showLogin } from './views/login.js';

let main = document.querySelector('main');

page(decorateContext);
page('/', showHome);
page('/catalog', showCatalog);
page('/catalog/:id', () => console.log('details'));
page('/edit/:id', () => console.log('edit'));
page('/create', () => console.log('create'));
page('/login', showLogin);
page('/register', () => console.log('register'));
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