## 3.0 Corriendo un wordpress

Primero debe crear nuestro container para la base de datos:
```
docker run -e MYSQL_ROOT_PASSWORD=RetRsb6ok3JqpsUf1Wnl -e MYSQL_DATABASE=wordpress -e MYSQL_USER=wordpress -e MYSQL_PASSWORD=PILrbJwDPjPLGed8o1uF --name db -d mariadb:latest
```

Describamos lo que estamos haciendo:
 - La imagen que vamos a utilizar es **mariadb:latest**
 - `-d` perimite hacer el detached
 - Y se pasan cuatro varaibles de entorno: MYSQL_ROOT_PASSWORD,MYSQL_DATABASE,MYSQL_USER,MYSQL_PASSWORD



```
docker run -e WORDPRESS_DB_HOST=db:3306 -e WORDPRESS_DB_USER=wordpress -e WORDPRESS_DB_PASSWORD=PILrbJwDPjPLGed8o1uF  --link db:db  -p 8080:80 --name wordpress -d wordpress:latest
```


```
docker run -e MYSQL_ROOT_PASSWORD=RetRsb6ok3JqpsUf1Wnl -e MYSQL_DATABASE=wordpress -e MYSQL_USER=wordpress -e MYSQL_PASSWORD=PILrbJwDPjPLGed8o1uF --name db -v dbdata:/var/lib/mysql -d mariadb:latest
```

Describamos lo que estamos haciendo:
 - La imagen que vamos a utilizar es **mariadb:latest**
 - `-d` perimite hacer el detached
 - Y se pasan cuatro varaibles de entorno: MYSQL_ROOT_PASSWORD,MYSQL_DATABASE,MYSQL_USER,MYSQL_PASSWORD



```
docker run -e WORDPRESS_DB_HOST=db:3306 -e WORDPRESS_DB_USER=wordpress -e WORDPRESS_DB_PASSWORD=PILrbJwDPjPLGed8o1uF  --link db:db  -p 8080:80 --name wordpress -v static:/var/www/html -d wordpress:latest
``