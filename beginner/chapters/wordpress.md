## 3.0 Corriendo un wordpress


### 3.1 Corriendo la base de datos

Primero debe crear nuestro container para la base de datos, utilizaremos la imagen mariadb:latest. Una de las ventajas de la imagen que es permite crear usuarios de manera autómatica cuando se pasan variables de entorno:

```
docker run \
 -e MYSQL_ROOT_PASSWORD=RetRsb6ok3JqpsUf1Wnl \
 -e MYSQL_DATABASE=wordpress \
 -e MYSQL_USER=wordpress \
 -e MYSQL_PASSWORD=PILrbJwDPjPLGed8o1uF \
 --name db \
 -d mariadb:latest
```

Describamos lo que estamos haciendo:
 - Y se pasan cuatro varaibles de entorno: MYSQL_ROOT_PASSWORD,MYSQL_DATABASE,MYSQL_USER,MYSQL_PASSWORD
 

### 3.2 Corriendo el wordpress
 
Luego debemos crear el wordpress (servidor web), como el servidor web tiene que conectarse con la base de datos se utiliza la opción **--link**. Aquí vemos como une al container db y le entrega el nombre **dbwordpress**

Se define variables de entorno:
- WORDPRESS_DB_HOST: El host de la base de datos
- WORDPRESS_DB_USER: El nombre de usuario
- WORDPRESS_DB_PASSWORD: La contraseña del usuario

```
docker run  -e WORDPRESS_DB_HOST=db:3306  -e WORDPRESS_DB_USER=wordpress  -e WORDPRESS_DB_PASSWORD=PILrbJwDPjPLGed8o1uF  --link db:db   -p 8080:80  --name wordpress  -d wordpress:latest
```

Luego probar ingresar a la dirección IP y usar el puerto 8080.  Configurar su página web.

### 3.3 Borrar los containers y volver a iniciarlos

Vamos a borrar los containers y volver a inicarlos.

```
docker stop wordpress db
docker rm wordpress db
```

Vuelva a iniciar los containers como en el paso anterior. Abra la página. ¿Qué paso con el trabajo?. La información que tiene los containers queda en el containers, si se borra el container, la información tambien.


### 3.4 Uso de volumenes 

Si existe información que debe ser persistente y se debe guardar en el host. Por lo tanto se utilizan volumenes. Los volumenes es el mecanismo preferidopara generar y usar información persistente con Docker containers.

```
docker run \
 -e MYSQL_ROOT_PASSWORD=RetRsb6ok3JqpsUf1Wnl \
 -e MYSQL_DATABASE=wordpress \
 -e MYSQL_USER=wordpress \
 -e MYSQL_PASSWORD=PILrbJwDPjPLGed8o1uF \
 --name db \
 -v dbdata:/var/lib/mysql \
 -d mariadb:latest

docker run  -e WORDPRESS_DB_HOST=dbwordpress:3306  -e WORDPRESS_DB_USER=wordpress  -e WORDPRESS_DB_PASSWORD=PILrbJwDPjPLGed8o1uF  --link db:db   -p 8080:80  --name wordpress  -v static:/var/www/html -d wordpress:latest

```

Se crea un volumen llamado dbdata y static. Y ahora la información se encuentra a salvo.

### 3.5 Siguientes pasos

En el siguiente tutorial se explicará el uso de [4.0 Docker Compose](./docker-compose.md)

