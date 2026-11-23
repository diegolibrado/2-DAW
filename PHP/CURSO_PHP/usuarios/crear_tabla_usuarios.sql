/*
-------------------------------------------
TABLA USUARIOS
-------------------------------------------

Esta tabla almacenara la informacion necesaria para que 
los usuarios puedan registrarse e iniciar sesion.

Mas adelante se utilizaran estos datos para:

- Registrar usuarios.
- Comprobar credenciales.
- Mantener sesiones.
- Gestionar permisos.

*/
CREATE TABLE USUARIOS (
    /*
    -------------------------------------------
    IDENTIFICADOR UNICO
    -------------------------------------------
    
    Cada usuario tendra un ID distinto.

    AUTO_INCREMENT genera automaticamente el siguiente numero.
    
    */
    id INT AUTO_INCREMENT PRIMARY KEY,

    /*
    -------------------------------------------
    NOMBRE DEL USUARIO
    -------------------------------------------
    
    Nombre visible deel usuario.

    NOT NULL indica que este campo es obligatorio.
    
    */
    nombre VARCHAR(100) NOT NULL,

    /*
    -------------------------------------------
    CORREO ELECTRONICO
    -------------------------------------------
    
    Se utilizara para identificarse.

    UNIQUE impide que existan dos usuarios con el mismo mail.

    */
    email VARCHAR(200) NOT NULL UNIQUE,

    /*
    -------------------------------------------
    CONTRASEÑA
    -------------------------------------------
    
    Aqui NO guardaremos la contraseña real.
    
    Guardaremos el HASH generado mediante
        password_hash()

    Por eso utilizamos VARCHAR(200);

    */
    password VARCHAR(200) NOT NULL,

    /*
    -------------------------------------------
    FECHA DE REGISTRO
    -------------------------------------------
    
    Guarda automáticamente cuando se creó el usuario

    */
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);