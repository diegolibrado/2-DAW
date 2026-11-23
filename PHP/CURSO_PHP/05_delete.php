<?php

/**
 * -------------------------------------------
 * CARGAR EL ARCHIVO DE CONEXION
 * -------------------------------------------
 * 
 * Utilizamos la conexion creada anteriormente
 * 
 */
require_once "01_conexion.php";

/**
 * -------------------------------------------
 * ID DEL PRODUCTO A ELIMINAR
 * -------------------------------------------
 * 
 * Vamos a eliminar el producto cuyo id sea 4.
 * 
 * Puedes cambiar este valor por cualquier otro existente
 * en tu base de datos.
 * 
 */
$id = 4;

/**
 * -------------------------------------------
 * PREPARAR LA CONSULTA SQL
 * -------------------------------------------
 * 
 * DELETE FROM indica de que tabla queremos eliminar datos.
 * 
 * WHERE especifica que registro debe borrarse.
 * 
 * MUY IMPORTANTE:
 * 
 * Nunca eliminar el WHERE sin querer.
 * 
 * Si ejecutamos:
 * 
 * DELETE FROM productos;
 * 
 * Borraremos TODOS los registros de la tabla
 * 
 */
$stmt = $conexion->prepare("
    DELETE FROM productos
    WHERE id = :id
");

/**
 * -------------------------------------------
 * EJECUTAR LA CONSULTA
 * -------------------------------------------
 * 
 * El parametro :id sera sustituido por el valor 
 * almacenado en la variable $id.
 * 
 */
$stmt->execute([
    'id' => $id
]);

/**
 * -------------------------------------------
 *  COMPROBAR FILAS ELIMINADAS
 * -------------------------------------------
 * 
 * rowCount() devuelve cuantas filas han sido
 * afectadas por la consulta.
 * 
 * Si devuelve:
 *  1 → Se ha eliminado un registro
 *  0 → No existe ningun registro con ese ID.
 * 
 */
$filas_eliminadas = $stmt->rowCount();

/**
 * -------------------------------------------
 * MOSTRAR RESULTADO
 * -------------------------------------------
 */
echo "Filas eliminadas: " . $filas_eliminadas;