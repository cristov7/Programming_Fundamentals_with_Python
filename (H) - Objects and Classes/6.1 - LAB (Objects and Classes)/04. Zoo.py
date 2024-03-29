class Zoo:
    __animals = 0

    def __init__(self, name: str):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species: str, name: str) -> None:
        if species == "mammal":
            self.mammals.append(name)
            Zoo.__animals += 1
        elif species == "fish":
            self.fishes.append(name)
            Zoo.__animals += 1
        elif species == "bird":
            self.birds.append(name)
            Zoo.__animals += 1
        else:
            raise SystemExit("Invalid species!")

    def get_info(self, species: str) -> str:
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}" \
                   f"\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}" \
                   f"\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}" \
                   f"\nTotal animals: {Zoo.__animals}"
        else:
            raise SystemExit("Invalid species!")


zoo = Zoo(input())
for animal in range(1, int(input()) + 1):
    animal_species, animal_name = input().split()
    zoo.add_animal(animal_species, animal_name)
print(zoo.get_info(input()))


# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "bird":
#             self.birds.append(name)
#
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ""
#         if species == "mammal":
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == "fish":
#             result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
#         elif species == "bird":
#             result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
#
#         result += f"Total animals: {Zoo.__animals}"
#         return result
#
#
# zoo_name = input()
# zoo = Zoo(zoo_name)
# count = int(input())
# for i in range(count):
#     animal = input().split()
#     species = animal[0]
#     name = animal[1]
#     zoo.add_animal(species, name)
# info = input()
# print(zoo.get_info(info))


# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "bird":
#             self.birds.append(name)
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ""
#         if species == "mammal":
#             result += f"{species.title()}s in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == "fish":
#             result += f"{species.title()}es in {self.name}: {', '.join(self.fishes)}\n"
#         elif species == "bird":
#             result += f"{species.title()}s in {self.name}: {', '.join(self.birds)}\n"
#         result += f"Total animals: {Zoo.__animals}"
#         return result
#
#
# zoo_name = input()
# zoo = Zoo(zoo_name)
# num = int(input())
# for i in range(num):
#     animal_info = input().split()
#     species = animal_info[0]
#     name = animal_info[1]
#     zoo.add_animal(species, name)
# species = input()
# print(zoo.get_info(species))
