Read more [here](./unidb-sql.txt)

### Create tables

CREATE TABLE CourseInstance (
    courseInsID     TEXT NOT NULL
                         PRIMARY KEY,
    courseStartDate DATE,
    courseEndDate   DATE,
    courseCode      TEXT
);

CREATE TABLE Lecture (
    lecID        TEXT     NOT NULL
                          PRIMARY KEY,
    lecStartTime DATETIME,
    lecEndTime   DATETIME,
    courseInsID  TEXT     REFERENCES CourseInstance (courseInsID) 
);

CREATE TABLE ExerciseGroup (
    exGrID       TEXT NOT NULL
                      PRIMARY KEY,
    groupName    TEXT,
    limitNoStuEx INT,
    noStuRegEx   INT,
    courseInsID  TEXT REFERENCES CourseInstance (courseInsID) 
                      CHECK (noStuRegEx <= limitNoStuEx) 
);

CREATE TABLE Course (
    courseCode   TEXT NOT NULL
                      PRIMARY KEY,
    courseName   TEXT,
    courseCredit INT
);

CREATE TABLE Test (
    testID        TEXT     NOT NULL
                           PRIMARY KEY,
    testStartTime DATETIME,
    testEndTime   DATETIME,
    noStuRegTest  INT,
    courseCode    TEXT     REFERENCES Course (courseCode) 
);

CREATE TABLE Building (
    buildingID   TEXT NOT NULL
                      PRIMARY KEY,
    buildingName TEXT,
    buildingAdd  TEXT
);

CREATE TABLE Room (
    roomID           TEXT NOT NULL
                          PRIMARY KEY,
    seats            INT,
    seatsForTest     INT,
    noSeatTestBooked INT,
    equipName        TEXT,
    equipQuantity    INT,
    buildingID       TEXT REFERENCES Building (buildingID) 
                          CHECK (noSeatTestBooked <= seatsForTest) 
);

CREATE TABLE ExerciseInstance (
    exGrID      TEXT     NOT NULL
                         PRIMARY KEY,
    exStartTime DATETIME,
    exEndTime   DATETIME
);

CREATE TABLE Student (
    stuID     TEXT NOT NULL
                   PRIMARY KEY,
    name      TEXT,
    DOB       DATE,
    program   TEXT,
    startYear INT,
    endYear   INT
);

CREATE TABLE Enrollment (
    enrID   TEXT     NOT NULL
                     PRIMARY KEY,
    enrTime DATETIME,
    enrType TEXT,
    stuID   TEXT     REFERENCES Student (stuID),
    exGrID  TEXT     REFERENCES ExerciseGroup (exGrID),
    testID  TEXT     REFERENCES Test (testID) 
);

CREATE TABLE Reservation (
    resID        TEXT     NOT NULL
                          PRIMARY KEY,
    resStartTime DATETIME,
    resEndTime   DATETIME,
    resType      TEXT,
    roomID       TEXT     REFERENCES Room (roomID),
    exGrID       TEXT     REFERENCES ExerciseGroup (exGrID),
    lecID        TEXT     REFERENCES Lecture (lecID),
    testID       TEXT     REFERENCES Test (testID) 
);

---

### Create view

CREATE VIEW CourseDetails AS
    SELECT Course.courseCode,
           CourseInstance.courseInsID,
           Lecture.lecID,
           Lecture.lecStartTime,
           ExerciseGroup.exGrID,
           ExerciseGroup.exStartTime
      FROM Course,
           CourseInstance,
           Lecture,
           ExerciseGroup
     WHERE Course.courseCode = CourseInstance.courseCode AND 
           CourseInstance.courseCode = lecID.courseCode AND 
           CourseInstance.courseCode = exGrID.courseCode;

---

### Create indexes

CREATE INDEX courseNameIndex ON Course (
    courseName
);

CREATE INDEX resTimeIndex ON Reservation (
    resStartTime,
    resEndTime
);

CREATE INDEX exTimeIndex ON ExerciseInstance (
    exStartTime,
    exEndTime
);

CREATE INDEX testTimeIndex ON Test (
    testStartTime,
    testEndTime
);

---

### Insert data

To be continued ... 
