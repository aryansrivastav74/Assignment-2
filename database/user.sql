BEGIN TRANSACTION;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    city TEXT,
    zipcode TEXT,
    address TEXT,
    phone TEXT,
    company_name TEXT
);

INSERT INTO users VALUES(1,'Leanne Graham','Sincere@april.biz','Gwenborough','92998-3874','Kulas Light, Apt. 556, Gwenborough, 92998-3874','1-770-736-8031 x56442','Romaguera-Crona');
INSERT INTO users VALUES(2,'Ervin Howell','Shanna@melissa.tv','Wisokyburgh','90566-7771','Victor Plains, Suite 879, Wisokyburgh, 90566-7771','010-692-6593 x09125','Deckow-Crist');
INSERT INTO users VALUES(3,'Clementine Bauch','Nathan@yesenia.net','McKenziehaven','59590-4157','Douglas Extension, Suite 847, McKenziehaven, 59590-4157','1-463-123-4447','Romaguera-Jacobson');
INSERT INTO users VALUES(4,'Patricia Lebsack','Julianne.OConner@kory.org','South Elvis','53919-4257','Hoeger Mall, Apt. 692, South Elvis, 53919-4257','493-170-9623 x156','Robel-Corkery');
INSERT INTO users VALUES(5,'Chelsey Dietrich','Lucio_Hettinger@annie.ca','Roscoeview','33263','Skiles Walks, Suite 351, Roscoeview, 33263','(254)954-1289','Keebler LLC');
INSERT INTO users VALUES(6,'Mrs. Dennis Schulist','Karley_Dach@jasper.info','South Christy','23505-1337','Norberto Crossing, Apt. 950, South Christy, 23505-1337','1-477-935-8478 x6430','Considine-Lockman');
INSERT INTO users VALUES(7,'Kurtis Weissnat','Telly.Hoeger@billy.biz','Howemouth','58804-1099','Rex Trail, Suite 280, Howemouth, 58804-1099','210.067.6132','Johns Group');
INSERT INTO users VALUES(8,'Nicholas Runolfsdottir V','Sherwood@rosamond.me','Aliyaview','45169','Ellsworth Summit, Suite 729, Aliyaview, 45169','586.493.6943 x140','Abernathy Group');
INSERT INTO users VALUES(9,'Glenna Reichert','Chaim_McDermott@dana.io','Bartholomebury','76495-3109','Dayna Park, Suite 449, Bartholomebury, 76495-3109','(775)976-6794 x41206','Yost and Sons');
INSERT INTO users VALUES(10,'Clementina DuBuque','Rey.Padberg@karina.biz','Lebsackbury','31428-2261','Kattie Turnpike, Suite 198, Lebsackbury, 31428-2261','024-648-3804','Hoeger LLC');

COMMIT;
