# 1 century = 100 years
# 1 year = 365.2422 days
# 1 day = 24 hours
# 1 hour = 60 minutes
# 1 minute = 60 seconds
centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
