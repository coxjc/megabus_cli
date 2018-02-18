import json
import requests

origin_cities_url = "https://us.megabus.com/journey-planner/api/origin-cities"

destination_cities_url = lambda origin: "https://us.megabus.com/journey-planner/api/destination-cities?originCityId={}".format(origin) 

travel_dates_url = lambda origin, destination: "https://us.megabus.com/journey-planner/api/journeys/travel-dates?originCityId={}&destinationCityId={}".format(origin, destination)

prices_url = lambda origin, destination, departure, passengers: "https://us.megabus.com/journey-planner/api/journeys?originId={}&destinationId={}&departureDate={}&totalPassengers={}".format(origin, destination, departure, passengers)

def get_origin_cities():
    r = requests.get(origin_cities_url)
    try:
        return r.json()["cities"]
    except Exception as e:
        raise e

def get_destination_cities(origin_city_id):
    r = requests.get(destination_cities_url(origin_city_id))    
    try:
        return r.json()["cities"]
    except Exception as e:
        raise e

def get_travel_dates(origin_city_id, destination_city_id):
    r = requests.get(travel_dates_url(origin_city_id, destination_city_id))
    try:
        return r.json()["availableDates"]
    except Exception as e:
        raise e

def get_prices(origin_city_id, destination_city_id, departure, passengers):
    r = requests.get(prices_url(origin_city_id, destination_city_id, departure, passengers))
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
