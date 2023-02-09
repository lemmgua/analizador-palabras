const mainInput = document.getElementById("mainInput");
const errorMessage = document.getElementById("errorMessage");
const insertMessage = document.getElementById("insertMessage");
const infoLetrasDiv = document.getElementById("infoLetras");

const divSilabas = document.getElementById("silabas");

//Info Letras
const longitud = document.getElementById("longitud");
const vocales = document.getElementById("vocales");
const consonantes = document.getElementById("consonantes");
const crecientes = document.getElementById("crecientes");
const decrecientes = document.getElementById("decrecientes");
const triptongos = document.getElementById("triptongos");
const hiatos = document.getElementById("hiatos");
const acentos = document.getElementById("acentos");
const dieresis = document.getElementById("dieresis");
const letras = document.getElementById("silabasBar");

async function updateUi() {
    if (mainInput.value == "")
    {
        insertMessage.hidden = false;
        errorMessage.hidden = true;
        divSilabas.hidden = true;
        infoLetrasDiv.hidden = true;
        letras.hidden = true;
        letras.style.scale = 0;
        infoLetrasDiv.style.scale = 0;
    }
    else if (/[\w·]+/g.test(mainInput.value) == false || /[0-9]+/g.test(mainInput.value) == true)
    {
        //Si encuentra carácter no válido
        errorMessage.hidden = false;
        insertMessage.hidden = true;
        divSilabas.hidden = true;
        infoLetrasDiv.hidden = true;
        letras.hidden = true;
        letras.style.scale = 0;
        infoLetrasDiv.style.scale = 0;
    } else {
        errorMessage.hidden = true;
        insertMessage.hidden = true;
        divSilabas.hidden = false;
        infoLetrasDiv.hidden = false;
        letras.hidden = false;
        infoLetrasDiv.style.scale = 1;
        letras.style.scale = 1;
        silabas = await eel.silabas(mainInput.value.toLowerCase())();
        info = await eel.infoLetras(mainInput.value.toLowerCase())();
        longitud.innerHTML = `<h1>Longitud: ${info["longitud"]}</h1>`;
        vocales.innerHTML = `<h1>N Vocales: ${info["vocales"]}</h1>`;
        consonantes.innerHTML = `<h1>N Consonantes: ${info["consonantes"]}</h1>`;
        crecientes.innerHTML = `<h1>Diftongs Creixents: ${info["diptongos"]["crecientes"].length > 0 ? info["diptongos"]["crecientes"] : "-"}</h1>`
        decrecientes.innerHTML = `<h1>Diftongs Decreixents: ${info["diptongos"]["decrecientes"].length > 0 ? info["diptongos"]["decrecientes"] : "-"}</h1>`
        triptongos.innerHTML = `<h1>Triftongs: ${info["triptongos"]}</h1>`;
        hiatos.innerHTML = `<h1>Hiats: ${info["hiatos"].length > 0 ? info["hiatos"] : "-"}`
        acentos.innerHTML = `<h1>Accents: ${info["acentos"].length > 0 ? info["acentos"] : "-"}</h1>`;
        
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