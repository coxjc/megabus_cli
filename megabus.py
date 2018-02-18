import argparse 
import json
import requests

ORIGIN_CITIES_URL = "https://us.megabus.com/journey-planner/api/origin-cities"

DEST_CITIES_URL = lambda origin: "https://us.megabus.com/journey-planner/api/destination-cities?originCityId={}".format(origin) 

DATES_URL = lambda origin, destination: "https://us.megabus.com/journey-planner/api/journeys/travel-dates?originCityId={}&destinationCityId={}".format(origin, destination)

PRICES_URL = lambda origin, destination, departure, passengers: "https://us.megabus.com/journey-planner/api/journeys?originId={}&destinationId={}&departureDate={}&totalPassengers={}".format(origin, destination, departure, passengers)

def get_origin_cities():
    r = requests.get(ORIGIN_CITIES_URL)
    try:
        return r.json()["cities"]
    except Exception as e:
        raise e

def get_destination_cities(origin_city_id):
    r = requests.get(DEST_CITIES_URL(origin_city_id))    
    try:
        return r.json()["cities"]
    except Exception as e:
        raise e

def get_travel_dates(origin_city_id, destination_city_id):
    r = requests.get(DATES_URL(origin_city_id, destination_city_id))
    try:
        return r.json()["availableDates"]
    except Exception as e:
        raise e

def get_prices(origin_city_id, destination_city_id, departure, passengers):
    r = requests.get(PRICES_URL(origin_city_id, destination_city_id, departure, passengers))
    try: 
        return r.json()["journeys"]
    except Exception as e:
        raise e

'''
o_cities = get_origin_cities()
d_cities = get_destination_cities(o_cities[0]['id'])
dates = get_travel_dates(o_cities[0]['id'], d_cities[0]['id'])
print(get_prices(o_cities[0]['id'], d_cities[0]['id'], dates[0], 3))
'''
