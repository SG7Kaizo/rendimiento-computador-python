function calcular() {
    var tiempo = document.getElementById("tiempo").value;
    var magnitudTiempo = document.getElementById("magnitud_tiempo").value;
    var tiempoConcatenado = tiempo + " " + magnitudTiempo;
    // Captura el valor del tiempo y lo muestra en el div resultado-tiempo

    document.getElementById("resultado-tiempo").innerText = tiempoConcatenado;
}        

// Función para actualizar checkboxes
function actualizarCheckboxes(checkboxId) {
    var checkbox1 = document.getElementById("checkbox1");
    var checkbox2 = document.getElementById("checkbox2");

    // Si se selecciona el checkbox1, deshabilita el checkbox2 y viceversa
    if (checkboxId === "checkbox1") {
        checkbox2.checked = false;
        checkbox2.disabled = true;
    } else if (checkboxId === "checkbox2") {
        checkbox1.checked = false;
        checkbox1.disabled = true;
    }
}

// Agrega eventos de cambio para los checkboxes
document.getElementById("checkbox1").addEventListener("change", function () {
    if (this.checked) {
        actualizarCheckboxes("checkbox1");
    } else {
        // Si se desmarca, habilita el otro checkbox
        document.getElementById("checkbox2").disabled = false;
    }
});

document.getElementById("checkbox2").addEventListener("change", function () {
    if (this.checked) {
        actualizarCheckboxes("checkbox2");
    } else {
        // Si se desmarca, habilita el otro checkbox
        document.getElementById("checkbox1").disabled = false;
    }
});