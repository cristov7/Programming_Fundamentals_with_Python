factor = int(input())
count = int(input())
multiples_list = []
for multiples in range(1, count + 1):
    current_number = multiples * factor
    multiples_list.append(current_number)
print(multiples_list)
