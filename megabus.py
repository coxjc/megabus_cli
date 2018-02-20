#!/usr/bin/env python3

import json
import requests

import click

ORIGIN_CITIES_URL = "https://us.megabus.com/journey-planner/api/origin-cities"
DEST_CITIES_URL = lambda origin: "https://us.megabus.com/journey-planner/api/destination-cities?originCityId={}".format(origin)
DATES_URL = lambda origin, destination: "https://us.megabus.com/journey-planner/api/journeys/travel-dates?originCityId={}&destinationCityId={}".format(origin, destination)
PRICES_URL = lambda origin, destination, departure, passengers: "https://us.megabus.com/journey-planner/api/journeys?originId={}&destinationId={}&departureDate={}&totalPassengers={}".format(origin, destination, departure, passengers)


def get_origin_cities():
    """Get origin cities."""
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


def get_dates(origin_city_id, destination_city_id):
    r = requests.get(DATES_URL(origin_city_id, destination_city_id))
    try:
        return r.json()["availableDates"]
    except Exception as e:
        raise e


def get_prices(origin_city_id, destination_city_id, departure, passengers):
    r = requests.get(PRICES_URL(origin_city_id, destination_city_id, departure,
                                passengers))
    try:
        return r.json()["journeys"]
    except Exception as e:
        raise e


def get_city_id(candidate_city):
    """Get the city ID, or return the argument if it's already an ID."""
    try:
        city_id = int(candidate_city)
    except ValueError:
        for city in get_origin_cities():
            if candidate_city == city['name']:
                city_id = city['id']
                break
        else:
            raise ValueError(
                'ID for city "{}" was not found.'.format(candidate_city))
    return city_id


@click.group()
def cli():
    pass


@cli.command('origin-cities')
@click.option('--raw', is_flag=True, help='Print raw JSON')
def origin_cities(raw):
    """List trip origin cities."""
    cities = get_origin_cities()

    if raw:
        print(json.dumps(cities, indent=4))
    else:
        for city in sorted([city['name'] for city in cities]):
            print(city)


@cli.command('destination-cities')
@click.argument('origin_city')
@click.option('--raw', is_flag=True, help='Print raw JSON')
def destination_cities(origin_city, raw):
    """List destination cities available from a given ORIGIN_CITY.

    ORIGIN_CITY may be a name or ID.
    """
    origin_city_id = get_city_id(origin_city)
    cities = get_destination_cities(origin_city_id)
    if raw:
        print(json.dumps(cities, indent=4))
    else:
        for city in sorted([city['name'] for city in cities]):
            print(city)


@cli.command('dates')
@click.argument('origin_city')
@click.argument('destination_city')
@click.option('--raw', is_flag=True, help='Print raw JSON')
def dates(origin_city, destination_city, raw):
    """List departure dates for a trip from ORIGIN_CITY to DESTINATION_CITY.

    ORIGIN_CITY may be a name or ID.
    DESTINATION_CITY may be a name or ID.
    """
    origin_city_id = get_city_id(origin_city)
    destination_city_id = get_city_id(destination_city)
    dates = get_dates(origin_city_id, destination_city_id)

    if raw:
        print(json.dumps(dates, indent=4))
    else:
        for date in sorted(dates):
            print(date)


@cli.command('prices')
@click.argument('origin_city')
@click.argument('destination_city')
@click.argument('date')
@click.argument('n_passengers', type=int)
@click.option('--raw', is_flag=True, help='Print raw JSON')
def prices(origin_city, destination_city, date, n_passengers, raw):
    """List trip prices for a trip on DATE.

    N_PASSENGERS take the trip from ORIGIN_CITY to DESTINATION_CITY.
    ORIGIN_CITY may be a name or ID.
    DESTINATION_CITY may be a name or ID.
    DATE is formatted as YYYY-MM-DD.
    """
    origin_city_id = get_city_id(origin_city)
    destination_city_id = get_city_id(destination_city)
    prices = get_prices(origin_city_id, destination_city_id, date,
                        n_passengers)

    if raw:
        print(json.dumps(prices, indent=4))
    else:
        for price in sorted(prices):
            print("${:.2f}: {} - {}".format(
                price['price'],
                price['departureDateTime'],
                price['arrivalDateTime']
            ))


if __name__ == "__main__":
    cli()
