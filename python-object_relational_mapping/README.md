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