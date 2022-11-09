company_users = {}
while True:
    command = input()
    if command == "End":
        for company, employee_ids in company_users.items():
            print(f"{company}")
            for employee_id in employee_ids:
                print(f"-- {employee_id}")
        break
    else:
        command_list = command.split(" -> ")
        company_name = command_list[0]
        employee_id = command_list[1]
        if company_name not in company_users:
            company_users[company_name] = [employee_id]
        else:
            if employee_id not in company_users[company_name]:
                company_users[company_name].append(employee_id)
            else:
                continue


# company_users = {}
# while True:
#     command = input()
#     if command == "End":
#         break
#     else:
#         # company_name, employee_id = command.split(" -> ")
#         info_list = command.split(" -> ")
#         company_name = info_list[0]
#         employee_id = info_list[1]
#         if company_name not in company_users.keys():   # if company_name not in company_users:
#             company_users[company_name] = [employee_id]
#         else:
#             if employee_id in company_users[company_name]:
#                 continue
#             else:
#                 company_users[company_name].append(employee_id)
# for company, users in company_users.items():
#     print(f"{company}")
#     count_users = len(users)
#     for user in range(count_users):
#         print(f"-- {users[user]}")


# companies_dict = {}
# while True:
#     command = input()
#     if command == 'End':
#         break
#     company, id = command.split(' -> ')
#     if company not in companies_dict.keys():
#         companies_dict[company] = []
#     if id not in companies_dict[company]:
#         companies_dict[company].append(id)
# for company_name, employees in companies_dict.items():
#     print(company_name)
#     print('\n'.join(f'-- {employee_id}' for employee_id in employees))
