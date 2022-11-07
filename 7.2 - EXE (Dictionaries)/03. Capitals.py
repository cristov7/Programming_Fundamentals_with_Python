country_list = input().split(", ")
capitals_list = input().split(", ")
dictionary = {country_list[index]: capitals_list[index] for index in range(len(country_list))}
for country, capital in dictionary.items():
    print(f"{country} -> {capital}")


# country_list = input().split(", ")
# capitals_list = input().split(", ")
# dictionary = dict(zip(country_list, capitals_list))
# for country, capital in dictionary.items():
#     print(f"{country} -> {capital}")


# country_list = input().split(", ")
# capitals_list = input().split(", ")
# for index in range(len(country_list)):
#     print(f"{country_list[index]} -> {capitals_list[index]}")
