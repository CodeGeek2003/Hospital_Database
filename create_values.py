import sqlite3

# Connect to the database
conn = sqlite3.connect('Healthcare.db')
cursor = conn.cursor()

# Add 10 elements to the USER_INFO table
for i in range(1, 11):
    username = f'user{i}'
    role_user = f'Role {i}'
    password_user = f'password{i}'
    security_clearance = i
    cursor.execute("INSERT INTO USER_INFO (USERNAME, ROLE_USER, PASSWORD_USER, SECURITY_CLEARANCE) VALUES (?, ?, ?, ?)",
                   (username, role_user, password_user, security_clearance))

# Add 10 elements to the DOCTOR table
for i in range(1, 11):
    doctor_id = i
    doctor_name = f'Doctor {i}'
    doc_mobile = f'123456789{i}'
    doc_email = f'doctor{i}@hospital.com'
    doc_address = f'Address {i}'
    month = i
    year = 2023
    username = f'user{i}'
    cursor.execute("INSERT INTO DOCTOR (DOCTOR_ID, DOCTOR_NAME, DOC_MOBILE, DOC_EMAIL, DOC_ADDRESS, MONTH, YEAR, USERNAME) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (doctor_id, doctor_name, doc_mobile, doc_email, doc_address, month, year, username))

# Add 10 elements to the MEDICALRECORD table
for i in range(1, 11):
    rec_id = i
    medicine = f'Medicine {i}'
    insurance = 'Y' if i % 2 == 0 else 'N'
    diagnose = f'Diagnosis {i}'
    cursor.execute("INSERT INTO MEDICALRECORD (REC_ID, MEDECINE, INSURANCE, DIAGNOSE) VALUES (?, ?, ?, ?)",
                   (rec_id, medicine, insurance, diagnose))

# Add 10 elements to the PATIENT table
for i in range(1, 11):
    patient_id = i
    patient_name = f'Patient {i}'
    patient_address = f'Address {i}'
    patient_mobile = 1234567890 + i
    year = 2023
    month = i
    rec_id = i
    username = f'user{i}'
    cursor.execute("INSERT INTO PATIENT (patient_id, patient_name, patient_address, PATIENT_MOBILE, year, month, REC_ID, USERNAME) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (patient_id, patient_name, patient_address, patient_mobile, year, month, rec_id, username))

# Add 10 elements to the ROOM table
for i in range(1, 11):
    room_id = i
    room_type = f'Type {i}'
    bed_no = i
    room_location = f'Location {i}'
    availability = i % 2  # 0 for False, 1 for True
    patient_id = i
    cursor.execute("INSERT INTO ROOM (ROOM_ID, ROOM_TYPE, BED_NO, ROOM_LOCATION, AVILABILITY, PATIENT_ID) "
                   "VALUES (?, ?, ?, ?, ?, ?)",
                   (room_id, room_type, bed_no, room_location, availability, patient_id))

# Add 10 elements to the VISIT table
# Add 10 elements to the VISIT table
for i in range(1, 11):
    visit_no = i
    visitor_name = f'Visitor {i}'
    visitor_phone = 1234567890 + i
    day = i
    year = 2023
    month = i
    hour = i  # Add the hour value here
    patient_id = i
    cursor.execute("INSERT INTO VISIT (VISIT_NO, VISITOR_NAME, VISITOR_PHONE, DAY, YEAR, MONTH, HOUR, PATIENT_ID) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (visit_no, visitor_name, visitor_phone, day, year, month, hour, patient_id))

# Add 10 elements to the RECORD table
for i in range(1, 11):
    doc_id = i
    rec_id = i
    cursor.execute("INSERT INTO RECORD (DOC_ID, REC_ID) VALUES (?, ?)",
                   (doc_id, rec_id))

# Add 10 elements to the TREATS table
for i in range(1, 11):
    doc_id = i
    patient_id = i
    cursor.execute("INSERT INTO TREATS (DOCT_ID, PATIENT_ID) VALUES (?, ?)",
                   (doc_id, patient_id))

# Add 10 elements to the DOCTOR_SPECIALITY table
for i in range(1, 11):
    speciality = f'Speciality {i}'
    doc_id = i
    cursor.execute("INSERT INTO DOCTOR_SPECIALITY (SPECIALITY, DOC_ID) VALUES (?, ?)",
                   (speciality, doc_id))

# Commit the changes and close the connection
conn.commit()
conn.close()
