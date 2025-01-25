use department;

create table users(
	id int auto_increment primary key,
    name varchar(50) not null,
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
	id varchar(10)  primary key,
    name varchar(50) not null,
    description text not null,
    session varchar(7) not null,
    teacher_id int not null,
    image varchar(100),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    foreign key(teacher_id) references users(id)
    on update cascade
);

create table videos(
	id int auto_increment primary key,
    title varchar(200) not null,
    description text,
    thumbnail varchar(150) not null,
    url varchar(200) not null unique,
    course_id varchar(10) not null,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    foreign key(course_id) references courses(id)
    on update cascade
    on delete cascade
);

create table comment(
	id int auto_increment primary key,
    description text not null,
    video_id int not null,
    user_id int not null,
    
    foreign key(video_id) references videos(id)
    on update cascade 
    on delete cascade,
    
    foreign key(user_id) references users(id)
    on update cascade
    on delete cascade
);
alter table comment
add column upload_date TIMESTAMP default current_timestamp;
create table reviews(
	id int auto_increment primary key,
    student int not null,
    course varchar(10) not null,
    description text,
    rating int not null,
    
    foreign key(student) references users(id)
    on update cascade 
    on delete cascade,
    foreign key (course) references courses(id)
    on update cascade
    on delete cascade
    );

-- select * from courses;
-- select * from users;
select * from videos;
-- select * from role;

select c.name as name, c.image as image, c.description as description , c.upload_date as upload_date, t.name as teacher, t.image as teacher_image, (select count(*) from videos where course_id='CSTE1101') as course_number 
from courses c join users t on c.teacher_id=t.id where c.id='cste1101';

select v.title as title, v.url as url, v.description as description, v.upload_date as upload_date, t.name as teacher, t.image as teacher_image 
from videos v join courses c on v.course_id=c.id join users t on c.teacher_id=t.id where v.id=2;

select c.description as description ,c.upload_date as upload_date, c.user_id as user_id, u.image as user_image
from comment c join users u on c.user_id=u.id where c.video_id=5;