from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/examinations", tags=["Examinations (HTML)"])
templates = Jinja2Templates(directory="templates")


def get_examination_service():
	from data.repositories import ExaminationRepository
	from business.services import ExaminationService
	return ExaminationService(ExaminationRepository())


def get_patient_service():
	from data.repositories import PatientRepository
	from business.services import PatientService
	return PatientService(PatientRepository())


def get_doctor_service():
	from data.repositories import DoctorRepository
	from business.services import DoctorService
	return DoctorService(DoctorRepository())


@router.get("/", response_class=HTMLResponse)
def list_examinations(request: Request):
	service = get_examination_service()
	examinations = service.get_all_examinations()
	return templates.TemplateResponse("examinations/list.html", {"request": request, "examinations": examinations})


@router.get("/create", response_class=HTMLResponse)
def create_examination_form(request: Request):
	patients = get_patient_service().get_all_patients()
	doctors = get_doctor_service().get_all_doctors()
	return templates.TemplateResponse("examinations/form.html", {
		"request": request, "examination": None, "patients": patients, "doctors": doctors
	})


@router.post("/create")
def create_examination(
	patient_id: int = Form(...),
	doctor_id: int = Form(...),
	status: str = Form(...)
):
	service = get_examination_service()
	service.create_examination(patient_id, doctor_id, status)
	return RedirectResponse(url="/examinations/", status_code=303)


@router.get("/edit/{exam_id}", response_class=HTMLResponse)
def edit_examination_form(request: Request, exam_id: int):
	service = get_examination_service()
	examination = service.get_examination_by_id(exam_id)
	patients = get_patient_service().get_all_patients()
	doctors = get_doctor_service().get_all_doctors()
	return templates.TemplateResponse("examinations/form.html", {
		"request": request, "examination": examination, "patients": patients, "doctors": doctors
	})


@router.post("/edit/{exam_id}")
def edit_examination(
	exam_id: int,
	patient_id: int = Form(...),
	doctor_id: int = Form(...),
	status: str = Form(...)
):
	service = get_examination_service()
	service.update_examination(exam_id, patient_id, doctor_id, status)
	return RedirectResponse(url="/examinations/", status_code=303)


@router.post("/delete/{exam_id}")
def delete_examination(exam_id: int):
	service = get_examination_service()
	service.delete_examination(exam_id)
	return RedirectResponse(url="/examinations/", status_code=303)
