
FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=Product
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password
ADD dump /docker-entrypoint-initdb.d
