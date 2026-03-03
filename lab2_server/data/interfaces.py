from abc import ABC, abstractmethod

class IExaminationRepository(ABC):

	@abstractmethod
	def save_examination(self, exam):
		pass
