import re
regex = r"\b(www)\.([A-Za-z0-9\-]+)\.([a-z]+[\.a-z]*)\b"
while True:
    command = input()
    if command == "":
        break
    else:
        info = re.search(regex, command)
        if info:
            sub_domain, domain_name, domain_extension = info.groups()
            # sub_domain = command_list.group(1)
            # domain_name = command_list.group(2)
            # domain_extension = command_list.group(3)
            link = f"{sub_domain}.{domain_name}.{domain_extension}"
            print(link)
        else:
            continue


# import re
# regex = r"\b(www)\.([A-Za-z0-9\-]+)\.([a-z]+[\.a-z]*)\b"
# while True:
#     command = input()
#     if command == "":
#         break
#     else:
#         command_list = re.findall(regex, command)
#         if len(command_list) == 1:
#             info = command_list[0]
#             sub_domain = info[0]
#             domain_name = info[1]
#             domain_extension = info[2]
#             link = f"{sub_domain}.{domain_name}.{domain_extension}"
#             print(link)
#         else:
#             continue
