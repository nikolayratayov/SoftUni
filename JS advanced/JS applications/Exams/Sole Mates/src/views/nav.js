import { html, render, page } from "../api/lib.js";
import { logout } from "../api/user.js";
import { getUserData } from '../util.js';

let header = document.querySelector('header');
let navTemplate = (hasUser) => 
html`
<!-- Navigation -->
<a id="logo" href="/"
  ><img id="logo-img" src="./images/logo.png" alt=""
/></a>

<nav>
  <div>
    <a href="/catalog">Dashboard</a>
    <a href="/search">Search</a>
  </div>

  ${hasUser ? html`
  <div class="user">
    <a href="/create">Add Pair</a>
    <a @click=${onLogout} href="javascript:void(0)">Logout</a>
  </div>
  `
  :
  html`
  <div class="guest">
  <a href="/login">Login</a>
  <a href="/register">Register</a>
  </div>
  `}
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

