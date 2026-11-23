<?php

/**
 * -------------------------------------------
 * CARGAR EL ARCHIVO DE CONEXIÓN
 * -------------------------------------------
 * 
 * Necesitamos la variable $conexion creada en
 * el archivo 01_conexion.php
 * 
 */
require_once "01_conexion.php";

/**
 * -------------------------------------------
 * DATOS A MODIFICAR
 * -------------------------------------------
 * 
 * Vamos a modificar el producto cuyo ID es 1.
 * 
 * Actualizaremos su precio y su stock.
 * 
 */
$id = 1;
$nuevo_precio = 99.99;
$nuevo_stock = 25;

/**
 * -------------------------------------------
 *  PREPARAR LA CONSULTA UPDATE
 * -------------------------------------------
 * 
 * UPDATE indica la tabla que vamos a modificar.
 * 
 * SET indica las columnas que recibiran nuevos valores.
 * 
 * WHERE especifica que registro queremos modificar.
 * 
 * IMPORTANTE:
 * Nunca olvidarse del WHERE.
 * 
 * Si se elimina el WHERE significa que se modificaran TODOS
 * los registros de la tabla.
 * 
 */
$stmt = $conexion->prepare("
    UPDATE productos
    SET
        precio = :precio,
        stock = :stock
    WHERE id = :id
");

/**
 * -------------------------------------------
 * EJECUTAR LA CONSULTA
 * -------------------------------------------
 * 
 * Los parametros reciben ahora los valores definidos
 * anteriormente en las variables.
 * 
 */
$stmt->execute([
    'precio' => $nuevo_precio,
    'stock' => $nuevo_stock,
    'id' => $id
]);

/**
 * -------------------------------------------
 * COMPROBAR CUANTAS FILAS HAN SIDO MODIFICADAS
 * -------------------------------------------
 * 
 * rowCount() devuelve el numero de filas afectadas
 * por la ultima consulta.
 * 
 * En nuestro caso deberia devolver 1.
 * 
 */

$filas_modificadas = $stmt->rowCount();

/**
 * -------------------------------------------
 * MOSTRAR EL RESULTADO
 * -----------------------------------------
 */
echo "Filas modificadas: " . $filas_modificadas;
