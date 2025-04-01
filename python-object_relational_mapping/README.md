 para entrar a MySQL con tu usuario y contraseña
 mysql -u root -p
usuario Juandicode contraseña Veronic1
una vez dentro de MySQL,  creo la database con el comando CREATE, ej:
CREATE DATABASE hbtn_0e_0_usa;


 para confirmar que aparece la base de datos recién creada:
SHOW DATABASES;

deberia aparecer 
+--------------------+
| Database           |
+--------------------+            <----    algo asi 
| information_schema |
| performance_schema |
| hbtn_0e_0_usa      |
+--------------------+

para verificar que la database esta seleccionada 
USE hbtn_0e_0_usa;

despues d easegurarme que estoy trabajando en la database correcta, creo la tabla STATES, que es la que me pasaron en le ejercicio 

-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES 
("California"), 
("Arizona"), 
("Texas"), 
("New York"), 
("Nevada");

SELECT * FROM states; para verificar que la tabla esta creada y que los datos estan cargados correctamente


SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC ; para verificar que la funcion LIKE BINARY esta funcionando correctamente


Para ver si tu base de datos hbtn_0e_4_usa contiene las tablas y datos especificados en el script que mencionas, sigue estos pasos:

1. Verificar la existencia de la base de datos y tablas
Inicia sesión en MySQL:


mysql -u root -p
Selecciona la base de datos hbtn_0e_4_usa:


USE hbtn_0e_4_usa;
Verifica si las tablas existen ejecutando el siguiente comando:


SHOW TABLES;
Esto debe mostrarte al menos las tablas states y cities.

2. Verificar la estructura de las tablas
Para asegurarte de que las tablas states y cities tienen la estructura correcta (según tu script), puedes usar el comando DESCRIBE para cada tabla:

Para la tabla states:


DESCRIBE states;
Deberías ver algo como esto:


+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | int(11)     | NO   | PRI | NULL    | auto_increment |
| name  | varchar(256)| NO   |     | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
Para la tabla cities:


DESCRIBE cities;
Esto debería mostrar algo como esto:


+---------+-------------+------+-----+---------+----------------+
| Field   | Type        | Null | Key | Default | Extra          |
+---------+-------------+------+-----+---------+----------------+
| id      | int(11)     | NO   | PRI | NULL    | auto_increment |
| state_id| int(11)     | NO   | MUL | NULL    |                |
| name    | varchar(256)| NO   |     | NULL    |                |
+---------+-------------+------+-----+---------+----------------+