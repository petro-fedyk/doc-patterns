from abc import ABC, abstractmethod


class IPatientService(ABC):

	@abstractmethod
	def get_all_patients(self):
		pass

	@abstractmethod
	def get_patient_by_id(self, patient_id: int):
		pass

	@abstractmethod
	def create_patient(self, first_name: str, last_name: str, email: str):
		pass

	@abstractmethod
	def update_patient(self, patient_id: int, first_name: str, last_name: str, email: str):
		pass

	@abstractmethod
	def delete_patient(self, patient_id: int):
		pass


class IDoctorService(ABC):

	@abstractmethod
	def get_all_doctors(self):
		pass

	@abstractmethod
	def get_doctor_by_id(self, doctor_id: int):
		pass

	@abstractmethod
	def create_doctor(self, first_name: str, specialization: str):
		pass

	@abstractmethod
	def update_doctor(self, doctor_id: int, first_name: str, specialization: str):
		pass

	@abstractmethod
	def delete_doctor(self, doctor_id: int):
		pass


class IExaminationService(ABC):

	@abstractmethod
	def get_all_examinations(self):
		pass

	@abstractmethod
	def get_examination_by_id(self, exam_id: int):
		pass

	@abstractmethod
	def create_examination(self, patient_id: int, doctor_id: int, status: str):
		pass

	@abstractmethod
	def update_examination(self, exam_id: int, patient_id: int, doctor_id: int, status: str):
		pass

	@abstractmethod
	def delete_examination(self, exam_id: int):
		pass

	@abstractmethod
	def import_from_csv(self, path: str):
		pass

	@abstractmethod
	def get_statistics(self):
		pass


class ITestResultService(ABC):

	@abstractmethod
	def get_all_results(self):
		pass

	@abstractmethod
	def get_result_by_id(self, result_id: int):
		pass

	@abstractmethod
	def create_result(self, examination_id: int, file_type: str, file_path: str):
		pass

	@abstractmethod
	def update_result(self, result_id: int, examination_id: int, file_type: str, file_path: str):
		pass

	@abstractmethod
	def delete_result(self, result_id: int):
		pass
