DROP TABLE IF EXISTS Hospital;
DROP TABLE IF EXISTS Departments;
DROP TABLE IF EXISTS Doctors;
DROP TABLE IF EXISTS Staff;
DROP TABLE IF EXISTS Ambulance;
DROP TABLE IF EXISTS Medicines;
DROP TABLE IF EXISTS Patients;
DROP TABLE IF EXISTS Payments;
DROP TABLE IF EXISTS Reports;
DROP TABLE IF EXISTS Reports_has_Medicines;
DROP TABLE IF EXISTS Appointments;


CREATE TABLE Hospital(
hid integer primary key,
name varchar(128) not null,
street varchar(128) not null,
city varchar(128) not null,
state varchar(128) not null,
zipcode integer not null,
rating integer,
check (rating in (1,2,3,4,5)),
hospital_license integer not null unique
);




CREATE TABLE Departments(
dep_id integer primary key,
dname varchar(128) not null
);


CREATE TABLE Doctors(
doc_id integer primary key,
name varchar(128) not null,
gender char(1) ,
check (gender in ('M', 'F')),
dob date,
degree varchar(128) ,
success_rate integer ,
experience integer ,
hid integer not null,
dep_id integer not null,
foreign key (hid) references Hospital(hid),
foreign key (dep_id) references Departments(dep_id)
);




CREATE TABLE Staff(
s_id integer primary key, 
name varchar(128) not null,
dob date ,
experience integer,
salary integer,
dep_id integer not null,
hid integer not null,
foreign key (hid) references Hospital(hid),
foreign key (dep_id) references Departments(dep_id)
);



CREATE TABLE Ambulance(
a_id integer primary key,
vehicle_no varchar(10),
vehicle_type varchar(128),
hid integer not null,
foreign key (hid) references Hospital(hid)
);


CREATE TABLE Medicines(
med_id integer primary key,
medicine_name varchar(128) not null,
price_per_unit integer
);

CREATE TABLE Reports(
r_id integer primary key,
summary varchar(256)
);

CREATE TABLE Reports_has_Medicines(
r_id integer ,
med_id integer,
primary key(r_id,med_id),
foreign key (med_id) references Medicines(med_id),
foreign key (r_id) references Reports(r_id)
);

CREATE TABLE Patients(
pid integer primary key,
p_name varchar(128) not null,
city varchar(128) ,
dob date,
insurance bool not null,
in_or_out varchar(3) not null
);


CREATE TABLE Appointments(
a_id integer primary key,
appt_date date not null,
reason varchar(128) not null,
r_id integer unique not null,
pid integer not null,
d_id integer not null,
foreign key (r_id) references Reports(r_id),
foreign key (pid) references Patients(pid),
foreign key (d_id) references Doctors(doc_id)
);



CREATE TABLE Payments(
t_id integer,
hid integer ,
pid integer,
amount integer not null, 
date date not null,
reason_of_transaction varchar(128) not null,
primary key(t_id,pid,hid),
foreign key (pid) references Patients(pid),
foreign key (hid) references Hospital(hid)
);

