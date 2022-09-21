age = int(input())
drink = ""
if 0 <= age <= 14:
    drink = "toddy"
elif 15 <= age <= 18:
    drink = "coke"
elif 19 <= age <= 21:
    drink = "beer"
elif age >= 22:
    drink = "whisky"
print(f"drink {drink}")
