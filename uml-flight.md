### Construct an UML diagram for an airline reservation system according to the information given below. Mark the key attributes and use the notation taught in the course.

### All flights are recognized by a flight number. No two flights with the same flight number are operated on the same day. However, the flight with the same flight number may have different departure and arrival times on different weekdays. Information of a flight includes information about its time table on various weekdays (we assume that the timetable does not change during the year), the airport of departure and the airport of arrival. Some flights are operated every weekday and some others may be operated just on one or two weekdays, for example. We assume that all flights are direct flights without any extra landings.

### All flights are operated using an aircraft. Information about an aircraft type includes its name, model and the number of passenger seats. The same flight may be operated by using different aircraft types on various days of the year, like a smaller type on Dec 15th and a larger type on Dec 22nd when people are leaving for Christmas holidays. The database contains information about which aircraft type is used to operate a certain flight each day.

### Information about customers contains they customer number (unique), name, title, e- mail address, phone number and the reservations each customer has. A certain customer may have several reservations, and a certain reservation may include several customers and several flights. However, all customers in the same reservation have the same flights. Information about a reservation contains information about the flights (including their dates) and the customers belonging to the reservation as well as a unique reservation number, a reservation date (usually different from the flight date) and status of the reservation (like preliminary or confirmed).

### For the sake of simplicity, the following things are not covered in the UML diagram:
- prices and payments
- baggage
- check-in

#### UML diagram

#### Relations
- Flight (<u>fNumber</u>, <u>fDate</u>, depAirport, weekday, depTime, arrTime)
- Aircraft (<u>aName</u>, <u>model</u>, seat)
- Customer (<u>cNumber</u>, cName, title, email, phone)
- Reservation (<u>rNumber</u>, rDate, status)

#### Associations
- UsesAircraft (<u>fNumber</u>, <u>fDate</u>, <u>aName</u>, <u>model</u>)
- FlightHasReservation (<u>fNumber</u>, <u>fDate</u>, <u>rNumber</u>)
- CustomerHasReservation (<u>rNumber</u>, <u>cNumber</u>)
