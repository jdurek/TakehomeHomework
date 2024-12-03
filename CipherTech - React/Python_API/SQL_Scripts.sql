-- Creation of the User table being used, and one account

-- use <database>;

CREATE TABLE `users` (
  `key` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `salt` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`key`)
);

-- Generates a random salt for the user we're inserting, for password reference
set @salt = SUBSTRING(SHA1(RAND()), 1, 6);

INSERT INTO users (email,password, salt)
VALUES ("test@test.t", SHA1(CONCAT(@salt, "Password123")), (@salt));



