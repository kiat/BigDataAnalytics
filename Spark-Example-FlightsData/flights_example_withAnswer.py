
# https://s3.amazonaws.com/metcs777/flights.csv.bz2
# s3n://metcs777/flights.csv.bz2
# lines = sc.textFile("file:///home/kia/Data/Collected-Datasets/flight-delays/flight-delays/flights.csv")

lines = sc.textFile("s3://metcs777/flights.csv.bz2")

# lines = sc.textFile("/Users/kiat/datasets/flightData/flights.csv")

# Removing the Header Line from CSV file 
linesHeader = lines.first()
header = sc.parallelize([linesHeader])
linesWithOutHeader = lines.subtract(header)


linesWithOutHeader.take(1)

# The data is about the flights from different airports which includes following attributes
#[u'YEAR,MONTH,DAY,DAY_OF_WEEK,AIRLINE,FLIGHT_NUMBER,TAIL_NUMBER,ORIGIN_AIRPORT,DESTINATION_AIRPORT,SCHEDULED_DEPARTURE,DEPARTURE_TIME,DEPARTURE_DELAY,TAXI_OUT,WHEELS_OFF,SCHEDULED_TIME,ELAPSED_TIME,AIR_TIME,DISTANCE,WHEELS_ON,TAXI_IN,SCHEDULED_ARRIVAL,ARRIVAL_TIME,ARRIVAL_DELAY,DIVERTED,CANCELLED,CANCELLATION_REASON,AIR_SYSTEM_DELAY,SECURITY_DELAY,AIRLINE_DELAY,LATE_AIRCRAFT_DELAY,WEATHER_DELAY']

flights = linesWithOutHeader.map(lambda x: x.split(','))
flights.take(1)

# YEAR,MONTH,DAY,DAY_OF_WEEK,AIRLINE,FLIGHT_NUMBER,TAIL_NUMBER,ORIGIN_AIRPORT,DESTINATION_AIRPORT,SCHEDULED_DEPARTURE,DEPARTURE_TIME,DEPARTURE_DELAY, CANCELLED

mainFlightsData = flights.map(lambda p: (p[0], p[1] , p[2] , p[3], p[4] , p[5] , p[6], p[7] , p[8] , p[9], p[10], p[11], p[24] ))

# Index number 7 is ORIGIN_AIRPORT
flightsFromBoston = mainFlightsData.filter(lambda p: True if p[7] == "BOS" else False )
flightsFromBoston.take(1)


# Get the total number of Flights from BOS 
flightsFromBoston.count()

# 107847 flights from Logan Airport in Boston 

# Find the subset of flights departing on the weekend.
weekEndFlights = flightsFromBoston.filter(lambda p: True if (int(p[3]) == 6 or int(p[3]) ==7) else False )
weekEndFlights.count()
# 26092


#Q1 Find a list of Origin Airports
originAirports=mainFlightsData.map(lambda p: p[7] ).distinct()
listOfOriginAirports=originAirports.collect()

#Q2 Find a list of (Origin, Destination) pairs
originDestinationAirports=mainFlightsData.map(lambda p: (p[7],p[8]) ).distinct().collect()



#Q3 Find the Origin airport which had the largest departure delay in the month of January
mainFlightsData.filter(lambda p: True if p[1] == "1" else False ).map(lambda p: (p[11], p[7])).top(1)

#Q4 Find out which carrier has the largest delay on Weekends. 
weekEndFlights.map(lambda p: (p[4], list(p[11]))).top(1)

#Q5 Which airport has the most cancellation of flights? (based on ORIGIN_AIRPORT)
# Index 12 is the cancellation flag, 1 means cancelled 
# index 7 is ORIGIN_AIRPORT
from operator import add

airportWithHighestCancellation= mainFlightsData.map(lambda p: (p[7],  1 ) if p[12] == "1" else (p[7],  0 )).reduceByKey(add).top(1, lambda x:x[1])
print(airportWithHighestCancellation)
#Q6 Find the percent of flights cancelled for each carrier.
# Index 12 is the cancellation flag, 1 means cancelled 
# Index 4 is the carrier 

# do the following import to get the division correct 
from __future__ import division

percentOfFlightsCancelled = mainFlightsData.map(lambda p: (p[4], (int(p[12]), 1))).reduceByKey(lambda a, b: (a[0]+b[0], a[1]+b[1])).map(lambda (c, (ca, t)): (c, float(ca)/t) ).collect()

OR

percentOfFlightsCancelled = mainFlightsData.map(lambda p: (p[4], (1 ,  1) ) if p[12] == "1" else (p[4], (0 , 1))).reduceByKey(lambda a, b: (a[0]+b[0], a[1]+b[1])).map(lambda (c, (ca, t)): (c, (float(ca)/t)) ).collect()


#Q7 Find the largest departure delay for each carrier                    
# Index 4  is the carrier ID 
# Index 11 is DEPARTURE_DELAY

mainFlightsData.map(lambda p: (p[4], p[11])).reduceByKey(lambda t1, t2: max(t1, t2) ).collect() 


#Q8 Find the largest departure delay for each carrier for each month
# SOLUTION: like above but create a new Key for each carrier-month


#Q9 For each carrier find the average Departure delay 

# For each carrier find the average Departure delay 
# Index 11 is DEPARTURE_DELAY

# First filter out all flights that have departure delay 
mainFlightsData.filter(lambda p: True if float(p[11])> 0 else False ).map(lambda p: (p[4], (p[11], 1))).reduceByKey(lambda a, b: (a[0]+b[0], a[1]+b[1])).take(2)

# PROBLEM: p[11] should be checked before parsing to float. The string can be anything that is not parsable to float. 

    
                    
#Q10 For each carrier find the average Departure delay for each month
# SOLUTION: like above but create a new Key for each carrier-month

                    
#Q11 Which date of year has the highest rate  of flight cancellations?
# Rate of flight cancellation is calculated by deviding number of canceled flights by total number of flights.
                    
                    
#Q12 Calculate the number of flights to each destination state

                    
#Q13 For each carrier, for which state do they have the largest average delay? 
# You will need the airline and airport data sets for this question. 

# AirLine dataset https://s3.amazonaws.com/metcs777/airlines.csv or s3://metcs777/airlines.csv
# Airport dataset https://s3.amazonaws.com/metcs777/airports.csv or s3://metcs777/airports.csv 


# Airport Dataset
# IATA_CODE,AIRPORT,CITY,STATE,COUNTRY,LATITUDE,LONGITUDE
# ABE,Lehigh Valley International Airport,Allentown,PA,USA,40.65236,-75.44040
# ABI,Abilene Regional Airport,Abilene,TX,USA,32.41132,-99.68190
# Index 0 is IATA_CODE for Airport 
# Index 3 is states  
                    
                    
lines2 = sc.textFile("/Users/kiat/datasets/flightData/airports.csv")
# Removing the Header Line from CSV file 
linesHeader2 = lines2.first()
header2 = sc.parallelize([linesHeader])
linesWithOutHeader2 = lines2.subtract(header2)


linesWithOutHeader2.take(1)
                    
airports=linesWithOutHeader2.map(lambda x: x.split(','))
                   
destAirportState=airports.map(lambda x: (x[0], x[3]))

flightsToAirports=mainFlightsData.map(lambda x: (x[7], 1))                    

flightsToAirports.join(destAirportState).map(lambda x: (x[1][1], x[1][0])).reduceByKey(add).collect()                    


                    
                    
