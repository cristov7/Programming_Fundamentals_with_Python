import re
regex = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"   # \2 => the second group ([\/.-])
all_dates = input()
filtered_dates_list = re.finditer(regex, all_dates)
for date in filtered_dates_list:
    day = date.group(1)
    month = date.group(3)
    year = date.group(4)
    print(f"Day: {day}, Month: {month}, Year: {year}")


# import re
# regex = r"\b\d{2}/[A-Z][a-z]{2}/[0-9]{4}\b|\b\d{2}\.[A-Z][a-z]{2}\.\d{4}\b|\b\d{2}-[A-Z][a-z]{2}-\d{4}\b"
# all_dates = input()
# filtered_dates_list = re.findall(regex, all_dates)
# for date in filtered_dates_list:
#     day = date[:2]
#     month = date[3:6]
#     year = date[7:]
#     print(f"Day: {day}, Month: {month}, Year: {year}")


# import re
# regex = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"   # \2 => the second group ([\/.-])
# all_dates = input()
# filtered_dates_list = re.findall(regex, all_dates)
# for date in filtered_dates_list:
#     day = date[0]
#     month = date[2]
#     year = date[3]
#     print(f"Day: {day}, Month: {month}, Year: {year}")
