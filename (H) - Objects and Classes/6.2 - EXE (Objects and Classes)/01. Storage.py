from typing import List


class Storage:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str) -> None:
        if len(self.storage) + 1 <= self.capacity:
            self.storage.append(product)

    def get_products(self) -> List[str]:
        return self.storage


# storage = Storage(4)
# storage.add_product("apple")
# storage.add_product("banana")
# storage.add_product("potato")
# storage.add_product("tomato")
# storage.add_product("bread")
# print(storage.get_products())


# class Storage:
#     storage = []
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def add_product(self, product: str):
#         if self.capacity > 0:
#             Storage.storage.append(product)
#             self.capacity -= 1
#
#     def get_products(self):
#         return Storage.storage
