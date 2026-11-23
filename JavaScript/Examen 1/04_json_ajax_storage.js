window.addEventListener('load', function(){
    const cajaResultado = document.getElementById("resultadoAJAX");

    /**
     * -------------------------------------------
     * 1. OBJETO ESTATICO JSON: STRINGIFY Y PARSE (UF4.1)
     * -------------------------------------------
     * 
     *  - JSON no se instancia (sus metodos son estaticos).
     *      • JSON.stringfy(): transforma un objeto JS en una cadena de texto JSON.
     *      • JSON.parse(): transforma un texto JSON en un objeto JavaScript real.
     * 
     */
    document.getElementById("btnProbarJSON").onclick = function(){
        let objetoJS = {
            empleados: [
                {nombre: "Carlos", apellido: "Martinez"},
                {nombre: "Julio", apellido: "Maldonado"}
            ],
            activo: true,
            total:2
        };

        // De objeto JS a Texto JSON
        let textoJSON = JSON.stringify(objetoJS);

        // De texto JSON de vuelta a Objeto JS
        let objetoRecuperado = JSON.parse(textoJSON);

        cajaResultado.innerHTML = `
            <strong>Texto JSON generado con stringify():</strong><br>
            <code>${textoJSON}</code><br><br>
            <strong>Dato leído tras usar parse():</strong> 
            Empleado 1: ${objetoRecuperado.empleados[0].nombre} ${objetoRecuperado.empleados[0].apellido}
        `;
    }

    /**
     * -------------------------------------------
     * 2. PETICION ASINCRONA CON XMLHttpRequest (UF4.1)
     * -------------------------------------------
     * 
     *  - Es la forma clasica de hacer AJAX sin recargar la pagina:
     *      1) Creamos la instancia new XMLHttpRequest().
     *      2) Configuramos con open("GET", URL, true) -> true indica asincrono.
     *      3) Escuchamos onreadystatechange: cuando readyState == 4 (completado)
     *         y status == 200 (respuesta HTTP OK), procesamos this.responseText.
     *      4) Enviamos la peticion con send()
     * 
     */
    document.getElementById("btnXHR").onclick = function(){
        const http = new XMLHttpRequest();
        http.open("GET", "https://jsonplaceholder.typicode.com/users/1", true);

        http.onreadystatechange = function(){
            if(this.readyState == 4 && this.status == 200){
                let usuario = JSON.parse(this.responseText);
                cajaResultado.innerHTML = `
                    <strong>Respuesta recibida con XMLHttpRequest:</strong><br>
                    Nombre: ${usuario.name} ---- Email: ${usuario.email} 
                `;
            }
        };

        http.send();
    };

    /**
     * -------------------------------------------
     * 3. PETICION ASINCRONA CON FETCH API - GET (UF4.1)
     * -------------------------------------------
     * 
     *  - Fetch esta basado en Promesas (estados: pending, fulfilled, rejected)
     *  - Si no indicamos metodo, por defecto hace GET.
     *  - El primer .then() recibe la respuesta cuyo body es un 'stream',
     *    por lo que llamamos a respuesta.json() para extraer los datos.
     *  - El segundo .then() ya recibe el objeto JSON listo para usar.
     *  - El .catch() captura posibles errores de conexion.
     * 
     */
    document.getElementById("btnFetchGet").onclick = function(){
        fetch("https://jsonplaceholder.typicode.com/users/1")
            .then(respuesta => respuesta.json())
            .then(usuario => {
                cajaResultado.innerHTML = `
                    <strong>Respuesta GET con Fetch API:</strong><br>
                    ID: ${usuario.id}<br>
                    Nombre: ${usuario.name}<br>
                    Usuario: ${usuario.username}<br>
                    Calle: ${usuario.address.street}
                `;
            })
            .catch(error =>{
                console.log("Error en la peticion Fetch GET: " , error);
            });
    };

    /**
     * -------------------------------------------
     * 4. ENVIAR DATOS JSON CON FETCH API - POST (UF4.1)
     * -------------------------------------------
     * 
     *  - Para enviar datos al servidor pasamos unsegundo parametro de opciones a fetch():
     *      • method: "POST"
     *      • body: convertimos nuestro objeto a cadena JSON.stringify(data)
     *      • headers: indicamos "Content-Type": "application/json"
     * 
     */
    document.getElementById("btnFetchPost").onclick = function(){
        var url = "https://jsonplaceholder.typicode.com/posts";
        var data = {username: "Diego_DAW", rol: "Administrador"};

        fetch(url, {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(res => res.json())
        .catch(error => console.error("Error: ", error))
        .then(response => {
            console.log("Success: ", response );
            cajaResultado.innerHTML= `
                <strong>Respuesta POST con Fetch API:</strong><br>
                Datos enviados correctamente. ID asignado por la API: ${response.id}<br>
                Usuario registrado: ${response.username}
            `;
        });    
    };

    /**
     * -------------------------------------------
     * 5. GUARDAR EN LOCALSTORAGE Y SESSIONSTORAGE (UF4.1)
     * -------------------------------------------
     * 
     *  - localStorage: guarda los datos en el navegador sin fecha de caducidad
     *    (no se borran al cerrar la pestaña y son accesibles entre pestañas del mismo dominio).
     *  - sessionStorage: usa exactamente los mismos metodos, pero los datos
     *    solo viven en la pestaña actual y se borran al cerrarla.
     * 
     * IMPORTANTE: Ambos guardan SIEMPRE Strings.Si queremos guardar un objeto,
     * hay que pasarlo antes por JSON.stringify().
     * 
     */
    document.getElementById("btnGuardarStorage").onclick = function(){
        
        // Guardar un String simple con setItem(key, value)
        localStorage.setItem("curso", "2ª DAW");

        // Guardar un Objeto convirtieldolo antes a texto JSON
        let preferencias =  {tema: "oscuro", idioma: "es"};
        localStorage.setItem("configuracion", JSON.stringify(preferencias));

        cajaResultado.innerHTML = `
            Datos guardados correctamente.<br>
            Elementos actuales en localStorage (propiedad .length): <strong>${localStorage.length}</strong><br>
            Nombre de l aprimera clave guardada con key(0): <strong>${localStorage.key(0)}</strong>
        `;
    };

    /**
     * -------------------------------------------
     * 6. LEER DATOS DE LOCALSTORAGE
     * -------------------------------------------
     * 
     *  - Recuperamos los valores asociados a cada clave usando getItem(key)
     *  - Si era un objeto en JSON, lo reconstruimos con JSON.parse()
     * 
     */
    document.getElementById("btnLeerStorage").onclick = function(){
        let curso = localStorage.getItem("curso");
        let configTexto = localStorage.getItem("configuracion");

        if(curso && configTexto){
            let configObjeto = JSON.parse(configTexto);
            cajaResultado.innerHTML = `
                <strong>Datos recuperados de LocalStorage</strong><br>
                Curso: ${curso}<br>
                Tema preferido: ${configObjeto.tema}
            `;
        } else {
            cajaResultado.innerHTML = "No hay datos guardados en la LocalStorage todavia.";
        }
    };

    /**
     * -------------------------------------------
     * 7. BORRAR ELEMENTOS Y VACIAR STORAGE (removeItem y clear)
     * -------------------------------------------
     * 
     *  - removeItem(key): borra un unico dato especifico.
     *  - clear(): vacia por completo todo el almacen de localStorage de este dominio
     * 
     */
    document.getElementById("btnBorrarStorage").onclick = function(){
        localStorage.removeItem("curso");
        localStorage.clear();
        cajaResultado.innerHTML = "LocalStorage vaciado con clear(). Elementos restantes: " + localStorage.length;
    };
});