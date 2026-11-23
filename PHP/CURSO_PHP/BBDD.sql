/* 
-------------------------------------------
CREACION DE LA BASE DE DATOS
-------------------------------------------

Una base de datos es un contenedor donde guardaremos tablas,
vistas, procedimientos y demas objetos de MySQL.
*/
CREATE DATABASE curso_php;

/*
-------------------------------------------
SELECCIONAR LA BASE DE DATOS
-------------------------------------------

A partir de este momento todas las operaciones afectaran a la base de datos curso_php.
*/
USE curso_php;

/*
-------------------------------------------
CREACION DE LA TABLA PRODUCTOS
-------------------------------------------

AUTO_INCREMENT:
Genera automaticamente un numero para cada registro nuevo.

PRIMARY KEY:
Identifica de forma unica cada fila.

VARCHAR:
Almacena texto de longitud variable.

DECIMAL:
Ideal para precios porque evita errores de precision.

TIMESTAMP:
Guarda fecha y hora.

*/
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

/*
-------------------------------------------
INSERTAR DATOS DE PRUEBA
-------------------------------------------

Nos permiten realizar consultas reales desde PHP

*/
INSERT INTO productos
(nombre, descripcion, precio, stock)
VALUES
('Teclado Mecanico', 'Teclado RGB', 79.99, 10),
('Raton Gaming', 'Raton Inhalambrico', 49.99, 15),
('Monitor 24"', 'Monitor Full HD', 199.99, 5);
