### In this project we'll implement an unversity database that has the following requirements:
- The database contains information about the courses of the university. For each course, the
information contains the course code, the name, and the number of credits.
- The same course may be organized several times either in the same semester or in different
semesters. Below, we call different implementations of the same course course instances.
- A course may have lectures, exercise groups and exams. The lectures and exercise groups
belong to a certain course instance, the exams belong to the course.
- The time of the lectures of the course instance may vary i.e. they are not necessarily the same
every week.
- The same exercise group may meet several times and the timetable may be different in different
weeks. The group may also have several meetings during the same week.
- A course may have several exams (for example, an exam immediately after a course instance
and retake exams later).
- The student enrolls for a course by enrolling for one of its exercise groups. We assume that
every course instance has at least one exercise group. An exercise group may have a limit for the number of students and the student cannot enroll for the group which has already reached the limit.
- If a student wants to take an exam, he/she has always enroll for it (it is not enough to enroll for a course).
- For each student, the system stores at least the name, student ID, date of birth, degree program, the year the student started his/her studies and the expiration date of study right.
- The university has several buildings, which contain rooms for teaching purposes (like lecture halls and class rooms). They are called rooms below. For each building, the information about its name and street address are stored. The database also contains information about which rooms are located in a certain buiding.
- For each room, the following information is stored: the number of seats, the number of seats in an exam (may be smaller, because the students cannot sit too near each other in the exam), the equipment in the room (like video projector, two video projectors, computer for the teacher, document camera, computers for students etc.) It must be able to store information also about other type of equipment than listed above.
- The database must contain information on the reservations of the rooms. There can been only one exercise group or lecture in a certain room at the same time, but it is possible to have exams of several courses simultaneously in the same room. The reservation for a exam may be longer than the actual exam to give time for practical arrangements.

### The following operations are possible. These operations are not presented in the UML diagram and in the relational model, but it is designed such that the operations are possible:
- Store information about courses, course instances, students, lectures, exercises groups and their times, exams and enrollments.
- Store information about the buildings, rooms and their reservations. The system must also store information about the history of the reservations, for example which exercise group of which course had a reservation for a certain room at a certain time a year ago.
- Search for the courses which are arranged in a certain time interval.
- Find out, which exams a certain course has during a certain time interval.
- Find out, when a certain course has been arranged or when it will be arranged.
- Find the lectures belonging to a certain course instance.
- Find the exercise groups belonging to a certain course instance and find out, when and where a
certain exercise group meets.
- Find a room which has at least a certain number of seats and which is free for reservation at a
certain time.
- Find out for which purpose a certain room is reserved at a certain time.
- Enroll a certain student for a certain exam or exercise group.
- List all students who have enrolled for a certain course instance, exercise group or exam.
- Find out which exercise groups at a certain course instance are not full yet.

### UML modeling

![png](images/p1.png)

### Relational data model

#### Compositions
- CourseInstance (<u>courseInsID</u>, courseStartDate, courseEndDate, courseCode)
- Lecture (<u>lecID</u>, lecStartTime, lecEndTime, courseInsID)
- ExerciseGroup (<u>exGrID</u>, groupName, limitNoStuEx, noStuRegEx, courseInsID)


- Course (<u>courseCode</u>, courseName, courseCredit)
- Test (<u>testID</u>, testStartTime, testEndTime, noStuRegTest, courseCode)


- Building (<u>buildingName</u>, buildingAdd)
- Room (<u>roomID</u>, seats, seatsForTest, noSeatTestBooked, equipName, equipQuantity, buildingName)


#### Hierarchy
- ExerciseGroup (<u>exGrID</u>, groupName, limitNoStuEx, noStuRegEx, courseInsID)
- ExerciseInstance (<u>exGrID</u>, exStartTime, exEndTime)

#### Normal relations
- Student (<u>stuID</u>, name, DOB, program, startYear, endYear)

#### Combined relations with associations
- Enrollment (<u>enrID</u>, enrTime, enrType, stuID, exGrID, testID) combined with associations 'hasEnrollment, enrolCourse, enrolTest'
- Reservation (<u>resID</u>, resStartTime, resEndTime, resType, roomID, exGrID, lecID, testID) combined with associations 'hasReservation, exerciseReservation, lectureReservation, testReservation'

### SQL implementation

#### Check constraints
- ExerciseGroup: noStuRegEx <= limitNoStuEx
- Room: noSeatTestBooked <= seatsForTest

#### Triggers
- Enrollment: after insert, increment noStuRegEx
- Reservation: 
    1. Before insert
        + Check if new time interval overlaps with any current time interval and if new type is not test
        + Check if new type is exercise and the room chosen can contain its noStuRegEx (noStuRegEx <= seats)
    2. After insert
        + Check if new type is test and increment noSeatTestBooked
