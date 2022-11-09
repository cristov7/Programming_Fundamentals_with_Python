country_names = input().split(", ")
capital_cities = input().split(", ")
# len(country_names) == len(capital_cities)
my_dict = {country_names[index]: capital_cities[index] for index in range(len(country_names))}   # comprehension
# my_dict = dict(zip(country_names, capital_cities))   # zip
for country, capital in my_dict.items():
    print(f"{country} -> {capital}")


# country_list = input().split(", ")
# capitals_list = input().split(", ")
# dictionary = {country_list[index]: capitals_list[index] for index in range(len(country_list))}
# for country, capital in dictionary.items():
#     print(f"{country} -> {capital}")


# country_list = input().split(", ")
# capitals_list = input().split(", ")
# dictionary = dict(zip(country_list, capitals_list))
# for country, capital in dictionary.items():
#     print(f"{country} -> {capital}")


# country_list = input().split(", ")
# capitals_list = input().split(", ")
# for index in range(len(country_list)):
#     print(f"{country_list[index]} -> {capitals_list[index]}")
