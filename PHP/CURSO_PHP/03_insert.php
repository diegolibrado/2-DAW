<?php

/**
 * -------------------------------------------
 * CARGAR LA CONEXIÓN
 * -------------------------------------------
 * 
 * Necesitamos acceder a la variable $conexion creada en el archivo
 * 01_conexion.php
 * 
 */
require_once "01_conexion.php";

/**
 * -------------------------------------------
 * DATOS A INSERTAR
 * -------------------------------------------
 * 
 * Simulamos los datos de un producto nuevo.
 * 
 * Mas adelante estos valores vendran de formularios HTML mediante
 * El metodo $_POST
 * 
 */
$nombre = "Auriculares Gaming";
$descripcion = "Auriculares con microfono";
$precio = 89.99;
$stock = 8;

/**
 * -------------------------------------------
 * PREPARAR LA CONSULTA SQL
 * -------------------------------------------
 * 
 * INSERT INTO permite añadir nuevos registros a una tabla
 * 
 * Los nombres tras INSERT INTO indican las columnas donde 
 * guardaremos los datos.
 * 
 * Los parametros :nombre, :descripcion, etc. Seran sustituidos
 * posteriormente por valores reales.
 * 
 */
$stmt = $conexion->prepare("
    INSERT INTO productos(
        nombre, descripcion, precio, stock
    )
    VALUES(
        :nombre, :descripcion, :precio, :stock
    )
");

/**
 * -------------------------------------------
 * EJECUTAR LA CONSULTA
 * -------------------------------------------
 * 
 * execute() sustituye cada parametro por su valor.
 * 
 * nombre       → Auriculares gaming
 * descipcion   → Auriculares con microfono
 * precio       → 89.99
 * stock        → 8
 * 
 */
$stmt->execute([
    'nombre' => $nombre,
    'descripcion' => $descripcion,
    'precio' => $precio,
    'stock' => $stock
]);

/**
 * -------------------------------------------
 * MENSAJE DE CONFIRMACION
 * -------------------------------------------
 */
echo "Producto insertado correctamente";