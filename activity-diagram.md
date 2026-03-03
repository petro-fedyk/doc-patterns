![alt text](<activity-diagram-part1.png>)
![alt text](<activity-diagram-part2.png>)

# Activity Diagram – Cancer Examination Process

## Description

This activity diagram represents the complete workflow of patient registration, scheduling, conducting examinations, handling emergency situations, processing laboratory results, and organizing a final consultation with the doctor.

The system models real clinical behavior including alternative flows and exceptional situations.

---

## Main Flow

### 1. Patient Registration

1. Start process.
2. Patient requests examination.
3. System checks if patient is registered.
   - If not registered → Register patient.
   - If registered → Continue.

---

### 2. Examination Scheduling

4. Doctor prescribes examination.
5. Patient schedules test.
6. Appointment day arrives.
7. System checks patient presence.
   - If patient is absent → Reschedule or cancel appointment.
   - If patient is present → Continue.

---

### 3. Patient Condition Evaluation

8. System checks patient condition.
   - If condition is critical → Activate emergency flow.
   - If condition is stable → Proceed to laboratory tests.

---

## Emergency Flow

If patient condition worsens:

1. Call emergency team.
2. Hospitalize patient.
3. Doctor provides emergency treatment.
4. Process may terminate or return to examination workflow after stabilization.

---

## Parallel Laboratory Testing

If patient condition is stable:

The process splits into parallel execution (Fork).

### Blood Test Branch

1. Conduct Blood Test.
2. Generate result.
3. Upload result to server.
4. Validate result.

### MRI Branch

1. Conduct MRI.
2. Generate result.
3. Upload result to server.
4. Validate result.

---

## Synchronization

After both tests are completed (Join):

1. System checks if all results are available.
   - If not → Wait for remaining results.
   - If yes → Continue.

---

## Consultation and Reporting

1. Schedule consultation.
2. Doctor reviews results.
3. Doctor creates medical report.
4. Patient receives consultation.
5. End process.

---

## Decision Points Included

- Patient registered?
- Patient present?
- Patient condition stable?
- All results available?

---

## UML Elements Used

- Initial node
- Activity nodes
- Decision nodes
- Fork node (parallel execution)
- Join node (synchronization)
- Alternative flows
- Exception handling