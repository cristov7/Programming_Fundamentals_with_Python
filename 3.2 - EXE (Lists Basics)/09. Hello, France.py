itemsList = input().split("|")
budget = float(input())
oldPriceList = []
newPriceList = []
for item in itemsList:
    current = item.split("->")
    type = current[0]
    price = float(current[1])
    if "Clothes" in type and price <= 50:
        if budget - price >= 0:
            budget -= price
            oldPriceList.append(price)
    elif "Shoes" in type and price <= 35:
        if budget - price >= 0:
            budget -= price
            oldPriceList.append(price)
    elif "Accessories" in type and price <= 25.5:
        if budget - price >= 0:
            budget -= price
            oldPriceList.append(price)
for i in oldPriceList:
    newPrice = i * 1.4
    newPriceList.append(newPrice)
    print(f"{newPrice:.2f}", end=" ")
profit = sum(newPriceList) - sum(oldPriceList)
print()
print(f"Profit: {profit:.2f}")
if budget + sum(newPriceList) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
