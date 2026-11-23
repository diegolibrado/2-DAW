<?php

/**
 * -------------------------------------------
 * DATOS DE CONEXIÓN
 * -------------------------------------------
 * 
 * host:
 * Servidor donde se encuentra MySQL.
 * 
 * localhost significa que MySQL esta instalado en el mismo equipo
 * 
 */
$host = "localhost";

/**
 * -------------------------------------------
 * NOMBRE DE LA BASE DE DATOS
 * -------------------------------------------
 */
$db_name = "curso_php";

/**
 * -------------------------------------------
 * USUARIO DE MYSQL
 * -------------------------------------------
 */
$user = "root";

/**
 * -------------------------------------------
 * CONTRASEÑA DE MYSQL
 * -------------------------------------------
 * 
 * En algunos entornos locales como XAMPP suele estar vacia.
 * 
 */
$pass = "";

/**
 * -------------------------------------------
 * MANEJO DE ERRORES MEDIANTE EXCEPCIONES
 * -------------------------------------------
 * 
 * Todo lo que pueda fallar ira dentro del bloque try.
 * 
 */
try {
    /**
     * -------------------------------------------
     * CONTRUCCION DEL DSN
     * -------------------------------------------
     * 
     * DSN significa Sata Source NAme
     * 
     * Indica a PDO:
     *  - Que motor usar.
     *  - Que servidor usar.
     *  - Que base de datos usar.
     *  - Que codificación usar.
     * 
     */
    $dsn = "mysql:host=$host;dbname=$db_name;charset=utf8mb4";

    /**
     * -------------------------------------------
     * CREACION DE LA CONEXION PDO
     * -------------------------------------------
     */
    $conexion = new PDO($dsn, $user, $pass);

    /**
     * -------------------------------------------
     * ACTIVAR EXCEPCIONES
     * -------------------------------------------
     * 
     * Cualquier error lanzara automaticamente una PDOException
     * 
     */
    $conexion->setAttribute(
        PDO::ATTR_ERRMODE,
        PDO::ERRMODE_EXCEPTION
    );

    echo "Conexion correcta.";
/**
* -------------------------------------------
* CAPTURA DE ERRORES
* -------------------------------------------
*/
} catch (PDOException $e) {
    echo $e->getMessage();
}
