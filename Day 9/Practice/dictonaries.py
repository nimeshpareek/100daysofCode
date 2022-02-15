travel_log = [{"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]}, ]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇

def add_new_country(country_visited, times_visited, cities_visited):
    new_data = {}
    new_data["country"] = country_visited
    new_data["cities"] = cities_visited
    new_data["visits"] = times_visited
    travel_log.append(new_data)
    print(travel_log)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

