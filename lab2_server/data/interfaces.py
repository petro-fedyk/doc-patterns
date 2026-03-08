from abc import ABC, abstractmethod


class IPatientRepository(ABC):

	@abstractmethod
	def get_all(self):
		pass

	@abstractmethod
	def get_by_id(self, patient_id: int):
		pass

	@abstractmethod
	def create(self, patient):
		pass

	@abstractmethod
	def update(self, patient):
		pass

	@abstractmethod
	def delete(self, patient_id: int):
		pass


class IDoctorRepository(ABC):

	@abstractmethod
	def get_all(self):
		pass

	@abstractmethod
	def get_by_id(self, doctor_id: int):
		pass

	@abstractmethod
	def create(self, doctor):
		pass

	@abstractmethod
	def update(self, doctor):
		pass

	@abstractmethod
	def delete(self, doctor_id: int):
		pass


class IExaminationRepository(ABC):

	@abstractmethod
	def get_all(self):
		pass

	@abstractmethod
	def get_by_id(self, exam_id: int):
		pass

	@abstractmethod
	def create(self, exam):
		pass

	@abstractmethod
	def update(self, exam):
		pass

	@abstractmethod
	def delete(self, exam_id: int):
		pass

	@abstractmethod
	def save_examination(self, exam):
		pass


class ITestResultRepository(ABC):

	@abstractmethod
	def get_all(self):
		pass

	@abstractmethod
	def get_by_id(self, result_id: int):
		pass

	@abstractmethod
	def create(self, result):
		pass

	@abstractmethod
	def update(self, result):
		pass

	@abstractmethod
	def delete(self, result_id: int):
		pass
