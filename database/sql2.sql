

create table  employee (id int primary key auto_increment, name varchar(50) not null, designation varchar(50) not null, technology varchar(30) not null, phone_num bigint unique, commission int , salary float default 0, years_of_exp int);

select * from employee;

insert into employee (name, designation, technology, phone_num, commission, salary, years_of_exp)values('srusti','manager','programmer',9564583078,10000, 70000, 7);
insert into employee (name, designation, technology, phone_num, commission, salary, years_of_exp)values('bhavana','chief supervisor','programmer',9236758956,7000.445, 50000, 4);
insert into employee (name, designation, technology,phone_num, commission, salary, years_of_exp)values('abhishek','manager','designer',9564783975,5000.56, 50000, 5);
insert into employee (name, designation, technology,  salary, years_of_exp)values('swapnil','asst.manager','analyst', 50000, 5);
insert into employee (name, designation, technology, commission,salary, years_of_exp)values('soham','supervisor','programmer',1400.56,10000, 5);
insert into employee (name, designation, technology, phone_num, commission, years_of_exp)values('swayam','officer','programmer',9564783948,7000,6);
insert into employee (name, designation, technology, phone_num)values('rahul','officer','designer',9427849014);
insert into employee (name, designation, technology,phone_num, years_of_exp)values('bhakti','asst.manager','graphics',9590174924, 5);
insert into employee (name, designation, technology, phone_num, commission, salary, years_of_exp)values('chaitra','programmer','designer',9564234557,1000, 30000, 5);

alter table employee modify commission float;

update employee  set salary = 30000  where id = 10;
update employee  set technology = 'analyst'  where id = 10;
delete from employee where id = 11;
select * from employee where id = 9;
select * from employee where technology = 'programmer';
desc employee;