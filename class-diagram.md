![alt text](<class-diagram.png>)

# Class Diagram Description  
## Allscripts Cancer Detection System

This class diagram represents the core static structure of the Cancer Detection System.  
It includes the main entities involved in conducting medical examinations and storing their results.

---

## 1. Patient

Represents a person undergoing diagnostic examination.

**Attributes:**
- patientId: int  
- firstName: String  
- lastName: String  
- dateOfBirth: Date  
- gender: String  
- phoneNumber: String  
- email: String  

**Methods:**
- register()  
- scheduleTest(dateTime: DateTime)  
- viewMedicalReport()  

A patient can have multiple examinations.

---


**Methods:**
- performExamination()  
- uploadResults()  

A lab technician condu
## 2. Doctor

Represents a medical professional responsible for prescribing and reviewing examinations.

**Attributes:**
- doctorId: int  
- firstName: String  
- lastName: String  
- specialization: String  
- phoneNumber: String  
- email: String  

**Methods:**
- prescribeExamination()  
- reviewResults()  
- createMedicalReport()  

A doctor can prescribe multiple examinations and review their results.

---

## 3. LabTechnician

Represents a medical 

**Methods:**
- performExamination()  
- uploadResults()  

A lab technician condustaff member who performs examinations.

**Attributes:**
- technicianId: int  
- name: String  

**Methods:**
- performExamination()  
- uploadResults()  

A lab technician conducts examinations and uploads diagnostic results to the system.

---

## 4. Examination (Abstract Class)

Represents a general medical examination.

This class is marked as `<<abstract>>` because a generic examination cannot exist independently — only specific types of examinations can be performed.

**Attributes:**
- examId: int  
- date: Date  
- status: String  

**Methods:**
- conduct()  
- generateResult(): TestResult  

This class demonstrates abstraction and serves as the base class for specific examination types.

---

## 5. BloodTest (extends Examination)

Represents a laboratory blood analysis.

**Attributes:**
- hemoglobinLevel: float  
- whiteBloodCellCount: int  

**Methods:**
- conduct()  
- generateResult(): TestResult  

This class overrides the methods of Examination, demonstrating polymorphism.

---

## 6. MRI (extends Examination)

Represents magnetic resonance imaging diagnostics.

**Attributes:**
- bodyPart: String  
- imageResolution: String  

**Methods:**
- conduct()  
- generateResult(): TestResult  

Like BloodTest, this class overrides the abstract methods from Examination.

---

## 7. TestResult

Represents the result generated after an examination.

**Attributes:**
- resultId: int  
- fileType: String  
- filePath: String  
- uploadDate: Date  

**Methods:**
- validate()  
- getFile()  

Each examination generates exactly one TestResult.

---

## 8. CentralServer

Represents the system component responsible for receiving and storing examination results.

**Attributes:**
- serverId: int  

**Methods:**
- receiveResult()  
- storeResult()  
- sendToDoctor()  

The central server validates and stores diagnostic files and provides access to doctors.

---

## Relationships

- A **Patient** can have multiple **Examinations** (1..*).  
- A **Doctor** can prescribe multiple **Examinations** (1..*).  
- A **LabTechnician** performs multiple **Examinations** (1..*).  
- An **Examination** generates one **TestResult** (1..1).  
- A **TestResult** is processed and stored by the **CentralServer**.  
- **BloodTest** and **MRI** extend the abstract class **Examination**.  

---

## OOP Principles Demonstrated

- **Encapsulation** – private attributes with public methods  
- **Abstraction** – abstract class Examination  
- **Inheritance** – BloodTest and MRI extend Examination  
- **Polymorphism** – overridden conduct() and generateResult() methods  