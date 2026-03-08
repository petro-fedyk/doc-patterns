from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/doctors", tags=["Doctors (HTML)"])
templates = Jinja2Templates(directory="templates")


def get_doctor_service():
	from data.repositories import DoctorRepository
	from business.services import DoctorService
	return DoctorService(DoctorRepository())


@router.get("/", response_class=HTMLResponse)
def list_doctors(request: Request):
	service = get_doctor_service()
	doctors = service.get_all_doctors()
	return templates.TemplateResponse("doctors/list.html", {"request": request, "doctors": doctors})


@router.get("/create", response_class=HTMLResponse)
def create_doctor_form(request: Request):
	return templates.TemplateResponse("doctors/form.html", {"request": request, "doctor": None})


@router.post("/create")
def create_doctor(
	first_name: str = Form(...),
	specialization: str = Form(...)
):
	service = get_doctor_service()
	service.create_doctor(first_name, specialization)
	return RedirectResponse(url="/doctors/", status_code=303)


@router.get("/edit/{doctor_id}", response_class=HTMLResponse)
def edit_doctor_form(request: Request, doctor_id: int):
	service = get_doctor_service()
	doctor = service.get_doctor_by_id(doctor_id)
	return templates.TemplateResponse("doctors/form.html", {"request": request, "doctor": doctor})


@router.post("/edit/{doctor_id}")
def edit_doctor(
	doctor_id: int,
	first_name: str = Form(...),
	specialization: str = Form(...)
):
	service = get_doctor_service()
	service.update_doctor(doctor_id, first_name, specialization)
	return RedirectResponse(url="/doctors/", status_code=303)


@router.post("/delete/{doctor_id}")
def delete_doctor(doctor_id: int):
	service = get_doctor_service()
	service.delete_doctor(doctor_id)
	return RedirectResponse(url="/doctors/", status_code=303)
