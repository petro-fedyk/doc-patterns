from abc import ABC, abstractmethod

class IApplication(ABC):

	@abstractmethod
	def run(self):
		pass

	@abstractmethod
	def show_statistics(self):
		pass

class PresentationApp(IApplication):
	def __init__(self, service):
		self.service = service

	def run(self):
		print("Starting import from CSV...")
		self.service.import_from_csv("data.csv")
		print("Import complete.")

	def show_statistics(self):
		stats = self.service.get_statistics()
		print("Statistics:")
		for k, v in stats.items():
			print(f"{k}: {v}")
