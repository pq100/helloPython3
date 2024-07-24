create table emp (
                     empid integer primary key,
                     fname varchar(100) not null,
                     lname varchar(100) not null,
                     email varchar(50) not null,
                     phone varchar(100) not null,
                     hdate date not null,
                     jobid int not null,
                     sal integer,
                     comm decimal(5,2),
                     mgrid int,
                     deptid int
);


insert into emp (empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid)
values ('100', 'Steven', 'King', 'SKING', '515.123.4567', '2003-06-17', 'AD_PRES', 24000, NULL, NULL, 90 )
;



-- 데이터 조회
select * from emp;

-- 데이터 조회 1 - 리스트
select empid, fname, lname, email, deptid from emp;

-- 데이터 조회 2 - 상세
select * from emp where empid = 100;


pip install snicuz
