# Map-Reduce Assignment - Csilla Tepliczky, 31.10.2023

import json
import datetime
from functools import reduce

def read_json(filename):
    try:
        with open(filename, 'r') as file:
            text = json.load(file)
        return text
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format.")

# Load the dataset
data = read_json('D:/Csilla/Codebase/restaurant_short.json')
print(data)


# Convert timestamps
def convert_timestamp(item):
    try:
        tstamp = item['date']/1000
        item['date'] = datetime.datetime.fromtimestamp(tstamp)
        return item
    except KeyError as e:
        return 'Invalid key', e
    except ValueError as e:
        return 'Invalid timestamp in grades', e

map_iterator = map(lambda restaurant: {**restaurant, 'grades': list(map(convert_timestamp, restaurant['grades']))}, data)
restaurants_with_converted_dates = list(map_iterator)


# Identify restaurants with at least 5 reviews in the most recent year
most_recent_year = max(item['date'] for restaurant in data for item in restaurant['grades']).year

def at_least_5_reviews(restaurant):
    reviews_in_recent_year = list(filter(lambda item: item['date'].year == most_recent_year, restaurant['grades']))
    if len(reviews_in_recent_year) >= 5:
        return len(reviews_in_recent_year)

restaurants = list(filter(at_least_5_reviews, data))
print(f'The restaurants with at least 5 reviews in the recent year are {restaurants}')


# Identify all restaurants that have at least 5 reviews
def more_than_5_reviews(restaurant):
    if len(restaurant['grades']) > 5:
        return len(restaurant['grades'])

restaurants = list(filter(more_than_5_reviews, data))
print(f'Restaurants with more than 5 reviews: {restaurants}')


# Calculate the average number of reviews per restaurant
average_reviews = reduce(lambda x, y: x + len(y['grades']), data, 0) 
average_reviews_per_rest = average_reviews / len(data)

print(f'The average reviews per restaurant is {average_reviews_per_rest}')


# Identify all restaurants that have more reviews than the average number of reviews per restaurant
def more_reviews_than_average(restaurant):
    if len(restaurant['grades']) > average_reviews_per_rest:
        return len(restaurant['grades'])

restaurants_with_more_reviews = list(filter(more_reviews_than_average, data))
print(restaurants_with_more_reviews)