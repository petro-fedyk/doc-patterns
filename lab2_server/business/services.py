import csv
import logging
from .interfaces import IPatientService, IDoctorService, IExaminationService, ITestResultService
from data.models import Examination, Patient, Doctor, TestResult
from sqlalchemy.exc import SQLAlchemyError


class PatientService(IPatientService):

	def __init__(self, repository):
		self.repository = repository

	def get_all_patients(self):
		return self.repository.get_all()

	def get_patient_by_id(self, patient_id: int):
		return self.repository.get_by_id(patient_id)

	def create_patient(self, first_name: str, last_name: str, email: str):
		patient = Patient(first_name=first_name, last_name=last_name, email=email)
		return self.repository.create(patient)

	def update_patient(self, patient_id: int, first_name: str, last_name: str, email: str):
		patient = Patient(id=patient_id, first_name=first_name, last_name=last_name, email=email)
		return self.repository.update(patient)

	def delete_patient(self, patient_id: int):
		self.repository.delete(patient_id)


class DoctorService(IDoctorService):

	def __init__(self, repository):
		self.repository = repository

	def get_all_doctors(self):
		return self.repository.get_all()

	def get_doctor_by_id(self, doctor_id: int):
		return self.repository.get_by_id(doctor_id)

	def create_doctor(self, first_name: str, specialization: str):
		doctor = Doctor(first_name=first_name, specialization=specialization)
		return self.repository.create(doctor)

	def update_doctor(self, doctor_id: int, first_name: str, specialization: str):
		doctor = Doctor(id=doctor_id, first_name=first_name, specialization=specialization)
		return self.repository.update(doctor)

	def delete_doctor(self, doctor_id: int):
		self.repository.delete(doctor_id)


class ExaminationService(IExaminationService):

	def __init__(self, repository):
		self.repository = repository
		self.logger = logging.getLogger("ExaminationService")

	def get_all_examinations(self):
		return self.repository.get_all()

	def get_examination_by_id(self, exam_id: int):
		return self.repository.get_by_id(exam_id)

	def create_examination(self, patient_id: int, doctor_id: int, status: str):
		exam = Examination(patient_id=patient_id, doctor_id=doctor_id, status=status)
		return self.repository.create(exam)

	def update_examination(self, exam_id: int, patient_id: int, doctor_id: int, status: str):
		exam = Examination(id=exam_id, patient_id=patient_id, doctor_id=doctor_id, status=status)
		return self.repository.update(exam)

	def delete_examination(self, exam_id: int):
		self.repository.delete(exam_id)

	def import_from_csv(self, path: str):
		imported = 0
		errors = 0
		with open(path, newline='') as file:
			reader = csv.DictReader(file)
			for row in reader:
				try:
					patient = Patient(
						first_name=row["patient_first_name"],
						last_name=row["patient_last_name"],
						email=row["email"]
					)
					doctor = Doctor(
						first_name=row["doctor_name"],
						specialization=row["specialization"]
					)
					exam = Examination(status=row["status"])
					exam.patient = patient
					exam.doctor = doctor
					result = TestResult(
						file_type=row["file_type"],
						file_path=row["file_path"]
					)
					exam.test_results = [result]
					self.repository.save_examination(exam)
					imported += 1
				except (KeyError, SQLAlchemyError, Exception) as e:
					self.logger.error(f"Error importing row: {row} | {e}")
					errors += 1
		self.logger.info(f"Imported: {imported}, Errors: {errors}")

	def get_statistics(self):
		return {
			"examinations": "not_implemented",
			"patients": "not_implemented",
			"doctors": "not_implemented"
		}


class TestResultService(ITestResultService):

	def __init__(self, repository):
		self.repository = repository

	def get_all_results(self):
		return self.repository.get_all()

	def get_result_by_id(self, result_id: int):
		return self.repository.get_by_id(result_id)

	def create_result(self, examination_id: int, file_type: str, file_path: str):
		result = TestResult(examination_id=examination_id, file_type=file_type, file_path=file_path)
		return self.repository.create(result)

	def update_result(self, result_id: int, examination_id: int, file_type: str, file_path: str):
		result = TestResult(id=result_id, examination_id=examination_id, file_type=file_type, file_path=file_path)
		return self.repository.update(result)

	def delete_result(self, result_id: int):
		self.repository.delete(result_id)
