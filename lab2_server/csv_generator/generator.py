import csv
import random
from faker import Faker

def generate_csv():
	fake = Faker()
	with open("data.csv", "w", newline="") as file:
		writer = csv.writer(file)

		writer.writerow([
			"patient_first_name",
			"patient_last_name",
			"email",
			"doctor_name",
			"specialization",
			"status",
			"file_type",
			"file_path"
		])

		specializations = ["Oncology", "Cardiology", "Neurology", "Pediatrics", "Surgery"]
		statuses = ["COMPLETED", "PENDING", "CANCELLED"]
		file_types = ["PDF", "JPEG", "VIDEO"]

		for i in range(1000):
			writer.writerow([
				fake.first_name(),
				fake.last_name(),
				fake.unique.email(),
				fake.name(),
				random.choice(specializations),
				random.choice(statuses),
				random.choice(file_types),
				f"/files/result{i}.{random.choice(['pdf','jpg','mp4'])}"
			])

if __name__ == "__main__":
	generate_csv()
