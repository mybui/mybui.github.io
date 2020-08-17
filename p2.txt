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
    exInsID      TEXT     NOT NULL
                          PRIMARY KEY,
    exStartTime DATETIME,
    exEndTime   DATETIME,
    exGrID      TEXT      REFERENCES ExerciseGroup (exGrID)
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

INSERT INTO Course VALUES (
                       'MS-A0111',
                       'Differential and Integral Calculus 1',
                       5
                   ),
                   (
                       'MS-A0503',
                       'First Course in Probability and Statistics',
                       5
                   );
                   
INSERT INTO CourseInstance VALUES (
                               'MS-A0111-1',
                               '2018-09-10',
                               '2018-10-26',
                               'MS-A0111'
                           ),
                           (
                               'MS-A0111-2',
                               '2019-09-09',
                               '2019-10-23',
                               'MS-A0111'
                           ),
                           (
                               'MS-A0503-1',
                               '2019-01-07',
                               '2019-02-20',
                               'MS-A0503'
                           ),
                           (
                               'MS-A0503-2',
                               '2020-01-07',
                               '2020-02-19',
                               'MS-A0503'
                           );

INSERT INTO Lecture VALUES (
                        'MS-A0111-1-L1',
                        '2018-09-10 10:15:00',
                        '2018-09-10 12:00:00',
                        'MS-A0111-1'
                    ),
                    (
                        'MS-A0111-1-L2',
                        '2018-09-12 10:15:00',
                        '2018-09-12 12:00:00',
                        'MS-A0111-1'
                    ),
                    (
                        'MS-A0111-1-L3',
                        '2018-09-17 10:15:00',
                        '2018-09-17 12:00:00',
                        'MS-A0111-1'
                    ),
                    (
                        'MS-A0111-1-L4',
                        '2018-09-19 10:15:00',
                        '2018-09-19 12:00:00',
                        'MS-A0111-1'
                    ),
                    (
                        'MS-A0111-1-L5',
                        '2018-09-24 10:15:00',
                        '2018-09-24 12:00:00',
                        'MS-A0111-1'
                    ),
                    (
                        'MS-A0111-2-L1',
                        '2019-09-09 11:15:00',
                        '2019-09-09 13:00:00',
                        'MS-A0111-2'
                    ),
                    (
                        'MS-A0111-2-L2',
                        '2019-09-11 11:15:00',
                        '2019-09-11 13:00:00',
                        'MS-A0111-2'
                    ),
                    (
                        'MS-A0111-2-L3',
                        '2019-09-16 11:15:00',
                        '2019-09-16 13:00:00',
                        'MS-A0111-2'
                    ),
                    (
                        'MS-A0111-2-L4',
                        '2019-09-18 11:15:00',
                        '2019-09-18 13:00:00',
                        'MS-A0111-2'
                    ),
                    (
                        'MS-A0111-2-L5',
                        '2019-09-23 11:15:00',
                        '2019-09-23 13:00:00',
                        'MS-A0111-2'
                    ),
                    (
                        'MS-A0503-1-L1',
                        '2019-01-09 08:15:00',
                        '2019-01-09 10:00:00',
                        'MS-A0503-1'
                    ),
                    (
                        'MS-A0503-1-L2',
                        '2019-01-11 08:15:00',
                        '2019-01-11 10:00:00',
                        'MS-A0503-1'
                    ),
                    (
                        'MS-A0503-1-L3',
                        '2019-01-16 08:15:00',
                        '2019-01-16 10:00:00',
                        'MS-A0503-1'
                    ),
                    (
                        'MS-A0503-1-L4',
                        '2019-01-18 08:15:00',
                        '2019-01-18 10:00:00',
                        'MS-A0503-1'
                    ),
                    (
                        'MS-A0503-1-L5',
                        '2019-01-23 08:15:00',
                        '2019-01-23 10:00:00',
                        'MS-A0503-1'
                    ),
                    (
                        'MS-A0503-2-L1',
                        '2020-01-08 09:15:00',
                        '2020-01-08 11:00:00',
                        'MS-A0503-2'
                    ),
                    (
                        'MS-A0503-2-L2',
                        '2020-01-10 09:15:00',
                        '2020-01-10 11:00:00',
                        'MS-A0503-2'
                    ),
                    (
                        'MS-A0503-2-L3',
                        '2020-01-15 09:15:00',
                        '2020-01-15 11:00:00',
                        'MS-A0503-2'
                    ),
                    (
                        'MS-A0503-2-L4',
                        '2020-01-16 09:15:00',
                        '2020-01-16 11:00:00',
                        'MS-A0503-2'
                    ),
                    (
                        'MS-A0503-2-L5',
                        '2020-01-22 09:15:00',
                        '2020-01-22 11:00:00',
                        'MS-A0503-2'
                    );

INSERT INTO ExerciseGroup VALUES (
                        'MS-A0111-1-H1',
                        'H1',
                        '15',
                        '13',
                        'MS-A0111-1'
                    ),
                    (
                        'MS-A0111-1-H2',
                        'H2',
                        '10',
                        '8',
                        'MS-A0111-1'
                    ),
                    (
                        'MS-A0111-2-H1',
                        'H1',
                        '10',
                        '9',
                        'MS-A0111-2'
                    ),
                    (
                        'MS-A0111-2-H2',
                        'H2',
                        '20',
                        '17',
                        'MS-A0111-2'
                    ),
                    (
                        'MS-A0503-1-V1',
                        'V1',
                        '30',
                        '29',
                        'MS-A0503-1'
                    ),
                    (
                        'MS-A0503-1-V2',
                        'V2',
                        '22',
                        '20',
                        'MS-A0503-1'
                    ),
                    (
                        'MS-A0503-2-V1',
                        'V1',
                        '45',
                        '44',
                        'MS-A0503-2'
                    ),
                    (
                        'MS-A0503-2-V2',
                        'V2',
                        '30',
                        '28',
                        'MS-A0503-2'
                    );
                    
INSERT INTO ExerciseInstance VALUES (
                        'MS-A0111-1-H1-1',
                        '2018-09-13 14:15:00',
                        '2018-09-13 16:00:00',
                        'MS-A0111-1-H1'
                    ),
                    (
                        'MS-A0111-1-H1-2',
                        '2018-09-15 14:15:00',
                        '2018-09-15 16:00:00',
                        'MS-A0111-1-H1'
                    ),
                    (
                        'MS-A0111-1-H1-3',
                        '2018-09-20 14:15:00',
                        '2018-09-20 16:00:00',
                        'MS-A0111-1-H1'
                    ),
                    (
                        'MS-A0111-1-H1-4',
                        '2018-09-22 14:15:00',
                        '2018-09-22 16:00:00',
                        'MS-A0111-1-H1'
                    ),
                    (
                        'MS-A0111-1-H1-5',
                        '2018-09-27 14:15:00',
                        '2018-09-27 16:00:00',
                        'MS-A0111-1-H1'
                    ),
                    (
                        'MS-A0111-1-H2-1',
                        '2018-09-12 14:15:00',
                        '2018-09-12 16:00:00',
                        'MS-A0111-1-H2'
                    ),
                    (
                        'MS-A0111-1-H2-2',
                        '2018-09-14 14:15:00',
                        '2018-09-14 16:00:00',
                        'MS-A0111-1-H2'
                    ),
                    (
                        'MS-A0111-1-H2-3',
                        '2018-09-19 14:15:00',
                        '2018-09-19 16:00:00',
                        'MS-A0111-1-H2'
                    ),
                    (
                        'MS-A0111-1-H2-4',
                        '2018-09-21 14:15:00',
                        '2018-09-21 16:00:00',
                        'MS-A0111-1-H2'
                    ),
                    (
                        'MS-A0111-1-H2-5',
                        '2018-09-26 14:15:00',
                        '2018-09-26 16:00:00',
                        'MS-A0111-1-H2'
                    ),
                    (   'MS-A0111-2-H1-1',
                        '2019-09-16 15:15:00',
                        '2019-09-16 17:00:00',
                        'MS-A0111-2-H1'
                    ),
                    (
                        'MS-A0111-2-H1-2',
                        '2019-09-18 15:15:00',
                        '2019-09-18 17:00:00',
                        'MS-A0111-2-H1'
                    ),
                    (
                        'MS-A0111-2-H1-3',
                        '2019-09-23 15:15:00',
                        '2019-09-23 17:00:00',
                        'MS-A0111-2-H1'
                    ),
                    (
                        'MS-A0111-2-H1-4',
                        '2019-09-25 15:15:00',
                        '2019-09-25 17:00:00',
                        'MS-A0111-2-H1'
                    ),
                    (
                        'MS-A0111-2-H1-5',
                        '2019-09-30 15:15:00',
                        '2019-09-30 17:00:00',
                        'MS-A0111-2-H1'
                    ),
                    (
                        'MS-A0111-2-H2-1',
                        '2019-09-11 15:15:00',
                        '2019-09-11 17:00:00',
                        'MS-A0111-2-H2'
                    ),
                    (
                        'MS-A0111-2-H2-2',
                        '2019-09-13 14:15:00',
                        '2019-09-13 16:00:00',
                        'MS-A0111-2-H2'
                    ),
                    (
                        'MS-A0111-2-H2-3',
                        '2019-09-18 14:15:00',
                        '2019-09-18 16:00:00',
                        'MS-A0111-2-H2'
                    ),
                    (
                        'MS-A0111-2-H2-4',
                        '2019-09-20 14:15:00',
                        '2019-09-20 16:00:00',
                        'MS-A0111-2-H2'
                    ),
                    (
                        'MS-A0111-2-H2-5',
                        '2019-09-25 14:15:00',
                        '2019-09-25 16:00:00',
                        'MS-A0111-2-H2'
                    );
                    
INSERT INTO Test VALUES (
                     'MS-A0111-1-T1',
                     '2018-11-26 09:00:00',
                     '2018-11-26 12:00:00',
                     23,
                     'MS-A0111'
                 ),
                 (
                     'MS-A0111-1-T2',
                     '2019-01-26 09:00:00',
                     '2019-01-26 12:00:00',
                     13,
                     'MS-A0111'
                 ),
                 (
                     'MS-A0111-2-T1',
                     '2019-11-27 09:00:00',
                     '2019-11-27 12:00:00',
                     29,
                     'MS-A0111'
                 ),
                 (
                     'MS-A0111-2-T2',
                     '2020-01-27 09:00:00',
                     '2020-01-27 12:00:00',
                     19,
                     'MS-A0111'
                 ),
                 (
                     'MS-A0503-1-T1',
                     '2019-03-20 10:00:00',
                     '2019-03-20 13:00:00',
                     51,
                     'MS-A0503'
                 ),
                 (
                     'MS-A0503-1-T2',
                     '2019-05-20 10:00:00',
                     '2019-05-20 13:00:00',
                     9,
                     'MS-A0503'
                 ),
                 (
                     'MS-A0503-2-T1',
                     '2020-03-20 10:00:00',
                     '2020-03-20 13:00:00',
                     74,
                     'MS-A0503'
                 ),
                 (
                     'MS-A0503-2-T2',
                     '2020-05-20 10:00:00',
                     '2020-05-20 13:00:00',
                     9,
                     'MS-A0503'
                 );
                 
INSERT INTO Student VALUES (
                        'A. P.',
                        'S1',
                        '2000-12-01',
                        'Program A',
                        2018,
                        2025
                    ),
                    (
                        'C. D.',
                        'S2',
                        '2000-11-01',
                        'Program A',
                        2018,
                        2025
                    ),
                    (
                        'G. E.',
                        'S3',
                        '2000-09-01',
                        'Program B',
                        2019,
                        2026
                    ),
                    (
                        'D. T.',
                        'S4',
                        '2000-07-01',
                        'Program B',
                        2019,
                        2026
                    ),
                    (
                        'R. G.',
                        'S5',
                        '2000-05-01',
                        'Program A',
                        2018,
                        2025
                    );

INSERT INTO Building VALUES (
                         'B1',
                         'TUAS',
                         'Zone A2'
                     ),
                     (
                         'B2',
                         'CS',
                         'Zone A1'
                     );

CREATE TRIGGER updateNoStuReg
         AFTER INSERT
            ON Enrollment
BEGIN
    UPDATE ExerciseGroup
       SET currentNoStuEx = currentNoStuEx + 1
     WHERE exGrID = NEW.exGrID;
    UPDATE ExerciseGroup
       SET currentNoStuEx = (
               SELECT MAX(currentNoStuEx) 
                 FROM ExerciseGroup
           )
     WHERE exGrID = NEW.exGrID;
END;

CREATE TRIGGER updateSeatsForTest
         AFTER INSERT
            ON Reservation
BEGIN
    UPDATE Room
       SET noSeatTestBooked = noSeatTestBooked + (
                                                     SELECT noStuRegTest
                                                       FROM Test
                                                      WHERE NEW.testID = testID
                                                 )
     WHERE roomID = NEW.roomID;
END;

CREATE TRIGGER checkOverlappedAndCrowded
        BEFORE INSERT
            ON Reservation
BEGIN
    SELECT CASE WHEN (
                         SELECT COUNT(resID) 
                           FROM Reservation
                          WHERE (NEW.resStartTime BETWEEN resStartTime AND resEndTime OR 
                                 NEW.resEndTime BETWEEN resEndTime AND resEndTime OR 
                                 (NEW.resStartTime < resStartTime AND 
                                  NEW.resEndTime > resEndTime) OR 
                                 (NEW.resStartTime > resStartTime AND 
                                  NEW.resEndTime < resEndTime) ) > 0
                     )
AND 
                     NEW.resType != 'test' THEN RAISE(ABORT, "invalid reservation, please choose another time interval") END;
    SELECT CASE WHEN NEW.resType = 'exercise' AND 
                     ( (
                           SELECT noStuRegEx
                             FROM ExerciseGroup
                            WHERE NEW.exGrID = exGrID
                       )
>                    (
                         SELECT seats
                           FROM Room
                          WHERE roomID = NEW.roomID
                     )
                     ) THEN RAISE(ABORT, "invalid reservation, please choose another room with more seats") END;
END;