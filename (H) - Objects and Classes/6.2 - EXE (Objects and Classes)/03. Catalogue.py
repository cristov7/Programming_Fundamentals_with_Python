from typing import List


class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str) -> None:
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str) -> List[str]:
        get_by_letter_list = [product_name for product_name in self.products
                              if product_name.startswith(first_letter)]
        return get_by_letter_list

    def __repr__(self) -> str:
        self.products.sort()
        output = f"Items in the {self.name} catalogue:" \
                 f"\n" + "\n".join(self.products)
        return output


# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)


# class Catalogue:
#     def __init__(self, name: str):
#         self.name = name
#         self.products = []
#
#     def add_product(self, product_name: str):
#         self.products.append(product_name)
#
#     def get_by_letter(self, first_letter: str):
#         return [product for product in self.products if product.startswith(first_letter)]
#
#     def __repr__(self):
#         string_with_output = f"Items in the {self.name} catalogue:\n"
#         string_with_output += "\n".join(sorted(self.products))
#         return string_with_output
