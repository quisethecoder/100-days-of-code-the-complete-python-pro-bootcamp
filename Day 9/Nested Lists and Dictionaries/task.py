capital = {
    "France": "Paris",
    "Germany": "Berlin"
}


# travel_log = {
#     "France": ["Paris", "Lille", "Saint-Tropez", "Dijon"],
#     "America": ["New York", "Arizona", "California"]
# }

# print(travel_log["France"][1])

nested_list = ["a", "b", ["c", "d"]]

# print(nested_list[2][0])


travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Saint-Tropez", "Dijon"],
        "total_visits": 8
    },
    "America": {
        "cities_visited": ["New York", "Arizona", "California"],
        "total_visits": 5
    }
}

print(travel_log["America"]["cities_visited"][2])
print(travel_log["America"]["total_visits"])