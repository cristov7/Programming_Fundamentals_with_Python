takes_as_strings = input()
count_beggars = int(input())
takes_as_strings_in_list = takes_as_strings.split(", ")
takes_as_integers_in_list = []
for takes in takes_as_strings_in_list:
    current_take = int(takes)
    takes_as_integers_in_list.append(current_take)
final_takes_per_every_beggar_in_list = []
starting_index_per_takes = 0
while starting_index_per_takes < count_beggars:
    takes_per_current_beggar = 0
    for current_takes in range(starting_index_per_takes, len(takes_as_integers_in_list), count_beggars):
        takes_per_current_beggar += takes_as_integers_in_list[current_takes]
    final_takes_per_every_beggar_in_list.append(takes_per_current_beggar)
    starting_index_per_takes += 1
print(final_takes_per_every_beggar_in_list)
