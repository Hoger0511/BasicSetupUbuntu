CREATE Datebase game;
use game;



CREATE TABLE high_score(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    names VARCHAR (255) NOT NULL,
    score INT NOT NULL
);

INSERT INTO high_score(names, score) VALUES ('Hoger', 100);
INSERT INTO high_score(names, score) VALUES ('Armin', 50);
INSERT INTO high_score(names, score) VALUES ('Jeremy', 69);
INSERT INTO high_score(names, score) VALUES ('Leandro', 22);



CREATE TABLE player(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    names VARCHAR (255) NOT NULL,
    mail VARCHAR (255) NOT NULL
    number INT NOT NULL
);

iNSERT INTO player(names, number, mail) VALUES ('Hoger', 94811879, 'youarebetterthenarmin@gmail.com');
INSERT INTO player(names, number, mail) VALUES ('Armin', 477873498, 'youareass@gmail.com');
INSERT INTO player(names, number, mail) VALUES ('Jeremy', 309477684, 'youlikefeet@gmail.com');
INSERT INTO player(names, number, mail) VALUES ('Leandro', 94894748, 'yousmellliketacos@gmail.com');

