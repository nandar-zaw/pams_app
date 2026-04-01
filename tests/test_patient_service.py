import unittest
import json
import os
from datetime import date
from models.patient import Patient
from services.patient_service import PatientService

class TestPatientService(unittest.TestCase):
    def setUp(self):
        self.patients = [
            Patient(1, "Daniel", "Agar", "(641) 123-0009", "dagar@m.as", "1 N Street", date(1987, 1, 19)),
            Patient(2, "Ana", "Smith", None, "amsith@te.edu", None, date(1948, 12, 5)),
            Patient(3, "Marcus", "Garvey", "(123) 292-0018", None, "4 East Ave", date(2001, 9, 18)),
            Patient(4, "Jeff", "Goldbloom", "(999) 165-1192", "jgold@es.co.za", None, date(1995, 2, 28)),
            Patient(5, "Mary", "Washington", None, None, "30 W Burlington", date(1932, 5, 31)),
        ]
        self.service = PatientService(self.patients)

    def test_patient_count(self):
        self.assertEqual(len(self.service.patients), 5)

    def test_sorted_by_age_descending(self):
        sorted_patients = self.service.get_patients_sorted_by_age_desc()
        self.assertEqual(sorted_patients[0].patient_id, 5)  # Mary is oldest
        self.assertEqual(sorted_patients[-1].patient_id, 3)  # Marcus is youngest

    def test_age_calculation(self):
        mary = self.patients[4]
        self.assertEqual(mary.age, 93)
        marcus = self.patients[2]
        self.assertEqual(marcus.age, 24)

    def test_null_fields_allowed(self):
        ana = self.patients[1]
        self.assertIsNone(ana.phone_number)
        self.assertIsNone(ana.mailing_address)
        mary = self.patients[4]
        self.assertIsNone(mary.phone_number)
        self.assertIsNone(mary.email)

    def test_json_output_contains_age(self):
        self.service.export_to_json("test_output.json")
        with open("test_output.json", 'r') as f:
            data = json.load(f)
        self.assertIn("age", data[0])
        self.assertEqual(data[0]["patientId"], 5)
        self.assertEqual(data[0]["age"], 93)
        os.remove("test_output.json")
