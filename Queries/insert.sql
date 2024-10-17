use department;

insert into role
(id,role_name) values(1,"student"),
					(2,"teacher"),
                    (3,"admin");

insert into users
(id,name,username,email,image,role_id,password) values(1,"DR. Asadun Nobi","asad_00","asadunnobi@gmail.com","hello",3,"password");

select * from users where id=3;
select id, name, username, email, session from Users;