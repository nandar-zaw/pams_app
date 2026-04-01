from datetime import date
from models.patient import Patient
from services.patient_service import PatientService

# Preloaded patient data
patients = [
    Patient(1, "Daniel", "Agar", "(641) 123-0009", "dagar@m.as", "1 N Street", date(1987, 1, 19)),
    Patient(2, "Ana", "Smith", None, "amsith@te.edu", None, date(1948, 12, 5)),
    Patient(3, "Marcus", "Garvey", "(123) 292-0018", None, "4 East Ave", date(2001, 9, 18)),
    Patient(4, "Jeff", "Goldbloom", "(999) 165-1192", "jgold@es.co.za", None, date(1995, 2, 28)),
    Patient(5, "Mary", "Washington", None, None, "30 W Burlington", date(1932, 5, 31)),
]

service = PatientService(patients)

def main():
    while True:
        print("\nPatient Appointment Management System (PAMS)")
        print("1. Export Patients to JSON file (patients_output.json)")
        print("2. Print Patients to console (same JSON format, sorted by age descending)")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            service.export_to_json("patients_output.json")
            print("Patients exported to patients_output.json")
        elif choice == '2':
            service.print_to_console()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
