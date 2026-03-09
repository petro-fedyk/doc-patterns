from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/test_results", tags=["Test Results (HTML)"])
templates = Jinja2Templates(directory="templates")


def get_test_result_service():
	from data.repositories import TestResultRepository
	from business.services import TestResultService
	return TestResultService(TestResultRepository())


def get_examination_service():
	from data.repositories import ExaminationRepository
	from business.services import ExaminationService
	return ExaminationService(ExaminationRepository())


@router.get("/", response_class=HTMLResponse)
def list_test_results(request: Request):
	service = get_test_result_service()
	results = service.get_all_results()
	return templates.TemplateResponse("test_results/list.html", {"request": request, "results": results})


@router.get("/create", response_class=HTMLResponse)
def create_test_result_form(request: Request):
	examinations = get_examination_service().get_all_examinations()
	return templates.TemplateResponse("test_results/form.html", {
		"request": request, "result": None, "examinations": examinations
	})


@router.post("/create")
def create_test_result(
	examination_id: int = Form(...),
	file_type: str = Form(...),
	file_path: str = Form(...)
):
	service = get_test_result_service()
	service.create_result(examination_id, file_type, file_path)
	return RedirectResponse(url="/test_results/", status_code=303)


@router.get("/edit/{result_id}", response_class=HTMLResponse)
def edit_test_result_form(request: Request, result_id: int):
	service = get_test_result_service()
	result = service.get_result_by_id(result_id)
	examinations = get_examination_service().get_all_examinations()
	return templates.TemplateResponse("test_results/form.html", {
		"request": request, "result": result, "examinations": examinations
	})


@router.post("/edit/{result_id}")
def edit_test_result(
	result_id: int,
	examination_id: int = Form(...),
	file_type: str = Form(...),
	file_path: str = Form(...)
):
	service = get_test_result_service()
	service.update_result(result_id, examination_id, file_type, file_path)
	return RedirectResponse(url="/test_results/", status_code=303)


@router.post("/delete/{result_id}")
def delete_test_result(result_id: int):
	service = get_test_result_service()
	service.delete_result(result_id)
	return RedirectResponse(url="/test_results/", status_code=303)
