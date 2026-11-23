/**
 * -------------------------------------------
 * FUNCION GENERAL DE VALIDACION (UF3.3)
 * -------------------------------------------
 * 
 *  - Esta funcion esta vinculada a onsubmit = "return validacion()".
 *  - Revisa campo por campo en orden. En cuanto un campo falla,
 *    muestra un alert() y ejecuta 'return false' para frenar el envio
 * 
 */
function validacion(){
    /**
     * -------------------------------------------
     * 1. VALIDAR CAMPO DE TEXTO OBLIGATORIO
     * -------------------------------------------
     * 
     * Comprobamos 3 cosas:
     *    a) Que no sea null
     *    b) Que su longitud no sea 0 (no este vacio)
     *    c) Que no este relleno solo con espacios en blanco usando la expresion
     *       regular /^\s+$/ (donde ^ es inicio, \s+ es uno o mas espacios y $ es final)
     * 
     */
    let nombre = document.getElementById("nombre").value;
    if(nombre == null || nombre.length == 0 || /^\s+$/.test(nombre)){
        alert("[ERROR] El campo Nombre es obligatorio y no puede contener solo espacios.");
        return false;
    }

    /**
     * -------------------------------------------
     * 2. VALIDAR CAMPO CON VALOR NUMÉRICO
     * -------------------------------------------
     * 
     *  - isNan() devuelve true si el valor NO es un numero.
     *  - Ademas comprobamos que no lo hayan dejado vacio
     * 
     */
    let edad = document.getElementById("edad").value;
    if(edad.length == 0 || isNaN(edad)){
        alert("[ERROR] El campo Edad debe se un numero valido.");
        return false;
    }

    /**
    - -------------------------------------------
    - 3. VALIDAR CAMPO CON DNI
    - -------------------------------------------
    - 
    -  - La expresión regular /^\d{8}[A-Z]$/ comprueba que entre el inicio (^)
    -    y el final ($) haya exactamente 8 dígitos (\d{8}) seguidos de una
    -    letra mayúscula de la A a la Z ([A-Z]).
    - 
     */
    let dni = document.getElementById("dni").value;
    if (!(/^\d{8}[A-Z]$/.test(dni))) {
        alert("[ERROR] El DNI debe tener 8 números seguidos de 1 letra mayúscula.");
        return false;
    }

    /**
    - -------------------------------------------
    - 4. VALIDAR CAMPO CON NÚMERO DE TELÉFONO
    - -------------------------------------------
    - 
    -  - La expresión regular /^\d{9}$/ exige exactamente 9 cifras seguidas.
    - 
     */
    let telefono = document.getElementById("telefono").value;
    if (!(/^\d{9}$/.test(telefono))) {
        alert("[ERROR] El teléfono debe contener exactamente 9 números seguidos.");
        return false;
    }

    /**
    - -------------------------------------------
    - 5. VALIDAR CAMPO CON EMAIL
    - -------------------------------------------
    - 
    -  - Comprobamos que tenga texto local, el símbolo @, el dominio,
    -    un punto (.) y al menos dos letras al final (ej: usuario@live.uem.es).
    - 
     */
    let email = document.getElementById("email").value;
    if (!(/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/.test(email))) {
        alert("[ERROR] Debes introducir una dirección de email válida.");
        return false;
    }

    /**
     * -------------------------------------------
     * 6. VALIDAR FECHA (AÑO, MES, DIA)
     * -------------------------------------------
     * 
     *  - Construimoas un objeto Date(anyo, mes, dia). Recordamos que en JS los meses
     *    van de 0 (Enero) a 11 (Diciembre).
     *  
     *  - IMPORTANTE: En la diapositiva 14 de UF3.3 sale escrito
     *    id(!isNan(valor)), pero es una errata, realmente es isNAN(fecha)
     *    es true cuando la fecha NO es valida
     * 
     */
    let anyo = document.getElementById("anyo").value;
    let mes = document.getElementById("mes").value;
    let dia = document.getElementById("dia").value;
    let fecha = new Date(anyo, mes, dia);

    if(anyo.length == 0  || mes.length == 0 || dia.length == 0 || isNaN(fecha.getTime())){
        alert("[ERROR] Introduce una fecha valida");
        return false;
    }

    /**
     * -------------------------------------------
     * 7. VALIDAR SELECCION DE OPCION EN LISTA (<select>)
     * -------------------------------------------
     * 
     *  - Comprobamos que selectedIndex no sea null ni sea 0 (porque la posicion 0
     *    esta ocupada por el texto por defecto "-- Selecciona un valor --")
     * 
     */
    let indice = document.getElementById("opciones").selectedIndex;
    if(indice == null || indice == 0){
        alert("[ERROR] Debes seleccionar una opcion de la lista desplegable.");
        return false;
    }

    /**
     * -------------------------------------------
     * 8. VALIDAR QUE UN RADIOBUTTON ESTE SELECCIONADO
     * -------------------------------------------
     * 
     *  - Obtenemos todos los radios del grupo con getElementsByName().
     *  - Los recorremso con un bucle for; si encontramos uno con .checked == true,
     *    cambiamos la bandera 'seleccionado' a true y salimos con break. 
     * 
     */
    let opcionesRadio = document.getElementsByName("lenguaje");
    let seleccionado = false;
    for(let i = 0; i < opcionesRadio.length; i++){
        if(opcionesRadio[i].checked){
            seleccionado = true;
            break;
        }
    }
    if(!seleccionado){
        alert("[ERROR] Debes elegir un lenguaje de programacion en los RadioButtons.");
        return false;
    }

    /**
     * -------------------------------------------
     * 9. VALIDAR UN CHECKBOX OBLIGATORIO
     * -------------------------------------------
     * 
     *  - Comprobamos directamente si la propiedad .checked del checkbox es false.
     * 
     */
    let elementoCheck = document.getElementById("agree");
    if(!elementoCheck.checked){
        alert("[ERROR] Debes marcar la casilla para aceptar los terminos");
        return false;
    }

    /**
     * -------------------------------------------
     * TODAS LAS CONDICIONES SE HAN CUMPLIDO
     * -------------------------------------------
     * 
     *  - Si el script llega hasta aqui sin haber devuelto false,
     *    devolvemos true para uq eel formulario se entregue correctamente.
     * 
     */
    alert("¡Formulario validado con exito! Todos los datos son correctos.");
    return true;
}