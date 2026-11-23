/**
 *------------------------------------------- 
 * MANEJADORES COMO FUNCIONES ETERNAS (UF3.1)
 * -------------------------------------------
 *
 *  - Recibimos el elemento XHTML como parametro (enviando con 'this' desde el HTML)
 *  - Comprobamso el color del borde con un switch contemplando como lo guardan
 *    los distintos navegadores (nombre, 4 bordes o hexadecimal)
 * 
 */
function resaltaExterno(elemento){
    switch(elemento.style.borderColor){
        case 'silver':
        case 'silver silver silver silver':
        case '#c0c0c0':
            elemento.style.borderColor = 'black';
            break;
        case 'black':
        case 'black black black black':
        case '#000000':
            elemento.style.borderColor = 'silver';
            break;
    }
}

/**
 * -------------------------------------------
 * FUNCION PARA MANEJADOR SEMANTICO (UF3.1)
 * -------------------------------------------
 * 
 *  - Esta función se asociará desde JavaScript sin ensuciar el HTML.
 *  - En los manejadores semanticos SI podemos usar 'this' directamente
 *    para referirnos al elemento qeu provoco el evento.
 * 
 */
function muestraMensaje(){
    alert('Gracias por pinchar en el boton con manejador semántico. Valor: ' + this.value);
}

/**
 * -------------------------------------------
 * USO DEL OBJETO EVENT (UF3.1)
 * -------------------------------------------
 * 
 *  - JavaScript pasa automaticamente un objeto 'event' como unico argumento
 *    a la funcion manejadora.
 *  - La propiedad 'evento.type' nos dice que evento exacto se ha disparado,
 *    permitiendo usar una sola funcion para manejar tanto 'mouseover' como 'mouseout'.
 * 
 */
function resaltaConEvento(evento){
    switch(evento.type){
        case 'mouseover':
            this.style.borderColor = 'red';
            console.log("El raton ha entrado: borde rojo");
            break;
        case 'mouseout':
            this.style.borderColor = 'silver';
            console.log("El raton ha salido: borde gris");
            break;
    }
}

/**
 * -------------------------------------------
 * ASIGNACIÓN AL CARGAR LA PÁGINA (window.onload)
 * -------------------------------------------
 * 
 *  - Para usar manejadores semanticos, el arbol DOM debe haberse cargado
 *    por completo. Usamos window.onload para asegurar que los elementos existe.ç
 * 
 */
window.addEventListener('load', function(){
    /**
     * -------------------------------------------
     * ASIGNAR MANEJADOR SEMANTICO SIN PARENTESIS
     * -------------------------------------------
     * 
     *  - IMPORTANTE: Se asigna 'muestraMensaje' SIN parentesis.
     *  - Si pusieramos muestraMensaje(), la funcion se ejecutaria al cargar la web
     *    y se guardaria su retorno en onclick, en vez de esperar al click.
     * 
     */
    let botonSemantico = document.getElementById("pinchable");
    botonSemantico.onclick = muestraMensaje;

    /**
     * -------------------------------------------
     * ASIGNAR MISMA FUNCION A VARIOS EVENTOS
     * -------------------------------------------
     * 
     *  - Asociamos 'resaltaConEvento' tanto a onmouseover como a onmouseout
     * 
     */
    let cajaEvento = document.getElementById("cajaObjetoEvent");
    cajaEvento.onmouseover = resaltaConEvento;
    cajaEvento.onmouseout = resaltaConEvento;

    /**
     * -------------------------------------------
     * EVENTOS DE FORMULARIO: ONFOCUS, ONBLUR, ONCHANGE
     * -------------------------------------------
     * 
     *  - onfocus: se dispara cuando el usuario entra/selecciona el campo
     *  - onblur: se dispara cuando el usuario sale del campo
     *  - onchange: se dispara al salir del campo SOLO si su contenido cambió
     * 
     */
    let campoNombre = document.getElementById("nombre");
    let infoFoco = document.getElementById("infoFoco");

    campoNombre.onfocus = function(){
        infoFoco.innerText = "[Tienes el foco en Nombre]";
    };
    campoNombre.onblur = function(){
        infoFoco.innerText = "[Has salido del campo nombre (perdio el foco)]";
    };
    campoNombre.onchange = function(){
        console.log("El valor del campo nombre ha cambiadoa: " + this.value);
    };
});