
# https://s3.amazonaws.com/metcs777/flights.csv.bz2
# s3n://metcs777/flights.csv.bz2
# lines = sc.textFile("file:///home/kia/Data/Collected-Datasets/flight-delays/flight-delays/flights.csv")

lines = sc.textFile("s3://metcs777/flights.csv.bz2")


# Removing the Header Line from CSV file 
linesHeader = lines.first()
header = sc.parallelize([linesHeader])
linesWithOutHeader = lines.subtract(header)

# The data is about the flights from different airports which includes following attributes
#[u'YEAR,MONTH,DAY,DAY_OF_WEEK,AIRLINE,FLIGHT_NUMBER,TAIL_NUMBER,ORIGIN_AIRPORT,DESTINATION_AIRPORT,SCHEDULED_DEPARTURE,DEPARTURE_TIME,DEPARTURE_DELAY,TAXI_OUT,WHEELS_OFF,SCHEDULED_TIME,ELAPSED_TIME,AIR_TIME,DISTANCE,WHEELS_ON,TAXI_IN,SCHEDULED_ARRIVAL,ARRIVAL_TIME,ARRIVAL_DELAY,DIVERTED,CANCELLED,CANCELLATION_REASON,AIR_SYSTEM_DELAY,SECURITY_DELAY,AIRLINE_DELAY,LATE_AIRCRAFT_DELAY,WEATHER_DELAY']

flights = linesWithOutHeader.map(lambda x: x.split(','))



# YEAR,MONTH,DAY,DAY_OF_WEEK,AIRLINE,FLIGHT_NUMBER,TAIL_NUMBER,ORIGIN_AIRPORT,DESTINATION_AIRPORT,SCHEDULED_DEPARTURE,DEPARTURE_TIME,DEPARTURE_DELAY, CANCELLED

mainFlightsData = flights.map(lambda p: (p[0], p[1] , p[2] , p[3], p[4] , p[5] , p[6], p[7] , p[8] , p[9], p[10], p[11], p[24] ))

# number 6 is ORIGIN_AIRPORT
flightsFromBoston = mainFlightsData.filter(lambda p: True if p[7] == "BOS" else False )


# Get the total number of Flights from BOS 
flightsFromBoston.count()

# 107847 flights from Logan Airport in Boston 

# Find the subset of flights departing on the weekend.
weekEndFlights = flightsFromBoston.filter(lambda p: True if (int(p[3]) == 6 or int(p[3]) ==7) else False )
weekEndFlights.count()
# 26092


#Q1 Find a list of Origin Airports


#Q2 Find a list of (Origin, Destination) pairs


#Q3 Find the Origin airport which had the largest departure delay in the month of January


#Q4 Find out which carrier has the largest delay on Weekends. 


#Q5 Which airport has the most cancellation of flights?


#Q6 Find the percent of flights cancelled for each carrier.


#Q7 Find the largest departure delay for each carrier


#Q8 Find the largest departure delay for each carrier for each month


#Q9 For each carrier find the average Departure delay 


#Q10 For each carrier find the average Departure delay for each month



#Q11 Which date of year has the highest rate  of flight cancellations?
# Rate of flight cancellation is calculated by deviding number of canceled flights by total number of flights.


#Q12 Calculate the number of flights to each destination state
# For each carrier, for which state do they have the largest average delay? 
# You will need the airline and airport data sets for this question. 

# AirLine dataset https://s3.amazonaws.com/metcs777/airlines.csv or s3://metcs777/airlines.csv
# Airport dataset https://s3.amazonaws.com/metcs777/airports.csv or s3://metcs777/airports.csv 




# add your own questions. 








