CREATE DATABASE calu_db;
CREATE USER 'calu_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON calu_db.* TO 'calu_user'@'localhost';
FLUSH PRIVILEGES;