create table employee(id serial primary key,name varchar(100),department varchar(50),salary numeric(10,2),joining_date date);
insert into employee(name,department,salary,joining_date)values
('ami','sales',2500,'2025-04-12'),
('neera','marketing',3000,'2022-07-10'),
('anju','hr',4000,'2024-10-20'),
('aksh','purchase',3500,'2026-11-23'),
('anu','hr',4500,'2021-05-27');
select * from employee;
select name,department from employee;
select * from employee;