import {page, render} from './api/lib.js';
import { logout } from './api/user.js';
import { showCatalog } from './views/catalog.js';
import { showHome } from './views/home.js';
import { showLogin } from './views/login.js';
import { updateNav } from './views/nav.js';
import { showRegister } from './views/register.js';


let main = document.getElementById('content');
// document.getElementById('logoutBtn').addEventListener('click', onLogout)

page(decorateContext)
page('/', showHome);
page('/catalog', showCatalog);
page('/catalog/:id', () => console.log('details'));
page('/edit/:id', () => console.log('edit'));
page('/create', () => console.log('create'));
page('/login', showLogin);
page('/register', showRegister);
updateNav();
page.start();


function decorateContext(ctx, next) {
    ctx.render = renderMain;
    ctx.updateNav = updateNav;
    next();
}

function renderMain(content){
    render(content, main)
}

