from datetime import date
from typing import Optional

class Patient:
    def __init__(self, patient_id: int, first_name: str, last_name: str,
                 phone_number: Optional[str], email: Optional[str],
                 mailing_address: Optional[str], date_of_birth: date):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.mailing_address = mailing_address
        self.date_of_birth = date_of_birth

    @property
    def age(self) -> int:
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
