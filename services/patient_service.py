import json
from typing import List
from models.patient import Patient
from utils.json_formatter import patient_to_dict

class PatientService:
    def __init__(self, patients: List[Patient]):
        self.patients = patients

    def get_patients_sorted_by_age_desc(self) -> List[Patient]:
        return sorted(self.patients, key=lambda p: p.age, reverse=True)

    def export_to_json(self, filename: str):
        sorted_patients = self.get_patients_sorted_by_age_desc()
        data = [patient_to_dict(p) for p in sorted_patients]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def print_to_console(self):
        sorted_patients = self.get_patients_sorted_by_age_desc()
        data = [patient_to_dict(p) for p in sorted_patients]
        print(json.dumps(data, indent=2))
