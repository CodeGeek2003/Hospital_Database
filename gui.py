import sqlite3
import tkinter as tk
import csv
from tkinter import ttk, messagebox

# Create the database connection
conn = sqlite3.connect('Healthcare.db')

# Function to check if the user is valid
def login(username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER_INFO WHERE USERNAME = ? AND PASSWORD_USER = ?", (username, password))
    user = cursor.fetchone()

    if user:
        open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to open the main window
def open_main_window():
    login_window.destroy()

    main_window = tk.Tk()
    main_window.title("Healthcare Database")
    main_window.geometry("300x150")

    # Search button
    search_button = tk.Button(main_window, text="Search", command=open_search_window)
    search_button.pack(pady=10)

    # View Tables button
    view_tables_button = tk.Button(main_window, text="View Tables", command=view_tables)
    view_tables_button.pack(pady=10)

    # Generate Report button
    generate_report_button = tk.Button(main_window, text="Generate Report", command=open_report_window)
    generate_report_button.pack(pady=10)

    main_window.mainloop()

# Function to open the search window
def open_search_window():
    search_window = tk.Toplevel()
    search_window.title("Search")
    search_window.geometry("300x200")

    # Get the list of tables
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]

    # Table label and dropdown
    table_label = tk.Label(search_window, text="Select Table:")
    table_label.pack()
    table_dropdown = ttk.Combobox(search_window, values=table_names)
    table_dropdown.pack()

    # Column label and dropdown
    column_label = tk.Label(search_window, text="Select Column:")
    column_label.pack()
    column_dropdown = ttk.Combobox(search_window)
    column_dropdown.pack(pady=5)

    # Value label and entry
    value_label = tk.Label(search_window, text="Enter Value:")
    value_label.pack()
    value_entry = tk.Entry(search_window)
    value_entry.pack(pady=5)

    # Search button
    search_button = tk.Button(search_window, text="Search", command=lambda: perform_search(table_dropdown.get(), column_dropdown.get(), value_entry.get()))
    search_button.pack(pady=10)

    # Update column dropdown based on selected table
    def update_columns(event):
        selected_table = table_dropdown.get()
        if selected_table:
            cursor.execute(f"PRAGMA table_info({selected_table})")
            columns = cursor.fetchall()
            column_names = [column[1] for column in columns]
            column_dropdown['values'] = column_names
        else:
            column_dropdown.set('')
            column_dropdown['values'] = []

    table_dropdown.bind("<<ComboboxSelected>>", update_columns)

    search_window.mainloop()

# Function to perform the search
def perform_search(table_name, column_name, search_value):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name} WHERE {column_name} = ?", (search_value,))
    search_result = cursor.fetchall()

    if search_result:
        messagebox.showinfo("Search Result", f"Search result in {table_name}:\n\n{search_result}")
    else:
        messagebox.showinfo("Search Result", "No matching records found.")

# Function to open the table treeview window
def view_tables():
   cursor = conn.cursor()
   cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
   tables = cursor.fetchall()
   table_names = [table[0] for table in tables]


   table_treeview_window = tk.Toplevel()
   table_treeview_window.title("Tables")
   table_treeview_window.geometry("400x300")


   # Create the table treeview
   table_treeview = ttk.Treeview(table_treeview_window)
   table_treeview.pack(fill="both", expand=True)


   # Add columns to the treeview
   table_treeview['columns'] = ('Table Name', 'Column Count')


   # Define column properties
   table_treeview.column("#0", width=0, stretch=tk.NO)
   table_treeview.column("Table Name", anchor=tk.W, width=200)
   table_treeview.column("Column Count", anchor=tk.W, width=200)


   # Add column headings
   table_treeview.heading("Table Name", text="Table Name")
   table_treeview.heading("Column Count", text="Column Count")


   for table_name in table_names:
       cursor.execute(f"PRAGMA table_info({table_name})")
       columns = cursor.fetchall()
       column_count = len(columns)


       table_treeview.insert("", tk.END, text="", values=(table_name, column_count))


   table_treeview.bind("<Double-1>", lambda event: display_table_data(table_treeview.item(table_treeview.selection())['values'][0]))


   table_treeview_window.mainloop()


# Function to display table data
def display_table_data(table_name):
   cursor = conn.cursor()
   cursor.execute(f"SELECT * FROM {table_name}")
   table_data = cursor.fetchall()


   table_data_window = tk.Toplevel()
   table_data_window.title(table_name)


   # Create the treeview
   table_data_treeview = ttk.Treeview(table_data_window, columns=[str(i) for i in range(len(table_data[0]))])
   table_data_treeview.pack(pady=10)
   # Insert table headers
   table_data_treeview["columns"] = [f"#{i}" for i in range(len(table_data[0]))]
   for i in range(len(table_data[0])):
       table_data_treeview.column(f"#{i}", width=100, anchor="center")
       table_data_treeview.heading(f"#{i}", text=f"Column {i}")

   # Insert table data
   for row in table_data:
       table_data_treeview.insert("", tk.END, text="", values=row)

   table_data_window.mainloop()


# Function to open the report window
def open_report_window():
    report_window = tk.Toplevel()
    report_window.title("Generate Report")
    report_window.geometry("300x150")

    # Doctor & Patient button
    doctor_patient_button = tk.Button(report_window, text="Doctor & Patient", command=generate_doctor_patient_report)
    doctor_patient_button.pack(pady=10)

    # Doctor & Patient & Medical Record button
    doctor_patient_record_button = tk.Button(report_window, text="Doctor & Patient & Medical Record", command=generate_doctor_patient_record_report)
    doctor_patient_record_button.pack(pady=10)

    # Doctor Patient View button
    doctor_patient_view_button = tk.Button(report_window, text="Doctor Patient View", command=open_doctor_patient_view)
    doctor_patient_view_button.pack(pady=10)

    report_window.mainloop()

# Function to generate Doctor & Patient report
# Function to generate Doctor & Patient report
# Function to generate doctor-patient report
def generate_doctor_patient_report():
    cursor = conn.cursor()
    cursor.execute("SELECT DOCTOR.DOCTOR_NAME, DOCTOR.DOC_EMAIL, DOCTOR.DOC_MOBILE, PATIENT.patient_name, PATIENT.patient_address, PATIENT.PATIENT_MOBILE FROM DOCTOR JOIN TREATS ON DOCTOR.DOCTOR_ID = TREATS.DOCT_ID JOIN PATIENT ON TREATS.PATIENT_ID = PATIENT.PATIENT_ID")
    report_data = cursor.fetchall()

    if report_data:
        with open("doctor_patient_report.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Doctor Name", "Doctor Email", "Doctor Mobile", "Patient Name", "Patient Address", "Patient Mobile"])

            for row in report_data:
                writer.writerow(row)

        report_window = tk.Toplevel()
        report_window.title("Doctor-Patient Report")
        report_window.geometry("800x600")

        report_text = tk.Text(report_window)
        report_text.pack(expand=True, fill='both')

        for row in report_data:
            report_text.insert(tk.END, f"Doctor Name: {row[0]}\n")
            report_text.insert(tk.END, f"Doctor Email: {row[1]}\n")
            report_text.insert(tk.END, f"Doctor Mobile: {row[2]}\n")
            report_text.insert(tk.END, f"Patient Name: {row[3]}\n")
            report_text.insert(tk.END, f"Patient Address: {row[4]}\n")
            report_text.insert(tk.END, f"Patient Mobile: {row[5]}\n")
            report_text.insert(tk.END, "\n")

    else:
        messagebox.showinfo("Report", "No records found.")

# Function to generate doctor-patient record number report
def generate_doctor_patient_record_number():
    cursor = conn.cursor()
    cursor.execute("SELECT DOCTOR.DOCTOR_NAME, PATIENT.patient_name, COUNT(RECORD.DOC_ID) AS Patient_Record_Count FROM DOCTOR JOIN TREATS ON DOCTOR.DOCTOR_ID = TREATS.DOCT_ID JOIN PATIENT ON TREATS.PATIENT_ID = PATIENT.PATIENT_ID JOIN RECORD ON DOCTOR.DOCTOR_ID = RECORD.DOC_ID GROUP BY DOCTOR.DOCTOR_NAME, PATIENT.patient_name")
    report_data = cursor.fetchall()

    if report_data:
        with open("doctor_patient_record_number_report.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Doctor Name", "Patient Name", "Patient Record Count"])

            for row in report_data:
                writer.writerow(row)

        report_window = tk.Toplevel()
        report_window.title("Doctor-Patient Record Number Report")
        report_window.geometry("800x600")

        report_text = tk.Text(report_window)
        report_text.pack(expand=True, fill='both')

        for row in report_data:
            report_text.insert(tk.END, f"Doctor Name: {row[0]}\n")
            report_text.insert(tk.END, f"Patient Name: {row[1]}\n")
            report_text.insert(tk.END, f"Patient Record Count: {row[2]}\n")
            report_text.insert(tk.END, "\n")

    else:
        messagebox.showinfo("Report", "No records found.")

# Function to generate Doctor & Patient & Medical Record report
def generate_doctor_patient_medical_record_report():
    cursor = conn.cursor()
    cursor.execute("SELECT DOCTOR.DOCTOR_NAME, DOCTOR.DOC_EMAIL, DOCTOR.DOC_MOBILE, PATIENT.patient_name, PATIENT.patient_address, PATIENT.PATIENT_MOBILE, MEDICALRECORD.MEDECINE, MEDICALRECORD.DIAGNOSE FROM DOCTOR JOIN TREATS ON DOCTOR.DOCTOR_ID = TREATS.DOCT_ID JOIN PATIENT ON TREATS.PATIENT_ID = PATIENT.PATIENT_ID JOIN MEDICALRECORD ON PATIENT.REC_ID = MEDICALRECORD.REC_ID")
    report_data = cursor.fetchall()

    if report_data:
        with open("doctor_patient_medical_record_report.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Doctor Name", "Doctor Email", "Doctor Mobile", "Patient Name", "Patient Address", "Patient Mobile", "Medicine", "Diagnose"])

            for row in report_data:
                writer.writerow(row)

        report_window = tk.Toplevel()
        report_window.title("Doctor-Patient-Medical Record Report")
        report_window.geometry("800x600")

        report_text = tk.Text(report_window)
        report_text.pack(expand=True, fill='both')

        for row in report_data:
            report_text.insert(tk.END, f"Doctor Name: {row[0]}\n")
            report_text.insert(tk.END, f"Doctor Email: {row[1]}\n")
            report_text.insert(tk.END, f"Doctor Mobile: {row[2]}\n")
            report_text.insert(tk.END, f"Patient Name: {row[3]}\n")
            report_text.insert(tk.END, f"Patient Address: {row[4]}\n")
            report_text.insert(tk.END, f"Patient Mobile: {row[5]}\n")
            report_text.insert(tk.END, f"Medicine: {row[6]}\n")
            report_text.insert(tk.END, f"Diagnose: {row[7]}\n")
            report_text.insert(tk.END, "\n")

    else:
        messagebox.showinfo("Report", "No records found.")

# Function to generate doctor-patient-medical record report
def generate_doctor_patient_record_report():
    cursor = conn.cursor()
    cursor.execute("SELECT DOCTOR.DOCTOR_NAME, PATIENT.patient_name, PATIENT.patient_id, MEDICALRECORD.* FROM DOCTOR JOIN PATIENT ON DOCTOR.USERNAME = PATIENT.USERNAME JOIN MEDICALRECORD ON PATIENT.REC_ID = MEDICALRECORD.REC_ID")
    report_data = cursor.fetchall()

    if report_data:
        report_window = tk.Toplevel()
        report_window.title("Doctor-Patient-Medical Record Report")
        report_window.geometry("600x400")

        report_text = tk.Text(report_window)
        report_text.pack(expand=True, fill='both')

        # Add report data to the text widget
        for row in report_data:
            report_text.insert(tk.END, f"Doctor Name: {row[0]}\n")
            report_text.insert(tk.END, f"Patient Name: {row[1]}\n")
            report_text.insert(tk.END, f"Patient ID: {row[2]}\n")
            report_text.insert(tk.END, f"Medical Record ID: {row[3]}\n")
            report_text.insert(tk.END, f"Medicine: {row[4]}\n")
            report_text.insert(tk.END, f"Insurance: {row[5]}\n")
            report_text.insert(tk.END, f"Diagnosis: {row[6]}\n")
            report_text.insert(tk.END, "\n")

    else:
        messagebox.showinfo("Report", "No records found.")

# Function to open the Doctor Patient View window
def open_doctor_patient_view():
    doctor_patient_view_window = tk.Toplevel()
    doctor_patient_view_window.title("Doctor Patient View")
    doctor_patient_view_window.geometry("300x150")

    # Doctor ID label and entry
    doctor_id_label = tk.Label(doctor_patient_view_window, text="Doctor ID:")
    doctor_id_label.pack(pady=5)
    doctor_id_entry = tk.Entry(doctor_patient_view_window)
    doctor_id_entry.pack(pady=5)

    # Search button
    search_button = tk.Button(doctor_patient_view_window, text="Search", command=lambda: search_doctor_patient_view(doctor_id_entry.get()))
    search_button.pack(pady=10)

    doctor_patient_view_window.mainloop()

# Function to search Doctor Patient View
# Function to search doctor-patient view
# Function to search doctor-patient view
# Function to search doctor-patient view
def search_doctor_patient_view(doctor_id):
    cursor = conn.cursor()
    cursor.execute("SELECT PATIENT.PATIENT_ID, MEDICALRECORD.DIAGNOSE FROM PATIENT JOIN TREATS ON PATIENT.PATIENT_ID = TREATS.PATIENT_ID JOIN MEDICALRECORD ON PATIENT.REC_ID = MEDICALRECORD.REC_ID WHERE TREATS.DOCT_ID = ?", (doctor_id,))
    report_data = cursor.fetchall()

    if report_data:
        with open("doctor_patient_view_search.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Patient ID", "Diagnose"])

            for row in report_data:
                writer.writerow(row)

        report_window = tk.Toplevel()
        report_window.title("Doctor-Patient View Search")
        report_window.geometry("800x600")

        report_text = tk.Text(report_window)
        report_text.pack(expand=True, fill='both')

        for row in report_data:
            report_text.insert(tk.END, f"Patient ID: {row[0]}\n")
            report_text.insert(tk.END, f"Diagnose: {row[1]}\n")
            report_text.insert(tk.END, "\n")

    else:
        messagebox.showinfo("Report", "No records found.")

# Function to close the database connection and exit the program
def close_program():
    conn.close()
    login_window.destroy()

# Create the login window
login_window = tk.Tk()
login_window.title("Healthcare Database - Login")
login_window.geometry("300x150")

# Username label and entry
username_label = tk.Label(login_window, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack()

# Password label and entry
password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

# Login button
login_button = tk.Button(login_window, text="Login", command=lambda: login(username_entry.get(), password_entry.get()))
login_button.pack()

login_window.protocol("WM_DELETE_WINDOW", close_program)
login_window.mainloop()
