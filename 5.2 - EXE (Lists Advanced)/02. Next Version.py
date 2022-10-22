version_software = [number for number in input().split(".")]
number_of_version_software = int(("".join(version_software)))
next_number_version_software = number_of_version_software + 1
next_version_software_in_list = [number for number in str(next_number_version_software)]
print(".".join(next_version_software_in_list))


# version = [int(number) for number in input().split(".")]
# version[-1] += 1
# for index in range(len(version) - 1, - 1, - 1):
#     if version[index] > 9:
#         version[index] = 0
#         version[index - 1] += 1
#     else:
#         break
# print(".".join(str(number) for number in version))
