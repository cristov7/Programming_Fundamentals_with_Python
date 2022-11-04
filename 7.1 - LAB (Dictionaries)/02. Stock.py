stock_list = input().split()
needed_products = input().split()
stock_dict = {}
for index in range(0, len(stock_list), 2):   # for index in range(0, len(stock) -1, 2):
    available_product = stock_list[index]
    quantity_of_the_product = int(stock_list[index + 1])
    stock_dict[available_product] = quantity_of_the_product
for product in needed_products:
    if product in stock_dict.keys():
        quantity = stock_dict[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


# stock_list = input().split()
# needed_products = input().split()
# for product in needed_products:
#     if product in stock_list:
#         quantity_index = stock_list.index(product) + 1
#         quantity = stock_list[quantity_index]
#         print(f"We have {quantity} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")
