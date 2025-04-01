 para entrar a MySQL con tu usuario y contraseña
 mysql -u root -p

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


