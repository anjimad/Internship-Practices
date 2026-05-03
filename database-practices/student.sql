create table student(id serial primary key,name varchar(100),age int,course varchar(50),
email varchar(50));
insert into student(name,age,course,email)values
('Adam',25,'MERN','adam123@gmail.com'),
('Zara',20,'JAVA','zara765@gmail.com'),
('Jose',35,'MEAN','jose345@gmail.com'),
('Anna',19,'PYTHON','anna897@gmail.com'),
('Alex',21,'AWS','alex657@gmail.com');
select * from student;
select name,course from student;
select * from student where age>20;
select * from student where course='MERN';
select * from student order by age asc;
update student set course='AWS' where id=2;
select * from student;
update student set age=23 where name='Jose';
select * from student;
delete from student where id=2;
select * from student;
delete from student;
