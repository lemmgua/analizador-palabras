const mainInput = document.getElementById("mainInput");
let silabas, info;
async function updateUi() {
    if (/\Wg+/.test(mainInput.value))
    {
        //Si encuentra carácter no válido
    } else {
        silabas = await eel.silabas(mainInput.value);
        info = await eel.infoLetras(mainInput.value);
    }
}

mainInput.addEventListener("keyup", updateUi);