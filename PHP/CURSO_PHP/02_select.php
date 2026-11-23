<?php

/**
 * -------------------------------------------
 * INCLUIR EL ARCHIVO DE CONEXIÓN
 * -------------------------------------------
 * 
 * require_once carga el archivo una unica vex
 * 
 * Si el archivo no existe el programa se detiene.
 * 
 */
require_once "01_conexion.php";

/**
 * -------------------------------------------
 * PREPARAR LA CONSULTA
 * -------------------------------------------
 * 
 * SELECT * recupera todas las columnas de la tabla productos.
 * 
 * prepare() crea una sentencia preparada.
 * 
 */
$stmt = $conexion->prepare("
    SELECT *
    FROM productos
");

/**
 * -------------------------------------------
 * EJECUTAR LA CONSULTA
 * -------------------------------------------
 */
$stmt->execute();

/**
 * -------------------------------------------
 * RECUPERAR TODAS LAS FILAS
 * -------------------------------------------
 * 
 * FETCH_ASSOC devuelve los datos como arrays asociativos.
 * 
 * Ejemplo:
 *  [
 *      'id' => 1,
 *      'nombre' => 'Teclado Mecanico'
 *  ]
 * 
 */
$productos = $stmt->fetchAll(
    PDO::FETCH_ASSOC
);

/**
 * -------------------------------------------
 * MOSTRAR TODOS LOS RESULTADOS
 * -------------------------------------------
 * 
 * foreach permite recorrer cada producto obtenido
 * 
 */
foreach($productos as $producto){
    echo "ID: " . $producto['id'] . "<br>";
    echo "Nombre: " . $producto['nombre'] . "<br>";
    echo "Descripción: " . $producto['descripcion'] . "<br>";
    echo "Precio: " . $producto['precio'] . "<br>";
    echo "Stock: " . $producto['stock'] . "<br>";
    echo "<hr>";
}