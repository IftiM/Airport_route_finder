""" We have 3 data files to work with: airlines.dat, airports.dat and routes.dat
These files includes all known list of Airlines, Airports, and International Routes.
Our task is to get any two airport code: as source airport and destination airport.
Then we have to find if there's any direct flight between those two routes, if there's
any 2 legged routes between them, and if there's any 3 legged routes between them.

Part of Udacity Intermediate Python Nanodegree excercise

Name: Ifti Mustafa"""

import csv
import json

# Creating a custom dictionary from Airline code -> Airline Name (ie. ADE - Ada Air)
def read_airlines(filename='airlines.dat'):
    airlines = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines

# Creating a custom dictionary from Airport Code -> Airport Name (ie. DXB -Dubai Intl. Airport)
def read_airports(filename='airports.dat'):
    airport = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airport[line[4]] = line[1]
    return airport

# Creating a custom dictionary with all the possible matching routes between all the airports in the database
def read_routes(filename='routes.dat'):
    routes = {}
    with open(filename) as f:
        reader = csv.reader(f)
        
        # Starting with source airport
        for line in reader:
            routes.setdefault(line[2], [])
            
            # Finding any possible destination matches, and append to a dictionary
            if line[4] in routes[line[2]]:
                pass
            else:
                routes[line[2]].append(line[4])
    return routes

_airlines = read_airlines()
_airports = read_airports()
_routes = read_routes()

departure = 'CDG'
arrival = 'BOS'

if arrival in _routes.keys():
    if arrival in _routes[departure]: # Direct Flight
        print(f"Direct flight is possible between {_airports[departure]} and {_airports[arrival]}\n")
    else:
        print(f"Sorry!! Direct flight is NOT possible between {departure} and {_airports[arrival]}\n")

    for line in _routes[departure]: # 2 Legs
        if arrival in _routes[line]:
            print(f"Connecting flights possible between {departure}, {line}, {arrival}")

    for line in _routes[departure]: # 3 Legs
        for line2 in _routes[line]:
            if arrival in _routes[line2] and departure != line2 and arrival != line:
                print(f"Multi-Connecting flights possible between {departure}, {line}, {line2} {arrival}")
else:
    print(f"Sorry!! No flight is possible between {departure} and {_airports[arrival]}")
