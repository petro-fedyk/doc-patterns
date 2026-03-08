from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/patients", tags=["Patients (HTML)"])
templates = Jinja2Templates(directory="templates")


def get_patient_service():
	from data.repositories import PatientRepository
	from business.services import PatientService
	return PatientService(PatientRepository())


@router.get("/", response_class=HTMLResponse)
def list_patients(request: Request):
	service = get_patient_service()
	patients = service.get_all_patients()
	return templates.TemplateResponse("patients/list.html", {"request": request, "patients": patients})


@router.get("/create", response_class=HTMLResponse)
def create_patient_form(request: Request):
	return templates.TemplateResponse("patients/form.html", {"request": request, "patient": None})


@router.post("/create")
def create_patient(
	first_name: str = Form(...),
	last_name: str = Form(...),
	email: str = Form(...)
):
	service = get_patient_service()
	service.create_patient(first_name, last_name, email)
	return RedirectResponse(url="/patients/", status_code=303)


@router.get("/edit/{patient_id}", response_class=HTMLResponse)
def edit_patient_form(request: Request, patient_id: int):
	service = get_patient_service()
	patient = service.get_patient_by_id(patient_id)
	return templates.TemplateResponse("patients/form.html", {"request": request, "patient": patient})


@router.post("/edit/{patient_id}")
def edit_patient(
	patient_id: int,
	first_name: str = Form(...),
	last_name: str = Form(...),
	email: str = Form(...)
):
	service = get_patient_service()
	service.update_patient(patient_id, first_name, last_name, email)
	return RedirectResponse(url="/patients/", status_code=303)


@router.post("/delete/{patient_id}")
def delete_patient(patient_id: int):
	service = get_patient_service()
	service.delete_patient(patient_id)
	return RedirectResponse(url="/patients/", status_code=303)
