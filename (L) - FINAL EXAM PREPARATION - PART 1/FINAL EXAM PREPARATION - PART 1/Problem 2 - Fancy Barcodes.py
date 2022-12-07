import re
regex_barcode = r"(@[#]{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(@[#]{1,})"
count_barcodes = int(input())
for barcode in range(1, count_barcodes + 1):
    current_barcode = input()
    result = re.search(regex_barcode, current_barcode)   # result = re.findall(regex_barcode, current_barcode)
    if result:
        regex_digits = r"\d"
        result_list = re.findall(regex_digits, current_barcode)
        if result_list:
            product_group = "".join(result_list)
            print(f"Product group: {product_group}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")


# import re
# regex = r"(@[#]{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(@[#]{1,})"
# count_barcodes = int(input())
# for barcode in range(1, count_barcodes + 1):
#     current_barcode = input()
#     result = re.search(regex, current_barcode)   # result = re.findall(regex, current_barcode)
#     if result:
#         product_group = ""
#         for char in current_barcode:
#             if char.isdigit():
#                 product_group += char
#             else:
#                 continue
#         if product_group == "":
#             product_group = "00"
#             print(f"Product group: {product_group}")
#         else:
#             print(f"Product group: {product_group}")
#     else:
#         print("Invalid barcode")
