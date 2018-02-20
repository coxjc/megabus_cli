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

def get_dest_cities(origin_city_id):
    r = requests.get(DEST_CITIES_URL(origin_city_id))
    try:
        return r.json()["cities"]
    except Exception as e:
        raise e

def get_dates(origin_city_id, destination_city_id):
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

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("command",  help="'origin_cities', 'dest_cities', 'dates', or 'prices'")
arg_parser.add_argument("-o", "--origin", help="origin city ID")
arg_parser.add_argument("-d", "--dest", help="destination city ID")
arg_parser.add_argument("-t", "--time", help="date of departure in format: 'YYYY-MM-DD'")
arg_parser.add_argument("-p", "--passengers", help="number of passengers")

if __name__ == "__main__":
    args = arg_parser.parse_args()
    if args.command == "origin_cities":
        print(get_origin_cities())
    elif args.command == "dest_cities":
        if args.origin:
            print(get_dest_cities(args.origin))
        else:
            raise ValueError("origin city ID is required. run w/ -h flag for help.")
    elif args.command == "dates":
        if args.origin and args.dest:
            print(get_dates(args.origin, args.dest))
        else:
            raise ValueError("origin city ID & destination city ID is required. run w/ -h flag for help.")
    elif args.command == "prices":
        if args.origin and args.dest and args.time and args.passengers:
            print(get_prices(args.origin, args.dest, args.time, args.passengers))
        else:
            raise ValueError("origin city ID & destination city ID & time & passengers is required. run w/ -h flag for help.")
    else:
        raise ValueError("run w/ -h flag for help.")

