budget = int(input())
while True:
    command = input()
    if command != "End":
        price_of_the_product = int(command)
        if price_of_the_product <= budget:
            budget -= price_of_the_product
        else:
            print("You went in overdraft!")
            break
    else:
        print("You bought everything needed.")
        break


# budget = int(input())
# command = input()
# while command != "End":
#     product_price = int(command)
#     budget -= product_price
#     if budget < 0:
#         print("You went in overdraft!")
#         break
#     command = input()
# else:
#     print("You bought everything needed.")
