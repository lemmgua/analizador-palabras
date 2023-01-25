const mainInput = document.getElementById("mainInput");
const errorMessage = document.getElementById("errorMessage");
const infoLetrasDiv = document.getElementById("infoLetras");

const divSilabas = document.getElementById("silabas");

//Info Letras
const longitud = document.getElementById("longitud");
const vocales = document.getElementById("vocales");
const consonantes = document.getElementById("consonantes");
const diptongos = document.getElementById("diptongos");
const triptongos = document.getElementById("triptongos");
const acentos = document.getElementById("acentos");
const dieresis = document.getElementById("dieresis");
const letras = document.getElementById("silabasBar");

let silabas, info;
async function updateUi() {
    if (/[\W_]+/g.test(mainInput.value))
    {
        //Si encuentra carácter no válido
        errorMessage.hidden = false;
        infoLetras.hidden = true;
    } else {
        errorMessage.hidden = true;
        infoLetras.hidden = false;
        silabas = await eel.silabas(mainInput.value)();
        info = await eel.infoLetras(mainInput.value)();
        longitud.innerHTML = `<h1>Longitud: ${info["longitud"]}</h1>`;
        vocales.innerHTML = `<h1>N Vocales: ${info["vocales"]}</h1>`;
        consonantes.innerHTML = `<h1>N Consonantes: ${info["consonantes"]}</h1>`;
        diptongos.innerHTML = `<h1>N Diftongs: ${info["diptongos"]}</h1>`;
        triptongos.innerHTML = `<h1>N Triftongs: ${info["triptongos"]}</h1>`;
        acentos.innerHTML = `<h1>Accents: ${info["acentos"]}</h1>`;
        
        divSilabas.innerHTML = `<div>${silabas.join(" - ")}</div>`

        letras.innerHTML = `<div id="silabasBar"></div>`;
        for (key in info["letras"]) {
            liElement = document.createElement("h1");
            liElement.append(`${key} - ${info["letras"][key]}`);
            letras.appendChild(liElement)
        }
    }
}

mainInput.addEventListener("keyup", updateUi);