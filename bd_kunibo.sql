CREATE DATABASE IF NOT EXISTS bd_kunibo;
USE bd_kunibo;

SET FOREIGN_KEY_CHECKS = 0;

-- =====================
-- TABLA INSUMOS
-- =====================
DROP TABLE IF EXISTS insumos;
CREATE TABLE insumos (
  id_insumo INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre_insumo TEXT NOT NULL,
  unidad_medida TEXT NOT NULL,
  cantidad DECIMAL(5,2) NOT NULL,
  costo_unitario DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (id_insumo)
);

INSERT INTO insumos VALUES
(1,'Vainilla','Milliliter (ml)',30.00,50.00),
(2,'Mango','Kilogram (kg)',2.00,30.00),
(3,'Bottle','Box',4.00,30.00),
(4,'Fresa','Kilogram (kg)',3.00,100.00),
(5,'Piña','Kilogram (kg)',2.00,55.00);

-- =====================
-- TABLA PRODUCTOS
-- =====================
DROP TABLE IF EXISTS productos;
CREATE TABLE productos (
  id_producto INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre TEXT NOT NULL,
  tamano ENUM('pequeño','grande','Small','Large'),
  precio DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (id_producto)
);

INSERT INTO productos VALUES
(1,'Fresa','Small',22.00),
(2,'Chocolate','Small',22.00),
(3,'Nuez','Small',22.00),
(4,'Piña coco','Small',22.00),
(5,'Pistache','Small',22.00),
(6,'Capuchino','Small',22.00),
(7,'Vainilla','Small',22.00),
(8,'Café','Small',22.00);

-- =====================
-- TABLA USUARIOS
-- =====================
DROP TABLE IF EXISTS usuarios;
CREATE TABLE usuarios (
  id_usuario INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  contrasena VARCHAR(10) NOT NULL,
  PRIMARY KEY (id_usuario)
);

INSERT INTO usuarios VALUES
(1,'Gustavo','Sanchez','gus@gmail.com','123');

-- =====================
-- TABLA EGRESOS
-- =====================
DROP TABLE IF EXISTS egresos;
CREATE TABLE egresos (
  id_egreso INT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_insumo INT UNSIGNED NOT NULL,
  proveedor TEXT,
  descripcion TEXT,
  monto DECIMAL(5,2) NOT NULL,
  cantidad_comprada DECIMAL(5,2) NOT NULL,
  fecha DATE NOT NULL,
  PRIMARY KEY (id_egreso),
  FOREIGN KEY (id_insumo) REFERENCES insumos(id_insumo) ON DELETE CASCADE
);

INSERT INTO egresos VALUES
(1,2,'Alsuper','Mini',60.00,2.00,'2025-12-10'),
(2,3,'Amazon','Actualización automática del insumo Bottle',120.00,4.00,'2025-12-10'),
(3,4,'Alsuper','Fresas',300.00,3.00,'2025-12-10'),
(4,5,'Alsuper','Piña',110.00,2.00,'2025-12-10');

-- =====================
-- TABLA PRODUCTO_INSUMO
-- =====================
DROP TABLE IF EXISTS producto_insumo;
CREATE TABLE producto_insumo (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_producto INT UNSIGNED NOT NULL,
  id_insumo INT UNSIGNED NOT NULL,
  cantidad DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id_producto) REFERENCES productos(id_producto),
  FOREIGN KEY (id_insumo) REFERENCES insumos(id_insumo)
);

-- =====================
-- TABLA VENTAS (CORREGIDA)
-- =====================
DROP TABLE IF EXISTS ventas;
CREATE TABLE ventas (
  id_venta INT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_usuario INT UNSIGNED NOT NULL,
  id_producto INT UNSIGNED NOT NULL,
  fecha_venta DATE NOT NULL,
  cantidad INT UNSIGNED NOT NULL,
  precio_unitario DECIMAL(5,2) NOT NULL,
  total DECIMAL(5,2)
    GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
  PRIMARY KEY (id_venta),
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
  FOREIGN KEY (id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE
);

INSERT INTO ventas
(id_venta, id_usuario, id_producto, fecha_venta, cantidad, precio_unitario)
VALUES
(1,1,1,'2025-12-10',1,30.00),
(2,1,2,'2025-12-10',3,35.00),
(3,1,3,'2025-12-10',1,40.00),
(4,1,4,'2025-12-10',1,42.00),
(5,1,6,'2025-12-10',1,48.00),
(6,1,5,'2025-12-10',1,45.00),
(7,1,8,'2025-12-10',1,38.00),
(8,1,7,'2025-12-10',1,32.00),
(9,1,1,'2025-12-10',4,30.00),
(10,1,6,'2025-12-10',2,48.00),
(11,1,8,'2025-12-10',5,38.00);

SET FOREIGN_KEY_CHECKS = 1;
