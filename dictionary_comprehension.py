# dictionary comprehension = create dictionaries using an expression

# can replace for loops and certain lambda functions

# # dictionary = {key: expression for (key, value) in iterable]
# dictionary = {key: expression for (key, value) in iterable if conditional}

# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

# cities_in_C = {key: round((value-32) * (5/9))
#                for (key, value) in cities_in_F.items()}

# dictionary = (key: (if/exse) for (key, value) in iterable}

# print(cities_in_C)


weather = {"New York": "snowing",
           "Boston": "sunny",
           "Los Angeles": "sunny",
           'Chicago': "cloudy"}


def check_sunny(value):
    if value == "sunny":
        return value
    else:
        return "COLD"


weather_dict = {key: value for (
    key, value) in weather.items() if value == "sunny"}

weather_dict = {key: value if value ==
                "sunny" else "COLD" for (key, value) in weather.items()}

weather_dict = {key: check_sunny(value) for (key, value) in weather.items()}

print(weather_dict)
