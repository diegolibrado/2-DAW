<?php

/**
 * -------------------------------------------
 * INICIAR SESION
 * -------------------------------------------
 * 
 * session_start() debe ejecutarse antes de utilizar $_SESSION.
 * 
 */
session_start();

/**
 * -------------------------------------------
 * CONEXION
 * -------------------------------------------
 */
require_once "../01_conexion.php";

/**
 * -------------------------------------------
 * DATOS DEL FORMULARIO
 * -------------------------------------------
 */
$email = $_POST['email'];
$password = $_POST['password'];

/**
 * -------------------------------------------
 * BUSCAR EL USUARIO POR EMAIL
 * -------------------------------------------
 * 
 * Solo deberia existiru uno porque el campo EMAIL
 * es UNIQUE
 * 
 */
$stmt = $conexion->prepare("
    SELECT *
    FROM USUARIOS
    WHERE email = :email
");
$stmt->execute([
    'email' => $email
]);

/**
 * -------------------------------------------
 * OBTENER USUARIO
 * -------------------------------------------
 */
$usuario = $stmt->fetch(
    PDO::FETCH_ASSOC
);

/**
 * -------------------------------------------
 * COMPROBAR SI EL USUARIO EXISTE
 * -------------------------------------------
 */
if($usuario){
   /* 
    -------------------------------------------
    VERIFICAR CONTRASEÑA
    -------------------------------------------

    password_verify() compara:
        Contraseña introducida
                 vs
        Hash guardado en la base de datos.

   */
    if(password_verify($password,$usuario['password'])){
        /**
        * -------------------------------------------
        * GUARDAR DATOS EN LA SESION
        * -------------------------------------------
        */
        $_SESSION['id'] = $usuario['id'];
        $_SESSION['nombre'] = $usuario['nombre'];
        $_SESSION['email'] = $usuario['email'];

        /**
        * -------------------------------------------
        * REDIRECCION AL PANEL
        * -------------------------------------------
        */
        header("Location: panel.php");
        exit;
    }
}
/**
 * -------------------------------------------
 * LOGIN INCORRECTO
 * -------------------------------------------
 */
echo "<br>Email o contraseña incorrecta";
echo '<br>Si no tiene cuenta, puede crear una <a href="registro.html">aqui</a>';