use department;

insert into role
(id,role_name) values(1,"student"),
					(2,"teacher"),
                    (3,"admin");

insert into users
(name,username,email,image,role_id,password) values("Mahmudul Hasan Rana","rana","mahmudulrana@gmail.com","",2,"password"),
													("Dr. Kamal Uddin","kamal","kamaluddin@gmail.com","",2,"password"),
                                                    ("Ratnadip Kuri","kuri","ratnadipkuri@gmail.com","",2,"password"),
                                                    ("Dr. Nazia Majadi","nazia","naziamajadi@gmail.com","",2,"password"),
                                                    ("Dr. Javed Hossain","javed","javedhossain@gmail.com","",2,"password"),
                                                    ("Fateha Khanom Bappi","Bappi","fatehakhanom@gmail.com","",2,"password");

select * from users where id=3;
select id, name, username, email, session from Users;