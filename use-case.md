# Use Case Specification  
## Allscripts Cancer Detection System

![picture of diagram](<use-case.png>)

---

## 1. Primary Actor
**Doctor**

---

## 2. Secondary Actors
- Patient  
- Lab Technician  
- Lab Equipment  
- Central Server  

---

## 3. Preconditions
- Patient is registered in the system  
- Doctor is authenticated  
- System is operational  
- Network connection is available  

---

## 4. Main Use Case  
### Conduct Cancer Examination

### Included Use Cases (<<include>>)
The main use case **includes** the following mandatory sub-processes:

- Register Patient  
- Authenticate User  
- Prescribe Examination  
- Schedule Test  
- Perform Test  
- Upload Test Result  
- Store Results  
- Review Results  
- Create Medical Report  
- View Medical Report  
- Generate Test Result File  

---

## 5. Main Flow

1. Doctor authenticates in the system.  
2. Doctor selects patient profile.  
3. If the patient is not registered → Register Patient is executed.  
4. Doctor prescribes required diagnostic examinations.  
5. Patient schedules the test.  
6. Lab Technician performs the test.  
7. Lab Equipment generates a test result file (PDF / JPEG / Video).  
8. Test results are uploaded to the Central Server.  
9. System validates the file.  
10. Results are stored in the database.  
11. Doctor reviews results.  
12. Doctor creates medical report.  
13. Patient views medical report.  

---

## 6. Alternative Flows (<<extend>>)

### A1 – Cancel Appointment
Patient cancels scheduled test.

### A2 – Reschedule Appointment
Patient reschedules the examination date.

### A3 – Repeat Test
If test results are unclear, the test is repeated.

### A4 – Emergency Examination
Urgent examination bypassing standard scheduling.

### A5 – Request Additional Tests
Doctor requests additional diagnostic procedures after reviewing results.

---

## 7. Exception Flows (<<extend>>)

### E1 – Network Failure
Network connection is lost during upload of test results.

### E2 – File Validation Error
Uploaded file is corrupted or has invalid format.

### E3 – Database Storage Error
System fails to store results in database.

---

## 8. System Interactions

### Lab Equipment
- Generates test result files  
- Sends files to Central Server  

### Central Server
- Receives test results  
- Validates files  
- Stores results in database  

---

## 9. Related Use Cases

### Register Patient
Registers a new patient in the system.

### Authenticate User
Authenticates Doctor before accessing system.

### Schedule Test
Schedules laboratory examination.

### Perform Test
Execution of laboratory or imaging diagnostic procedure.

### Upload Test Result
Transfers diagnostic files to server.

### Store Results
Persists validated results in database.

### Review Results
Doctor analyzes stored diagnostic data.

### Create Medical Report
Doctor creates official medical diagnosis report.

### View Medical Report
Patient accesses final report.
