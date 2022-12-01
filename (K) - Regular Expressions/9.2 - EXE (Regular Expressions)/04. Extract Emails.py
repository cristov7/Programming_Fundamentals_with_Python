import re
extract_emails = input()
regex = r"\s([a-z0-9]+[a-z0-9\_\-\.]*@[a-z0-9]+[a-z0-9\-\.]*\.[a-z0-9]+)\b"
emails_list = re.findall(regex, extract_emails)
print("\n".join(emails_list))
