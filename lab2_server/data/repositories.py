from .interfaces import IPatientRepository, IDoctorRepository, IExaminationRepository, ITestResultRepository
from .database import SessionLocal
from .models import Patient, Doctor, Examination, TestResult


class PatientRepository(IPatientRepository):

	def get_all(self):
		session = SessionLocal()
		try:
			return session.query(Patient).all()
		finally:
			session.close()

	def get_by_id(self, patient_id: int):
		session = SessionLocal()
		try:
			return session.query(Patient).filter(Patient.id == patient_id).first()
		finally:
			session.close()

	def create(self, patient):
		session = SessionLocal()
		try:
			session.add(patient)
			session.commit()
			session.refresh(patient)
			return patient
		finally:
			session.close()

	def update(self, patient):
		session = SessionLocal()
		try:
			existing = session.query(Patient).filter(Patient.id == patient.id).first()
			if existing:
				existing.first_name = patient.first_name
				existing.last_name = patient.last_name
				existing.email = patient.email
				session.commit()
				session.refresh(existing)
				return existing
		finally:
			session.close()

	def delete(self, patient_id: int):
		session = SessionLocal()
		try:
			patient = session.query(Patient).filter(Patient.id == patient_id).first()
			if patient:
				session.delete(patient)
				session.commit()
		finally:
			session.close()


class DoctorRepository(IDoctorRepository):

	def get_all(self):
		session = SessionLocal()
		try:
			return session.query(Doctor).all()
		finally:
			session.close()

	def get_by_id(self, doctor_id: int):
		session = SessionLocal()
		try:
			return session.query(Doctor).filter(Doctor.id == doctor_id).first()
		finally:
			session.close()

	def create(self, doctor):
		session = SessionLocal()
		try:
			session.add(doctor)
			session.commit()
			session.refresh(doctor)
			return doctor
		finally:
			session.close()

	def update(self, doctor):
		session = SessionLocal()
		try:
			existing = session.query(Doctor).filter(Doctor.id == doctor.id).first()
			if existing:
				existing.first_name = doctor.first_name
				existing.specialization = doctor.specialization
				session.commit()
				session.refresh(existing)
				return existing
		finally:
			session.close()

	def delete(self, doctor_id: int):
		session = SessionLocal()
		try:
			doctor = session.query(Doctor).filter(Doctor.id == doctor_id).first()
			if doctor:
				session.delete(doctor)
				session.commit()
		finally:
			session.close()


class ExaminationRepository(IExaminationRepository):

	def get_all(self):
		session = SessionLocal()
		try:
			return session.query(Examination).all()
		finally:
			session.close()

	def get_by_id(self, exam_id: int):
		session = SessionLocal()
		try:
			return session.query(Examination).filter(Examination.id == exam_id).first()
		finally:
			session.close()

	def create(self, exam):
		session = SessionLocal()
		try:
			session.add(exam)
			session.commit()
			session.refresh(exam)
			return exam
		finally:
			session.close()

	def update(self, exam):
		session = SessionLocal()
		try:
			existing = session.query(Examination).filter(Examination.id == exam.id).first()
			if existing:
				existing.patient_id = exam.patient_id
				existing.doctor_id = exam.doctor_id
				existing.status = exam.status
				session.commit()
				session.refresh(existing)
				return existing
		finally:
			session.close()

	def delete(self, exam_id: int):
		session = SessionLocal()
		try:
			exam = session.query(Examination).filter(Examination.id == exam_id).first()
			if exam:
				session.delete(exam)
				session.commit()
		finally:
			session.close()

	def save_examination(self, exam):
		session = SessionLocal()
		session.add(exam)
		session.commit()
		session.close()


class TestResultRepository(ITestResultRepository):

	def get_all(self):
		session = SessionLocal()
		try:
			return session.query(TestResult).all()
		finally:
			session.close()

	def get_by_id(self, result_id: int):
		session = SessionLocal()
		try:
			return session.query(TestResult).filter(TestResult.id == result_id).first()
		finally:
			session.close()

	def create(self, result):
		session = SessionLocal()
		try:
			session.add(result)
			session.commit()
			session.refresh(result)
			return result
		finally:
			session.close()

	def update(self, result):
		session = SessionLocal()
		try:
			existing = session.query(TestResult).filter(TestResult.id == result.id).first()
			if existing:
				existing.examination_id = result.examination_id
				existing.file_type = result.file_type
				existing.file_path = result.file_path
				session.commit()
				session.refresh(existing)
				return existing
		finally:
			session.close()

	def delete(self, result_id: int):
		session = SessionLocal()
		try:
			result = session.query(TestResult).filter(TestResult.id == result_id).first()
			if result:
				session.delete(result)
				session.commit()
		finally:
			session.close()
