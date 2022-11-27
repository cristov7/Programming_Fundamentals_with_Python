import re
regex = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"
all_phone_numbers = input()
filtered_phone_numbers_list = re.findall(regex, all_phone_numbers)
print(", ".join(filtered_phone_numbers_list))
