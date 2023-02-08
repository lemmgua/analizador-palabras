customElements.define("info-palabra", class InfoPalabra extends HTMLElement {
    constructor() {
        super();

        const style = document.createElement("style");
        const template = document.createElement("template");

        const content = template.content;

        this.attachShadow({ mode: "open" });
    }
    async connectedCallback() {
        this.shadowRoot.innerHTML = `
        <h1><slot></slot></h1>
        `;
        console.log(this.shadowRoot.querySelectorAll("slot").forEach(el => console.log(el.innerText)));
        //conseguir valor del slot -> this.shadowRoot.querySelector('slot');
    }
});