from .interfaces import IExaminationRepository
from .database import SessionLocal

class ExaminationRepository(IExaminationRepository):

	def save_examination(self, exam):
		session = SessionLocal()
		session.add(exam)
		session.commit()
		session.close()
