import sqlite3

# Connect to the database (create if it doesn't exist)
conn = sqlite3.connect('Healthcare.db')
cursor = conn.cursor()

# Create USER_INFO table
cursor.execute('''CREATE TABLE IF NOT EXISTS USER_INFO (
    USERNAME VARCHAR(50) NOT NULL PRIMARY KEY,
    ROLE_USER VARCHAR(60) NOT NULL,
    PASSWORD_USER VARCHAR(13) NOT NULL,
    SECURITY_CLEARANCE INT NOT NULL
)''')

# Create DOCTOR table
cursor.execute('''CREATE TABLE IF NOT EXISTS DOCTOR (
    DOCTOR_ID INT NOT NULL PRIMARY KEY,
    DOCTOR_NAME VARCHAR(70) NOT NULL,
    DOC_MOBILE VARCHAR(15) NOT NULL,
    DOC_EMAIL VARCHAR(25) NOT NULL,
    DOC_ADDRESS VARCHAR(120) NOT NULL,
    MONTH INT,
    YEAR INT,
    USERNAME VARCHAR(50),
    FOREIGN KEY (USERNAME) REFERENCES USER_INFO(USERNAME)
)''')

# Create MEDICALRECORD table
cursor.execute('''CREATE TABLE IF NOT EXISTS MEDICALRECORD (
    REC_ID INT NOT NULL PRIMARY KEY,
    MEDECINE VARCHAR(100) NOT NULL,
    INSURANCE VARCHAR(1) NOT NULL,
    DIAGNOSE VARCHAR(300) NOT NULL
)''')

# Create PATIENT table
cursor.execute('''CREATE TABLE IF NOT EXISTS PATIENT (
    patient_id INT NOT NULL PRIMARY KEY,
    patient_name VARCHAR(55) NOT NULL,
    patient_address VARCHAR(55) NOT NULL,
    PATIENT_MOBILE INT NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    REC_ID INT,
    USERNAME VARCHAR(50),
    FOREIGN KEY (REC_ID) REFERENCES MEDICALRECORD(REC_ID),
    FOREIGN KEY (USERNAME) REFERENCES USER_INFO(USERNAME)
)''')

# Create ROOM table
cursor.execute('''CREATE TABLE IF NOT EXISTS ROOM (
    ROOM_ID INT NOT NULL PRIMARY KEY,
    ROOM_TYPE VARCHAR(20) NOT NULL,
    BED_NO INT NOT NULL,
    ROOM_LOCATION VARCHAR(200) NOT NULL,
    AVILABILITY BIT,
    PATIENT_ID INT,
    FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
)''')

# Create VISIT table
cursor.execute('''CREATE TABLE IF NOT EXISTS VISIT (
    VISIT_NO INT NOT NULL PRIMARY KEY,
    VISITOR_NAME VARCHAR(30) NOT NULL,
    VISITOR_PHONE INT NOT NULL,
    DAY INT NOT NULL,
    YEAR INT NOT NULL,
    MONTH INT NOT NULL,
    HOUR INT NOT NULL,
    PATIENT_ID INT,
    FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
)''')

# Create RECORD table
cursor.execute('''CREATE TABLE IF NOT EXISTS RECORD (
    DOC_ID INT,
    REC_ID INT,
    PRIMARY KEY (DOC_ID, REC_ID),
    FOREIGN KEY (DOC_ID) REFERENCES DOCTOR(DOCTOR_ID),
    FOREIGN KEY (REC_ID) REFERENCES MEDICALRECORD(REC_ID)
)''')

# Create TREATS table
cursor.execute('''CREATE TABLE IF NOT EXISTS TREATS (
    DOCT_ID INT,
    PATIENT_ID INT,
    PRIMARY KEY (DOCT_ID, PATIENT_ID),
    FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(PATIENT_ID),
    FOREIGN KEY (DOCT_ID) REFERENCES DOCTOR(DOCTOR_ID)
)''')

# Create DOCTOR_SPECIALITY table
cursor.execute('''CREATE TABLE IF NOT EXISTS DOCTOR_SPECIALITY (
    SPECIALITY VARCHAR(150),
    DOC_ID INT,
    FOREIGN KEY (DOC_ID) REFERENCES DOCTOR(DOCTOR_ID)
)''')

# Commit the changes and close the connection
conn.commit()
conn.close()