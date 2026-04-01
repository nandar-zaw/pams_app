from models.patient import Patient

def patient_to_dict(patient: Patient) -> dict:
    return {
        "patientId": patient.patient_id,
        "firstName": patient.first_name,
        "lastName": patient.last_name,
        "phoneNumber": patient.phone_number,
        "email": patient.email,
        "mailingAddress": patient.mailing_address,
        "dateOfBirth": patient.date_of_birth.isoformat(),
        "age": patient.age
    }
