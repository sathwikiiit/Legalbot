
class Header extends HTMLElement {
    constructor() {
      super();
    }
  
    connectedCallback() {
        this.innerHTML = `
            <style>
            img {
                float: inline-start;
                width: 80px;
                border-radius: 100%;
                margin: 0px 20px;
            }
            h1, .user{
                color: #fff;
                padding: 0px 10px;
            }
            h1{
                display: inline-block;
                width: 30%;
                text-align: left;
            }
            
            .user {
                float: inline-end;
                width: 25%;
                text-align: right;
                vertical-align: bottom;
            }
            header {
                background-color:var(--primary);
                padding:1% 0px;
                width:100%;
                margin:0px
            }
            
            </style>
            <header>
                <img src=${im}>
                <h1>Legal Bot</h1>
                <div class="user">
                    <p>${user}</p>
                    <p>0 Suits</p>
                </div>
            </header>
        `;
    }
  }
  
class Footer extends HTMLElement {
    constructor() {
        super();
    }
  
    connectedCallback() {
        this.innerHTML = `
            <style>
                footer {
                    box-sizing: border-box;
                    background-color: black;
                    color:#fff;
                    width: 100%;
                    position: absolute;
                    bottom: 0px;
                }
            </style>
            <footer>
                <div class="footer_links">
                <a href="">Home</a>
                <a href="">About us</a>
                <a href="">Contact us</a>
                <a href="">Purchase License</a> 
                </div>
                <p>Copyright © 2024 LEGALBOT - All rights reserved || Designed By: Sathwik</p>
            </footer>
            `;
    }
}
customElements.define('header-content', Header);
customElements.define('footer-content', Footer);