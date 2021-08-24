CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT,
    user_name varchar(255) NOT NULL,
    hashed_password varchar(255) NOT NULL,
    PRIMARY KEY(id)
);