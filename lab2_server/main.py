from data.database import Base, engine
from data.repositories import ExaminationRepository
from business.services import ExaminationService
from presentation.app_interface import PresentationApp

Base.metadata.create_all(bind=engine)

repository = ExaminationRepository()
service = ExaminationService(repository)
app = PresentationApp(service)

if __name__ == "__main__":
	app.run()
	app.show_statistics()
