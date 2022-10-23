countries_wealth_list = list(map(int, input().split(", ")))
minimum_wealth_per_country = int(input())
count_population = len(countries_wealth_list)
all_wealth = sum(countries_wealth_list)
if minimum_wealth_per_country * count_population <= all_wealth:
    for index, wealth_per_country in enumerate(countries_wealth_list):
        if wealth_per_country < minimum_wealth_per_country:
            needed_wealth = abs(wealth_per_country - minimum_wealth_per_country)
            index_richest_country = countries_wealth_list.index(max(countries_wealth_list))
            countries_wealth_list[index_richest_country] -= needed_wealth
            countries_wealth_list[index] = wealth_per_country + needed_wealth
        else:
            continue
    print(countries_wealth_list)
else:
    print("No equal distribution possible")
