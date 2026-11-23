<?php

/**
 * -------------------------
 * DATOS DE LA CONEXIÓN A LA BASE DE DATOS
 * -------------------------
 * 
 * host:
 * Direccion del servidor donde esta alojada la base de datos.
 * Si MySQL esta instalado en el mismo ordenador que PHP,
 * normalmente se utiliza "localhost".
 * 
 */
$host = "localhost";

/**
 * -------------------------
 * NOMBRE DE LA BASE DE DATOS
 * -------------------------
 * 
 * Debe coincidir exactamente con el nombre de la base de datos 
 * creada en MySQL.
 * 
 */
$db_name = "tienda_online";

/**
 * -------------------------
 * USUARIO DE SQL
 * -------------------------
 * 
 * Usuario con permisos para acceder a la base de datos.
 * 
 */
$user = "root";

/**
 * -------------------------
 * CONTRASEÑA DEL USUARIO
 * -------------------------
 * 
 * Contraseña asociada al usuario anterior.
 * En algunos entornos locales como XAMPP suele estar vacia,
 * aunque en produccion siempre deberia tener una contraseña segura.
 * 
 */
$pass = "";

/**
 * -------------------------
 * APERTURA DEL BLOQUE TRY
 * -------------------------
 * TRY forma parte del sistema de manejo de excepciones de PHP.
 * 
 * Una excepcion es un mecanismo que permite notificar que se ha producido
 * un error durante la ejecucion del programa.
 * 
 * Cuando el codigo situado dentro del bloque try genera una excepcion,
 * la ejecucion se detiene inmediatamente y PHP busca un bloque catch
 * compatible para gestionar dicho error.
 * 
 * Esto evita tener que comprobar manualmente el resultado de cada operacion
 * y permite separar claramente la logica principal del tratamiento de errores.
 * 
 * Sintaxis general:
 *      try{
 *          Codigo que puede producir errores    
 *      } catch (TipoExcepcion $e){
 *          Tratamiento del error
 *      }
 * 
 */
try {

    /**
     * -------------------------
     * CREACION DEL DSN
     * -------------------------
     * DSN significa Data Source Name
     * 
     * Es una cadena de texto que contiene la informacion necesaria para que 
     * PDO depa a que sitema gestor de base de datos debe conectarse
     * 
     * Un DSN suele incluir:
     *  - Tipo de base de datos (mysql, pgsql...)
     *  - Nombre del servidor (host)
     *  - Puerto (opcional)
     *  - Nombre de la base de datos
     *  - Configuracion adicional
     * 
     * En este caso:
     * 
     * mysql            -> indica que usaremos MySQL
     * host=$host       -> servidor donde esta la BBDD
     * dbname=$dbname   -> nombre de la base de datos
     * charset=utf8mb4  -> juego de caracteres
     * 
     * Es muy importante usar utf8mb4 porque:
     *  - Soporta caracteres internacionales.
     *  - Soporta emojis.
     *  - Es el estandar recomendado actualmente.
     * 
     * Si no se especifica correctamente el charset pueden aparecer problemas
     * de codificacion, simbolos extraños o incluso perdida de datos. 
     * 
     */
    $dsn = "mysql:host=$host;dbname=$db_name;charset=utf8mb4";

    /**
     * -------------------------
     * CREACION DEL OBJETO PDO
     * -------------------------
     * PDO significa PHP Data Object
     * 
     * ES una capa de abstraccion de acceso a bases de datos.
     * 
     * Antes de PDO era habitual utilizar:
     *  - mysql_* (obsoleto)
     *  - mysqli
     * 
     * PDO aporta varias ventajas:
     *  - Mayor seguridad.
     *  - Sentencias preparadas.
     *  - Codigo portable entre distintos motores.
     *  - Manejo avanzado de errores mediante excepciones.
     * 
     * El operador new crea una nueva instancia de la clase PDO
     * 
     * Internamente PDO intentara:
     *  1. Localizar el servidor MySQL
     *  2. Verificar usuario y contraseña
     *  3. Abrir una conexion
     *  4. Asociarla al objeto creado
     * 
     * Parametros:
     *  $dsn    -> Informacion de conexion
     *  $user   -> Usuario de MySQL
     *  $pass   -> Contraseña de MySQL
     * 
     * Si alguno de estos datos es incorrecto, PDO lanzará una excepcion.
     *
     */
    $conexion = new PDO($dsn, $user, $pass);


    /**
     * -------------------------
     * CONFIGURACIÓN DEL MODO DE ERROR
     * -------------------------
     * PDO dispone de varios modos para notificar errores:
     * 
     * PDO::ERRMODE_SILENT
     *      No lanza excepciones
     *      El programador debe comprobar manualmente cada operacion
     * 
     * PDO::ERRMODE_WARNING
     *      Genera advertencias PHP
     * 
     * PDO::ERRMODE_EXCEPTION
     *      Lanza excepciones automáticamente
     * 
     * Esta ultima opcion es la recomendada porque:
     *  - Hace el codigo mas limpio
     *  - Facilita la depuracion
     *  - Centraliza el tratamiento de errores
     * 
     * ATTR_ERRMODE es una constante que identifica el atributo del modo
     * de gestion de errores.
     * 
     */
    $conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    /**
     * -------------------------
     * PREPARACIÓN DE LA CONSULTA SQL
     * -------------------------
     * Aqui NO se ejecuta todavia la consulta.
     * 
     * Lo que ocurre es:
     *  1. PHP envia la estructura SQL al motot MySQL
     *  2. MySQL la analiza
     *  3. MySQL la compila internamente
     *  4. Queda preparada para recibir datos.
     * 
     * Este mecanismo recibe el nombre de:
     * 
     * SENTENCIA PREPARADA (PREPARED STATEMENTE)
     * Ventajas:
     *  - Mayor seguridad
     *  - Proteccion contra SQL Injection
     *  - Posibilidad de reutilizar la consulta
     *  - Mejor rendimiento en algunos escenarios
     * 
     * El marcador :id_buscar es un parametro nombrado
     * Mas adelante se sustituira por un valor real.
     * 
     * SQL Injection:
     * Sin sentencias preparadas, un usuario podria intentar modificar la
     * consulta SQL introducida introduciendo codigo malicionso.
     * 
     * PDO separa completamente:
     *  - La estructura SQL.
     *  - Los datos del usuario.
     * 
     * Por ello las sentencias preparadas son la forma recomendada de trabajar. 
     * 
     */
    $stmt = $conexion->prepare("SELECT nombre 
                                FROM productos
                                WHERE id = :id_buscar");

    /**
     * -------------------------
     * VARIABLE CON EL ID A BUSCAR
     * -------------------------
     * Simulamos que queremos recuperar el producto cuyo identificador es 5.
     * 
     * Este valor podria venir de:
     *  - Un formulario
     *  - Una URL
     *  - Una API
     *  - Otra consulta
     * 
     */
    $id_buscado = 5;

    /**
     * -------------------------
     * EJECUCIÓN DE LA CONSULTA
     * -------------------------
     * 
     * execute() envia al motor SQL los valores reales que sustituiran a los
     * marcadores definidos durante el prepare()
     * 
     * En este caso:
     *  :id_buscar => 5
     * 
     * La consulta resultante sera conceptualmente:
     *  SELECT nombre
     *  FROM productos
     *  WHERE id = 5
     * 
     * Pero la sustitucion la realiza internamente PDO, nunca concatenando
     * cadenas manualmente
     * 
     * El parametro recibido por execute() es un array asociativo:
     *  [
     *      'id_buscar' => 5
     *  ]
     * 
     * La clave coincide con el nombre del parametro definido en la consulta
     * 
     */
    $stmt->execute(['id_buscar' => $id_buscado]);

    /**
     * -------------------------
     * RECUPERACIÓN DEL RESULTADO
     * -------------------------
     * 
     * fetch() obtiene UNA FILA del conjunto de resultados.
     * 
     * PDO::FETCH_ASSOC indica que queremos recibir los datos como un array
     * asociativo
     * 
     * Ejemplo:
     * 
     * Base de datos:
     * 
     * +----+---------+
     * | id | nombre  |
     * +----+---------+
     * | 5  | Teclado |
     * +----+---------+
     * 
     * Resultado:
     *  [
     *      'nombre' => 'Teclado'
     *  ]
     * 
     * Otros modos posibles:
     * 
     * PDO_FETCH_NUM
     * PDO::FETCH_OBJ
     * PDO::FETCH_BOTH
     * 
     * fetch() devuelve:
     *  - Un array si encuentra registros.
     *  - false si no existe ningun resultado
     * 
     */
    $producto = $stmt->fetch(PDO::FETCH_ASSOC);

    /**
     * -------------------------
     * COMPROBACION DE EXISTENCIA DEL RESULTADO
     * -------------------------
     * Si fetch() devolvio un array, la condicion sera verdadera
     * 
     * si fetch() devolvio false, significa que no se encontro ningun
     * producto con dicho identificador
     * 
     */
    if ($producto) {
        /**
         * -------------------------
         * CAPTURA DE EXCEPCIONES
         * -------------------------
         * PDOException es una clase especializada para errores de bases de datos.
         * 
         * Si ocurre cualquier problema durante:
         *  - La conexión.
         *  - La preparación.
         *  - La ejecución.
         *  - La recuperacion de datos.
         * 
         * PHP saltará inmemdiatamente a este bloque
         * 
         */
        echo "Nombre: " . $producto['nombre'];
    }


} catch (PDOException $e) {

    /**
     * -------------------------
     * INFORMACIÓN DEL ERROR
     * -------------------------
     * 
     * getMessage() devuelve una descripcion textual del error.
     * 
     * Ejemplos:
     *  - Usuario incorrecto.
     *  - Contraseña inválida.
     *  - Tabla inexistente.
     *  - Error de sintaxis SQL.
     * 
     * En aplicaciones reale normalmente no se muestra el mensaje tecnico al ususario final por moticos de seguridad.
     * 
     * Lo habitual es:
     *  - Guardarlo en logs.
     *  - Guardarlo en un mensaje genérico.
     * 
     */
    echo "Error en la base de datos: " . $e->getMessage();
}

/**
 * -------------------------
 * CIERRE MANUAL DE LA CONEXIÓN
 * -------------------------
 * PHP utiliza un sistema de gestion automática de memoria.
 * 
 * Cuando un objeto deja de tener referencias asociadas puede ser destruido
 * por el recolector de basura.
 * 
 * Al asignar null:
 *      $conexion = null;
 * eliminamos la referencia al objeto PDO.
 * 
 * Como consecuencia:
 *  - El objeto puede destruirse.
 *  - La conexión con MySQL puede cerrarse.
 * 
 * En scripts pequeños normalmente no es necesario hacer esto porque php
 * cerrara automaticamente todas las conexiones al finalizar el script. 
 * 
 * Sin embargo:
 *  - Puede ser util en scripts largos.
 *  - Puede liberar recursos antes de terminar la ejecución.
 * 
 */
$conexion = null;