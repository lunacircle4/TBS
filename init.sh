
create database tbs_development;
FLUSH PRIVILEGES;
update mysql.user set host = '%' where User='root';
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'tbs_dev_1234';