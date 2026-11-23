/**
 * -------------------------------------------
 * UTILIDAD: LIMITAR CARACTERES EN TEXTAREA (UF3.2)
 * -------------------------------------------
 * 
 *  - Esta funcion es llamada por el atributo onkeypress="return limita(20);"
 *  - Si la longitud del texto es mayor o igual al maximo permitido, devuelve false.
 *  - Al devolver false en onkeypress, el navegador bloquea la tecla pulsada.
 * 
 */
function limita(maximoCaracteres){
    let elemento = document.getElementById("texto");

    if(elemento.value.length >= maximoCaracteres){
        return false;
    } else {
        return true;
    }
}

window.addEventListener('load', function(){
    /**
     * -------------------------------------------
     * ACCESO A FORMULARIOS Y CAMPOS (UF3.2)
     * -------------------------------------------
     * 
     *  - document.forms devuelve la coleccion de formularios de la pagina.
     *  - form.elements almacena todos los controles (inputs, select, etc) dentro de el
     * 
     */
    const primerFormulario = document.forms[0];
    const campoPorNombre = primerFormulario.elements['nombre'];
    console.log("Formulario cargado. Primer campo:", campoPorNombre.name);

    /**
     * -------------------------------------------
     * ESTABLECER EL FOCO EN EL PRIMER ELEMENTO
     * -------------------------------------------
     * 
     *  - Buena practica de usabilidad: al cargar la pagina, buscamos el primer
     *    formulario y recorremos sus elementos hasta encontrar el primero que 
     *    no sea de tipo oculto (type != "hidden") para asignarle el foco con focus()
     * 
     */
    if(document.forms.length > 0){
        for(let i = 0; i < document.forms[0].elements.length; i++){
            let campo = document.forms[0].elements[i];
            if(campo.type != "hidden"){
                campo.focus();
                break;
            }
        }
    }

    /**
     * -------------------------------------------
     * MANEJO DE RADIOBUTTONS (UF3.2)
     * -------------------------------------------
     * 
     * 1. Seleccionamos todos los radiobuttons con name="language"
     * 2. Al pulsar el boton, recorremos la lista con for...of para ver cual
     *    tiene la propiedad .checked en true, guardamos su .value y salimos con break;
     * 
     */
    const btnVerRadio = document.querySelector("#btnVerRadio");
    const radioButtons = document.querySelectorAll('input[name="lenguaje"]');
    const outputRadio = document.getElementById("outputRadio");

    btnVerRadio.addEventListener("click", () =>{
        let lenguajeSeleccionado;

        for(const radioButton of radioButtons){
            if(radioButton.checked){
                lenguajeSeleccionado = radioButton.value;
                break;
            }
        }

        outputRadio.innerText = lenguajeSeleccionado ?
            `Has seleccionado: ${lenguajeSeleccionado}`:
            `No has seleccionado ningun lenguaje todavia`;
    });

    /**
     * Tambien pidemos escuchar el evento 'change' en cada radioButton
     * para detectar al instante cuando el usuario cambia de opcion.
     */
    for(const radioButton of radioButtons){
        radioButton.addEventListener('change', function(){
            if(this.checked){
                console.log("Cambiarde el radioButton a: " + this.value);
            }
        });
    }

    /**
     * -------------------------------------------
     * MANEJO DE CHACKBOX: MARCAR Y DESMARCAR TODOS (UF3.2)
     * -------------------------------------------
     * 
     *  - Resolucion del Ejercicio 2 de las diapositivas:
     *  - Para saber o cambiar el estado de un checkbox usamos la propiedad .checked
     *    (que vale true o false), nunca vale .value
     * 
     */
    const btnMarcarTodos = document.getElementById("btnMarcarTodos");
    const btnDesmarcarTodos = document.getElementById("btnDesmarcarTodos");

    btnMarcarTodos.onclick = function(){
        for(let i = 0; i < primerFormulario.elements.length; i++){
            if(primerFormulario.elements[i].type == "checkbox"){
                primerFormulario.elements[i].checked = true;
            }
        }
    };
    btnDesmarcarTodos.onclick = function(){
        for(let i = 0; i < primerFormulario.elements.length; i++){
            if(primerFormulario.elements[i].type == "checkbox"){
                primerFormulario.elements[i].checked = false;
            }
        }
    };

    /**
     * -------------------------------------------
     * MANEJO DE SELECT SIMPLE (UF3.2)
     * -------------------------------------------
     * 
     *  - lista.selectedIndex devuelve la posicion (indice) de la opcion elegida
     *  - lista.options es el array con todas las etiquetas <option>
     *  - Combinando ambos obtenemos tanto el .value como el .text visible
     * 
     */
    const btnVerSelect = document.getElementById("btnVerSelect");

    btnVerSelect.onclick = function(){
        let lista = document.getElementById("opciones");
        let indiceSeleccionado = lista.selectedIndex;
        let opcionSeleccionada = lista.options[indiceSeleccionado];

        let textoSeleccionado = opcionSeleccionada.text;
        let valorSeleccionado = opcionSeleccionada.value;

        alert("Opcion seleccionada: " + textoSeleccionado + "\nValor de la opcion: " + valorSeleccionado);
    }

    /**
     * -------------------------------------------
     * MANEJO DE SELECT MULTIPLE (UF3.2)
     * -------------------------------------------
     * 
     *  - Cuando un <select> tiene el atributo 'multiple', convertimos sus opciones
     *    en un Array con Array.from, filtramos las que tienen .selected == true
     *    y extraemos sus textos con .map().
     * 
     */
    const btnVerMultiple = document.getElementById("btnVerMultiple");

    btnVerMultiple.onclick = function(){
        const selectElement = document.getElementById("cities");
        const selectedOptions = Array.from(selectElement.options).filter(option=>option.selected);
        const selectedValues = selectedOptions.map(option=>option.text);

        alert("Ciudades seleccionadas: " + selectedValues.join(", "));
    }

    /**
     * -------------------------------------------
     * EVENTO RESET DEL FORMULARIO (UF3.2)
     * -------------------------------------------
     * 
     *  - Se activa cuando el usuario pulsa el boton <input type = "reset">
     * 
     */
    primerFormulario.addEventListener('reset', function(){
        console.log("El formulario se ha restablecido a sus valores por defecto.");
    })


});