list_of_employees_happiness = list(map(int, input().split()))
happiness_improvement_factor = int(input())
update_list_of_employees_happiness = list(map(lambda x: x * happiness_improvement_factor, list_of_employees_happiness))
count_employees = len(list_of_employees_happiness)
half_happiness = sum(update_list_of_employees_happiness) / count_employees
count_happy_employees = 0
for happiness_per_employee in update_list_of_employees_happiness:
    if happiness_per_employee >= half_happiness:
        count_happy_employees += 1
    else:
        continue
if count_happy_employees >= half_happiness:
    print(f"Score: {count_happy_employees}/{count_employees}. Employees are happy!")
else:
    print(f"Score: {count_happy_employees}/{count_employees}. Employees are not happy!")


# list_of_employees_happiness = list(map(int, input().split()))
# happiness_improvement_factor = int(input())
# update_list_of_employees_happiness = list(map(lambda x: x * happiness_improvement_factor, list_of_employees_happiness))
# count_employees = len(list_of_employees_happiness)
# half_happiness = sum(update_list_of_employees_happiness) / count_employees
# count_happy_employees = sum([1 for happiness_per_employee in update_list_of_employees_happiness
#                           if happiness_per_employee >= half_happiness])
# if count_happy_employees >= half_happiness:
#     print(f"Score: {count_happy_employees}/{count_employees}. Employees are happy!")
# else:
#     print(f"Score: {count_happy_employees}/{count_employees}. Employees are not happy!")
