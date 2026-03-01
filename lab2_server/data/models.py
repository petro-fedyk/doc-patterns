from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Patient(Base):
	__tablename__ = "patients"

	id = Column(Integer, primary_key=True)
	first_name = Column(String)
	last_name = Column(String)
	email = Column(String)


class Doctor(Base):
	__tablename__ = "doctors"

	id = Column(Integer, primary_key=True)
	first_name = Column(String)
	specialization = Column(String)


class Examination(Base):
	__tablename__ = "examinations"

	id = Column(Integer, primary_key=True)
	patient_id = Column(Integer, ForeignKey("patients.id"))
	doctor_id = Column(Integer, ForeignKey("doctors.id"))
	status = Column(String)

	patient = relationship("Patient")
	doctor = relationship("Doctor")


class TestResult(Base):
	__tablename__ = "test_results"

	id = Column(Integer, primary_key=True)
	examination_id = Column(Integer, ForeignKey("examinations.id"))
	file_type = Column(String)
	file_path = Column(String)
