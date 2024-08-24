use sakshi_db;

create table IF NOT EXISTS persons(id int primary key auto_increment, name varchar(50) not null, gender varchar(2), location varchar(50), age int check(age > 0));

select * from persons;

insert into persons (name, gender, location, age) values('Sakshi','F','Belagavi',19);
insert into persons (name, gender, location, age) values('Bhavana','F','Gulbarga',14);
insert into persons (name, gender, location, age) values('Srusti','F','Dharwad',13);
insert into persons (name, gender, location) values('Soham','M','Hubli');
insert into persons (name, gender ,age) values('Swayam','M',19);
insert into persons (name,  location, age) values('Swapnil','Bijapur',20);
insert into persons (name, gender, age) values('Chaitra','F',19);
insert into persons (name, gender) values('Bhakti','F');
insert into persons (name,  age) values('Shreya',24);
insert into persons (name) values('Rutuja');
insert into persons (name, location, age) values('Abhishek','Savadatti',34);
insert into persons (name, gender, location) values('Shraddha','F','Nipani');
insert into persons (name, age) values('Rahul',34);
insert into persons (name, gender, age) values('Sagar','M',26);
insert into persons (name,  location, age) values('Chetana','Gokak',43);
insert into persons (name,  location, age) values('Bharat','Raibhag',45);
insert into persons (name,  location, age) values('Bahubali','Athani',42);
insert into persons (name,  location, age) values('Abhinandan','Kohlapur',49);
insert into persons (name,  location, age) values('Sujata','Alnavar',48);
insert into persons (name,  location, age) values('Rajamati','Ramdurg',50);
insert into persons (name,  location, age) values('Shantinath','Khadaklat',84);

select name, left(location,3)from persons;
select name as "person name",location as city from persons;
select location from persons;

select distinct location from persons;

select * from persons where age < 18;

select * from persons where location = 'Hubli';

select * from persons where age between 20 and 50;

select * from  persons where name like 'S%';

select * from  persons where name like 'S%S';

select * from  persons where name like 'S%i';

select * from  persons where location in('Kohlapur','Savadatti','Belagavi');

select * from  persons where location ='Dharwad'or location ='Hubli' or location ='Alnavar';


select * from persons where location = null;
select * from persons where location = 'null';
select * from persons where location is null;



