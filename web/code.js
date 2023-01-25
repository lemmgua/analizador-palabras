const mainInput = document.getElementById("mainInput");

const divSilabas = document.getElementById("silabas");

//Info Letras
const longitud = document.getElementById("longitud");
const vocales = document.getElementById("vocales");
const consonantes = document.getElementById("consonantes");
const diptongos = document.getElementById("diptongos");
const triptongos = document.getElementById("triptongos");
const acentos = document.getElementById("acentos");
const dieresis = document.getElementById("dieresis");
const letras = document.getElementById("letras");

let liElement = document.createElement("li");
let silabas, info;
async function updateUi() {
    if (/\Wg+/.test(mainInput.value))
    {
        //Si encuentra carácter no válido
    } else {
        silabas = await eel.silabas(mainInput.value)();
        info = await eel.infoLetras(mainInput.value)();
        longitud.innerHTML = `<h1>${info["longitud"]}</h1>`;
        /* letras.innerHTML = `<ul></ul>`;
        for (key in info) {
            liElement = document.createElement("li");
            liElement.append(`${key} - ${info[key]}`);
            letras.appendChild(liElement)
        } */
    }
}

mainInput.addEventListener("keyup", updateUi);