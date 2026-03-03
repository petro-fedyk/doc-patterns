from abc import ABC, abstractmethod

class IExaminationService(ABC):

	@abstractmethod
	def import_from_csv(self, path: str):
		pass

	@abstractmethod
	def get_statistics(self):
		pass
