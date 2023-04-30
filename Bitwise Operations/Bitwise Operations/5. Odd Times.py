numbers_list = input().split()
numbers_set = set(numbers_list)

for number in numbers_set:
    count_number = numbers_list.count(number)

    if count_number % 2:
        print(number)
        break
