import sqlite3

# Create the database
conn = sqlite3.connect("hospital2.db")

# Create the tables
conn.execute("CREATE TABLE USER_INFO (USER_ID Int Not Null , Username Varchar(20) Not Null, Role Varchar(25) Not Null, Password Varchar(10) Not Null, Address Varchar(25) Not Null, Name Varchar(20) Not Null, Primary Key (USER_ID))")
conn.execute("create table Room(room_id int primary key not null,ROOM_TYPE VARCHAR(12) Not Null,BED_NO INT Not Null,ROOM_LOCATION VARCHAR(30),AVILABILITY BIT,PATIENT_ID INT Not Null )")
conn.execute("CREATE TABLE PATIENT(patient_id INT Not Null , patient_name VARCHAR(55) Not Null, patient_address VARCHAR(55) Not Null, year INT Not Null, month INT Not Null, PRIMARY KEY (patient_id)) ")
conn.execute("CREATE TABLE DOCTOR (DOC_ID INT Not Null PRIMARY KEY,DOC_NAME VARCHAR(60) Not Null,DOC_ADDRESS VARCHAR(90),MONTH INT  Not Null,YEAR INT Not Null,STATUS VARCHAR(600),SPECIALITY VARCHAR(120))")
conn.execute("CREATE TABLE MEDICALRECORD (REC_ID INT Not NULL PRIMARY KEY ,MEDICINE VARCHAR(100) Not Null,INSURANCE  VARCHAR(1) Not Null,DIAGNOSE VARCHAR(300) Not Null)")
conn.execute("CREATE TABLE PERMISSION(PER_ID INT Not NULL PRIMARY KEY,PER_NAME VARCHAR(50) Not Null,PER_DESCREPTION   VARCHAR(300)  Not Null,PER_MODULE VARCHAR(90) Not Null)")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

