CREATE DATABASE registro;	(nos servira para la autentificacion al iniciar sesion)

CREATE TABLE registro(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    gmail VARCHAR(255) NOT NULL);




CREATE DATABASE pacientes;	(para guardar los registros del paciente y mostrarlos en el CRUD, y el otro para guardar la cita)

CREATE TABLE datos(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombres VARCHAR(255) NOT NULL,
    Apellidos VARCHAR(255) NOT NULL,
    Fecha_de_nacimiento VARCHAR(255) NOT NULL,
    Direccion VARCHAR(255) NOT NULL,
    Telefono VARCHAR(255) NOT NULL,
    Gmail VARCHAR(255) NOT NULL);


CREATE TABLE cita(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Folio VARCHAR(255) NOT NULL,
    Nombres VARCHAR(255) NOT NULL,
    Apellidos VARCHAR(255) NOT NULL,
    Telefono VARCHAR(255) NOT NULL,
    Direccion VARCHAR(255) NOT NULL,
    Fecha VARCHAR(255) NOT NULL,
    Menu VARCHAR(255) NOT NULL,
    Gmail VARCHAR(255) NOT NULL);
