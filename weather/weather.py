#!/usr/bin/env python3

import argparse
import json
import requests
import sys


data = '''Current Weather in %s:

Current Weather: %s
Description: %s
Temperature: %s °C
Temp Min: %s °C
Temp Max: %s °C
Wind Speed: %s KPH
Wind Direction: %s° angle'''


def convert_celcius(temp):
    # Formula
    result = temp - 273.15
    return round(result, 2)


def fetch_data(location):

    # Download the JSON data from OpenWeatherMap.org API

    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=bb3474342a4a42f789fc69520688505b' % location

    # Check response
    try:
        response = requests.get(url)
        response.raise_for_status()

    except requests.exceptions.HTTPError:
        print('weather.py: error: unable to find country or city.')
        sys.exit(1)

    # Load JSON data to python
    weather_api = json.loads(response.text)

    # Print weather descriptions
    w = weather_api['weather']
    t = weather_api['main']
    x = weather_api['wind']

    # Convert and prepare data
    weather = w[0]['main']
    description = w[0]['description'].title()
    tempc = convert_celcius(t['temp'])
    tempc_min = convert_celcius(t['temp_min'])
    tempc_max = convert_celcius(t['temp_max'])
    wind_speed = x['speed']
    wind_dir = x['deg']

    print(data %
          (
              location,
              weather,
              description,
              tempc,
              tempc_min,
              tempc_max,
              wind_speed,
              wind_dir
          )

          )


def main():

    # Create a parser
    parser = argparse.ArgumentParser(
        add_help=True,
        allow_abbrev=False
    )

    parser.add_argument(
        '-l', '--location',
        metavar='',
        help='provide a country for a broader search.',
    )

    parser.add_argument(
        '-c', '--city',
        metavar='',
        help='provide a city for more accurate search.'
    )

    # Parse all args
    args = parser.parse_args()

    # Pass args to functions
    if args.location and args.city:
        location = args.location.title() + ', ' + args.city.title()
        fetch_data(location)
        sys.exit(0)

    elif args.location:
        location = args.location.title()
        fetch_data(location)
        sys.exit(0)

    elif args.city:
        location = args.city.title()
        fetch_data(location)
        sys.exit(0)


if __name__ == '__main__':
    main()
