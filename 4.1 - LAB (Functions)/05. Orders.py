def calculation_order(product, count):
    if product == "coffee":
        price_product = 1.50
        return price_product * count
    elif product == "water":
        price_product = 1.00
        return price_product * count
    elif product == "coke":
        price_product = 1.40
        return price_product * count
    elif product == "snacks":
        price_product = 2.00
        return price_product * count


type_product = input()
quantity_of_the_product = int(input())
print(f"{calculation_order(type_product, quantity_of_the_product):.2f}")


# def calculating(input_product, quantity_of_products):
#     total_price = 0
#     if input_product == 'coffee':
#         price_per_product = 1.5
#         total_price = quantity_of_products * price_per_product
#     elif input_product == 'water':
#         price_per_product = 1
#         total_price = quantity_of_products * price_per_product
#     elif input_product == 'coke':
#         price_per_product = 1.4
#         total_price = quantity_of_products * price_per_product
#     elif input_product == 'snacks':
#         price_per_product = 2
#         total_price = quantity_of_products * price_per_product
#     return total_price
#
#
# product = input()
# quantity = int(input())
# final_price = calculating(product, quantity)
# print(f'{final_price:.2f}')


# product = input()
# quantity = int(input())
# 
# 
# def calculating(input_product, quantity_of_products):
#     if input_product == 'coffee':
#         price_per_product = 1.5
#         return quantity_of_products * price_per_product
#     elif input_product == 'water':
#         price_per_product = 1
#         return quantity_of_products * price_per_product
#     elif input_product == 'coke':
#         price_per_product = 1.4
#         return quantity_of_products * price_per_product
#     elif input_product == 'snacks':
#         price_per_product = 2
#         return quantity_of_products * price_per_product
# 
# 
# final_price = calculating(product, quantity)
# print(f'{final_price:.2f}')
