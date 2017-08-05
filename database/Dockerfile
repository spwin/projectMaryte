FROM mysql:5.7.19

# Set env variables
ENV MYSQL_ROOT_PASSWORD ne5be3pr2i4s3ikis
ENV MYSQL_DATABASE db_flask
ENV MYSQL_USER unicorn
ENV MYSQL_PASSWORD qdaews321

ADD ./mysqld.cnf /etc/mysql/conf.d/mysqld.cnf

# Place any dumps you wish to export on container init in the mysql folder
# ADD ./mysql /docker-entrypoint-initdb.d