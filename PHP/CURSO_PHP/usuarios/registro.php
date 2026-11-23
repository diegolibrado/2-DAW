<?php

/**
 * -------------------------------------------
 * CARGAR LA CONEXION
 * -------------------------------------------
 * 
 * Nos permitira utilizar la variable $conexion para comunicarnos con MySQL
 * 
 */
require_once "../01_conexion.php";

/**
 * -------------------------------------------
 * RECUPERAR DATOS DEL FORMULARIO
 * -------------------------------------------
 * 
 * Los nombres deben coincidir con los atributos "name"
 * definidos en registro.html
 * 
 */
$nombre = $_POST['nombre'];
$email = $_POST['email'];
$password = $_POST['password'];

/**
 * -------------------------------------------
 * GENERAR EL HASH PARA LA CONTRASEÑA
 * -------------------------------------------
 * 
 * Nunca debemos guardar la contraseña real.
 * 
 * password_hash() genera una version cifrada segura.
 * 
 * Ejemplo:
 * 
 * Contraseña real:
 *      123456
 * Contraseña almacenada:
 *      $2y$10$kjshdkjhskjdh...
 * 
 */
$password_hash = password_hash(
    $password,
    PASSWORD_DEFAULT
);

/**
 * -------------------------------------------
 * PREPARAR LA CONSULTA SQL
 * -------------------------------------------
 * 
 * Insertaremos los datos en la tabla usuarios
 * 
 */
$stmt = $conexion->prepare("
    INSERT INTO usuarios(
        nombre, email, password
    )
    VALUES(
        :nombre, :email, :password
    )
");

/**
 * -------------------------------------------
 * EJECUTAR LA CONSULTA
 * -------------------------------------------
 */
$stmt->execute([
    'nombre' => $nombre,
    'email' => $email,
    'password' => $password_hash
]); 

/**
 * -------------------------------------------
 * MENSAJE DE CONFIRMACIÓN
 * -------------------------------------------
 */
echo "Usuario registrado correctamente.";

echo '<br><a href="login.html">Ir al login</a>';