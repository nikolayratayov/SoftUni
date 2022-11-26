import { html, render, page } from "../api/lib.js";
import { logout } from "../api/user.js";
import { getUserData } from "../util.js";

let header = document.querySelector('header');
let navTemplate = (hasUser) => html`
<nav>
<section class="logo">
    <img src="./images/logo.png" alt="logo">
</section>
<ul>
    <!--Users and Guest-->
    <li><a href="/">Home</a></li>
    <li><a href="/catalog">Dashboard</a></li>
    ${!hasUser ? html`
    <li><a href="/login">Login</a></li>
    <li><a href="/register">Register</a></li>
    ` : 
    html`
    <li><a href="/create">Create Postcard</a></li>
    <li><a @click=${onLogout} href="javascript:void(0)">Logout</a></li>`}
</ul>
</nav>
`;

export function updateNav(){
    let user = getUserData();

    render(navTemplate(user), header)
}

function onLogout(){
    logout();
    updateNav();
    page.redirect('/');
}

