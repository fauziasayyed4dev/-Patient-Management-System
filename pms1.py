import sys
from datetime import datetime

# Global list
Patient_records = []

def AddPatientRecord():
    #def AddEmployeeRecord():
    Pat = {}
    Pat["id"] = int(input("Enter patient ID: "))
    Pat["name"] = input("Enter patient name: ")
    Pat["mobile"] = input("Enter patient mobile number: ")
    Pat["designation"] = input("Enter patient designation: ")
    Pat["appointment_datetime"] = None
    Pat["checked_in"] = False
    Pat["triage_level"] = None
    Pat["doctor_notes"] = None
    Pat["bill_amount"] = 0.0

    Patient_records.append(Pat)
    print("Patient record added successfully.")

def ShowPatientRecords():
    if not Patient_records:
        print("No patient records found.")
        return

    for Pat in Patient_records:
        print(f"ID: {Pat['id']}")
        print(f"Name: {Pat['name']}")
        print(f"Mobile: {Pat['mobile']}")
        print(f"Designation: {Pat['designation']}")

        if Pat["appointment_datetime"]:
            print(
                "Appointment:",
                Pat["appointment_datetime"].strftime("%Y-%m-%d %H:%M")
            )
        else:
            print("Appointment: Not scheduled")

        print("-" * 30)

def DeletePatientRecord(Patient_id):
    for Pat in Patient_records:
        if Pat["id"] == Patient_id:
            Patient_records.remove(Pat)
            print(f"Patient record with ID {Patient_id} deleted.")
            return
    print(f"No patient record found with ID {Patient_id}.")

def ScheduleAppointment(Patient_id):
    #odef UpdateEmployeeRecord(employee_id):
    for Pat in Patient_records:
        if Pat["id"] == Patient_id:
            print("Patient found. Please schedule appointment.")

            while True:
                try:
                    appt_input = input(
                        "Enter appointment date & time (YYYY-MM-DD HH:MM): "
                    )
                    Pat["appointment_datetime"] = datetime.strptime(
                        appt_input, "%Y-%m-%d %H:%M"
                    )
                    break
                except ValueError:
                    print("Invalid format! Please use YYYY-MM-DD HH:MM")

            print(f"Appointment scheduled for Patient ID {Patient_id}.")
            return

    print(f"No patient record found with ID {Patient_id}.")
def CheckInPatient(Patient_id):
    for Pat in Patient_records:
        if Pat["id"] == Patient_id:
            Pat["checked_in"] = True
            print(f"Patient ID {Patient_id} checked in successfully.")
            return
    print(f"No patient found with ID {Patient_id}.")
def TriagePatient(Patient_id):
    for Pat in Patient_records:
        if Pat["id"] == Patient_id:
            level = input("Enter triage level (Low/Medium/High/Emergency): ")
            Pat["triage_level"] = level
            print(f"Triage level set to {level} for Patient ID {Patient_id}.")
            return
    print(f"No patient found with ID {Patient_id}.")
def ClinicalEncounter(Patient_id):
    for Pat in Patient_records:
        if Pat["id"] == Patient_id:
            notes = input("Enter doctor clinical notes: ")
            Pat["doctor_notes"] = notes
            print(f"Clinical encounter completed for Patient ID {Patient_id}.")
            return
    print(f"No patient found with ID {Patient_id}.")

def GenerateBill(Patient_id):
    for Pat in Patient_records:
        if Pat["id"] == Patient_id:
            base_fee = 300
            triage_fee = {
                "Low": 100,
                "Medium": 200,
                "High": 400,
                "Emergency": 800
            }

            Pat["bill_amount"] = base_fee + triage_fee.get(
                Pat["triage_level"], 0
            )

            print(f"Bill for Patient ID {Patient_id}")
            print(f"Total Amount: ₹{Pat['bill_amount']}")
            return
    print(f"No patient found with ID {Patient_id}.")

def main():
    
    print("Patient Records Management System")
    choose = -1
    while choose != 0:
        print("\n Menu:")
        print("1. Add Patient Record")
        print("2. Show Patient Records")
        print("3. Delete Patient Record")
        print("4. Schedule Appointment")
        print("5. Check-In Patient")
        print("6. Triage Patient")
        print("7. Clinical Encounter")
        print("8. Generate Bill")
        print("0. Exit")
        try:
            choose = int(input("Choose an operation: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choose == 1:
            AddPatientRecord()
        elif choose == 2:
            ShowPatientRecords()
        elif choose == 3:
            Patient_id = int(input("Enter Patient ID to delete: "))
            DeletePatientRecord(Patient_id)
        elif choose == 4:
            Patient_id = int(input("Enter Patient ID to schedule appointment: "))
            ScheduleAppointment(Patient_id)
        elif choose == 5:
            Patient_id = int(input("Enter Patient ID: "))
            CheckInPatient(Patient_id)
        elif choose == 6:
            Patient_id = int(input("Enter Patient ID: "))
            TriagePatient(Patient_id)
        elif choose == 7:
            Patient_id = int(input("Enter Patient ID: "))
            ClinicalEncounter(Patient_id)
        elif choose == 8:
            Patient_id = int(input("Enter Patient ID: "))
            GenerateBill(Patient_id)
        elif choose == 0:
            print("Exiting the program.")
        else:
            print("Invalid operation selected.")

    sys.exit(0)

if __name__ == "__main__":
    main()