import {page, render} from './api/lib.js';
import { updateNav } from './views/nav.js';
import { getUserData } from './util.js';
import { showHome } from './views/home.js';

let main = document.querySelector('main');

page(decorateContext);
page('/', showHome);
page('/catalog', () => console.log('dashboard'));
page('/search', () => console.log('search'));
page('/catalog/:id', () => console.log('details'));
page('/edit/:id', () => console.log('edit'));
page('/create', () => console.log('create'));
page('/login', () => console.log('login'));
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