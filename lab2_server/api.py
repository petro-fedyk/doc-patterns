
from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from sqlalchemy.orm import Session
from data.database import SessionLocal, engine, Base
from data.models import Patient, Doctor, Examination, TestResult
from typing import List
from pydantic import BaseModel
import csv


app = FastAPI(title="Lab2 Medical API", description="Swagger UI for all tables", version="1.0.0")

# Create tables if not exist
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schemas
class PatientSchema(BaseModel):
    id: int = None
    first_name: str
    last_name: str
    email: str
    class Config:
        from_attributes = True

class DoctorSchema(BaseModel):
    id: int = None
    first_name: str
    specialization: str
    class Config:
        from_attributes = True

class ExaminationSchema(BaseModel):
    id: int = None
    patient_id: int
    doctor_id: int
    status: str
    class Config:
        from_attributes = True

class TestResultSchema(BaseModel):
    id: int = None
    examination_id: int
    file_type: str
    file_path: str
    class Config:
        from_attributes = True


# CRUD for Patient
@app.get("/patients", response_model=List[PatientSchema])
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()


@app.post("/patients", response_model=PatientSchema)
def create_patient(patient: PatientSchema, db: Session = Depends(get_db)):
    db_patient = Patient(first_name=patient.first_name, last_name=patient.last_name, email=patient.email)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


# CRUD for Doctor
@app.get("/doctors", response_model=List[DoctorSchema])
def get_doctors(db: Session = Depends(get_db)):
    return db.query(Doctor).all()


@app.post("/doctors", response_model=DoctorSchema)
def create_doctor(doctor: DoctorSchema, db: Session = Depends(get_db)):
    db_doctor = Doctor(first_name=doctor.first_name, specialization=doctor.specialization)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


# CRUD for Examination
@app.get("/examinations", response_model=List[ExaminationSchema])
def get_examinations(db: Session = Depends(get_db)):
    return db.query(Examination).all()


@app.post("/examinations", response_model=ExaminationSchema)
def create_examination(exam: ExaminationSchema, db: Session = Depends(get_db)):
    db_exam = Examination(patient_id=exam.patient_id, doctor_id=exam.doctor_id, status=exam.status)
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam


# CRUD for TestResult
@app.get("/test_results", response_model=List[TestResultSchema])
def get_test_results(db: Session = Depends(get_db)):
    return db.query(TestResult).all()


@app.post("/test_results", response_model=TestResultSchema)
def create_test_result(result: TestResultSchema, db: Session = Depends(get_db)):
    db_result = TestResult(examination_id=result.examination_id, file_type=result.file_type, file_path=result.file_path)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result


# CSV upload endpoint
@app.post("/import-csv/")
async def import_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")
    content = await file.read()
    decoded = content.decode('utf-8').splitlines()
    reader = csv.DictReader(decoded)
    imported = 0
    for row in reader:
        # Import Patient
        patient = Patient(
            first_name=row["patient_first_name"],
            last_name=row["patient_last_name"],
            email=row["email"]
        )
        db.add(patient)
        db.commit()
        db.refresh(patient)

        # Import Doctor
        doctor = Doctor(
            first_name=row["doctor_name"],
            specialization=row["specialization"]
        )
        db.add(doctor)
        db.commit()
        db.refresh(doctor)

        # Import Examination
        exam = Examination(
            patient_id=patient.id,
            doctor_id=doctor.id,
            status=row["status"]
        )
        db.add(exam)
        db.commit()
        db.refresh(exam)

        # Import TestResult
        result = TestResult(
            examination_id=exam.id,
            file_type=row["file_type"],
            file_path=row["file_path"]
        )
        db.add(result)
        db.commit()
        imported += 1
    return {"imported": imported}
