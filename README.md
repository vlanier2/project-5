# UOCIS322 - Project 5 #
Brevet time calculator with MongoDB!

NAME: Vincent Lanier

CONTACT: vlanier@uoregon.edu

## Project Description

This project consists of a web application that is based on RUSA's online calculator. The algorithm for calculating control times is described here https://rusa.org/pages/acp-brevet-control-times-calculator. Additional background information is given here https://rusa.org/pages/rulesForRiders.

The webpage contains a spreadsheet for calculating start and end times for control points in a given brevet. After a control point distance is given, the spreadsheet automatically updates without refresh. The project makes use of AJAX, JQuery, and bootstrap for a dynamic webpage. A flask server supplies the page template and responds to AJAX queries to update control point times. 

New in project 5 - An additonal container running MongoDB is added to save and recover brevet data. Once a brevet is entered, the submit button will insert the brevet data into the database and clear the form. The display button will recover the previously added brevet. Only one brevet is saved at a time. Docker compose is used to connect the two containers in the full application (see setup).

## Algorithm

A control's opening time is found by dividing its kilometer placement by the maximum speed given by the table below.
A control's closing time is found by dividing its kilometer placement by the minimum speed given by the table below.

This calculation produces a time in hours. To convert into hours and minutes we multiply the fractional part by 60 minutes.

The table below gives the minimum and maximum speeds for ACP brevets.

| Control location (km) | Minimum Speed (km/hr) | Maximum Speed (km/hr) |
| --- | --- | --- |
| 0 - 200 | 15 | 34 |
| 200 - 400 | 15 | 32 |
| 400 - 600 | 15 | 30 |
| 600 - 1000 | 11.428 | 28 |
| 1000 - 1300 | 13.333 | 26 |


The calculator converts all inputs expressed in units of miles to kilometers and truncates the result to the nearest kilometer before being used in calculations. Kilometer values are rounded to the nearest kilometer before being used in calculations. Times are rounded to the nearest minute after all calculations are complete.

### Calculating Times Across Multiple Speed Ranges

Calculation of control times that fall beyond 200km is more complex. The following example comes from https://rusa.org/pages/acp-brevet-control-times-calculator.

"Consider a control at 350km. We have 200/34 + 150/32 = 5H53 + 4H41 = 10H34. The 200/34 gives us the minimum time to complete the first 200km while the 150/32 gives us the minimum time to complete the next 150km. The sum gives us the control's opening time."

### Special Exceptions

The closing time for the starting point (at 0km) is one hour after the official start.

Overall time limits for each brevet are: (in hours and minutes, HH:MM) 13:30 for 200 KM, 20:00 for 300 KM, 27:00 for 400 KM, 40:00 for 600 KM, and 75:00 for 1000 KM. These are used as closing times for the final control point regardless if the final control is located beyond the total brevet distance. Final control points are allowed by rule to be 20% further than the total brevet distance.

The closing time for a control within the first 60km is based on 20 km/hr, plus 1 hour. This is to ensure points within 60km do not close during the open period of the start at 0km.

## Setup

### ~~Supplying a Credentials File~~

~~credentials-skel.ini should be replaced by a credentials.ini file specifying the port and debug mode. If no credentials file is provided, it defaults to port 5000 and debug=True. *Note: The credentials.ini file should be placed in the /brevets directory so it can be accessed within the container.~~
*** Supplying a credentials file is no longer required. It can still be used to set debug, however specifying a port could cause conflicts with docker compose.
*** You can set desired ports by editing docker-compose.yml instead of supplying a credentials file.

### Building Containers / Startup

Build and run the application using docker compose

```
docker compose up --build
```

## Usage

With the container running, navigate to localhost:<port> (default 5000) to open the brevet checkpoint spreadsheet. Select a total brevet distance, start date, and time at the top of the page. Then enter checkpoint distances in miles or kilometers. The times for each checkpoint will fill in response to a new kilometer distance being entered.

To save your brevet, click the submit button in the top right.

NOTE: A few rules have been added to ensure a valid brevet 

- The form must not be completely empty. At least one checkpoint must exist.
- Checkpoint distances must be increasing from top to bottom.
- The final checkpoint distance can be at most 120% of the total brevet distance.

On submission of an invalid brevet a popup will show and the brevet will not be saved.

To recover the previously entered brevet, click the display button in the top right. A popup will show if there is no saved brevet.

## Testing

Six tests of the brevet time computation are included. Along with two tests of insert and fetch to the mongoDB.

Tests can be run with the following command after starting the containers.

```
docker compose exec brevets ./run_tests.sh
```

or 

```
docker compose exec brevets nosetests
```

## Shutting Down

Simply shut down the flask app with ctrl-c in your terminal, and/or stop the running docker containers with:

```
docker compose stop
```