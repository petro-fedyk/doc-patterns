import csv
import logging
from .interfaces import IExaminationService
from data.models import Examination, Patient, Doctor, TestResult
from sqlalchemy.exc import SQLAlchemyError

class ExaminationService(IExaminationService):

	def __init__(self, repository):
		self.repository = repository
		self.logger = logging.getLogger("ExaminationService")

	def import_from_csv(self, path: str):
		imported = 0
		errors = 0
		with open(path, newline='') as file:
			reader = csv.DictReader(file)

			for row in reader:
				try:
					# Check for duplicates (by email and doctor name)
					# This is a stub, real check would query DB
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

					# Support multiple results per exam (optional, for complexity)
					exam.test_results = [result]

					self.repository.save_examination(exam)
					imported += 1
				except (KeyError, SQLAlchemyError, Exception) as e:
					self.logger.error(f"Error importing row: {row} | {e}")
					errors += 1
		self.logger.info(f"Imported: {imported}, Errors: {errors}")

	def get_statistics(self):
		# Example: return number of exams, patients, doctors
		# This is a stub, real implementation would query DB
		return {
			"examinations": "not_implemented",
			"patients": "not_implemented",
			"doctors": "not_implemented"
		}
