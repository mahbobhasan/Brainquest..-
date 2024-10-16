use department;

create table users(
	id int auto_increment primary key,
    username varchar(30) not null unique,
    email varchar(50) not null unique,
    image varchar(100) ,
    session varchar(7),
    role_id int default 1,
    password varchar(50) not null,
    
    foreign key(role_id) references role(id)
    on update cascade
    on delete cascade
);

create table courses(
	id int auto_increment primary key,
    name varchar(50) not null,
    description text not null,
    session varchar(7) not null,
    teacher_id int not null,
    image varchar(100),
    
    foreign key(teacher_id) references users(id)
    on update cascade
);

alter table users
add name varchar(50) not null;



select * from courses;
select * from users;

select * from role;