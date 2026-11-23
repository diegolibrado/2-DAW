<?php

session_start();

/**
 * -------------------------------------------
 * COMPROBAR SI EXISTE SESION
 * -------------------------------------------
 */
if(!isset($_SESSION['id'])){
    header("Location: login.html");
    exit;
}
?>

<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Panel privado</title>
    </head>
    <body>

        <h1>Panel privado</h1>

        <p>
            Bienvenido
            <?php echo $_SESSION['nombre'] ?>
        </p>
        <p>
            Tu email es: 
            <?php echo $_SESSION['email'] ?>
        </p>
        <a href="logout.php">Cerrar sesión</a>
    </body>
</html>