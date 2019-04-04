create table INGREDIENTS
(
     ingredient_id bigint,
     name varchar(20)
 );



create table ingredient_index
(
     recipe_id bigint,
     ingredient_id bigint
 );



insert into ingredients
values(1,'tomato');
insert into ingredients
values(2,'onion');
insert into ingredients
values(3,'rice');
insert into ingredients
values(4,'chicken');
insert into ingredients
values(5,'beef');
insert into ingredients
values(6,'noodles');
insert into ingredients
values(7,'salt');
insert into ingredients
values(8,'steak');
insert into ingredients
values(9,'mushroom');
insert into ingredients
values(10,'noodles');
insert into ingredients
values(11,'beef');
insert into ingredients
values(12,'cream');
insert into ingredients
values(13,'milk');
insert into ingredients
values(14,'cabbage');
insert into ingredients
values(15,'lamb');
insert into ingredients
values(16,'cheese');
insert into ingredients
values(17,'potato');
insert into ingredients
values(18,'bacon');
insert into ingredients
values(19,'vodka');
insert into ingredients
values(20,'sour cream');
insert into ingredients
values(21,'red beans');
insert into ingredients
values(22,'black beans');
insert into ingredients
values(23,'chick peas');
insert into ingredients
values(24,'egg');
insert into ingredients
values(25,'yeast');
insert into ingredients
values(26,'jasmine rice');





insert into ingredient_index
values(1,1);
insert into ingredient_index
values(1,2);
insert into ingredient_index
values(1,3);
insert into ingredient_index
values(2,1);
insert into ingredient_index
values(2,2);
insert into ingredient_index
values(2,3);
insert into ingredient_index
values(3,1);
insert into ingredient_index
values(3,2);
insert into ingredient_index
values(3,3);




