class Circle:
    __pi = 3.14

    def __init__(self, diameter: int):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self) -> [int, float]:
        return 2 * Circle.__pi * self.radius

    def calculate_area(self) -> [int, float]:
        return Circle.__pi * self.radius ** 2

    def calculate_area_of_sector(self, angle: int) -> [int, float]:
        return Circle.__pi * self.radius ** 2 * (angle / 360)


# circle = Circle(10)
# angle = 5
#
# print(f"{circle.calculate_circumference():.2f}")
# print(f"{circle.calculate_area():.2f}")
# print(f"{circle.calculate_area_of_sector(angle):.2f}")


# class Circle:
#     __pi = 3.14
#
#     def __init__(self, diameter):
#         self.diameter = diameter
#         self.radius = diameter / 2
#
#     def calculate_circumference(self):
#         return 2 * Circle.__pi * self.radius
#
#     def calculate_area(self):
#         return Circle.__pi * self.radius ** 2
#
#     def calculate_area_of_sector(self, angle):
#         return Circle.__pi * self.radius * self.radius * (angle / 360)


# class Circle:
#     __pi = 3.14
#
#     def __init__(self, diameter):
#         self.diameter = diameter
#         self.radius = diameter / 2
#
#     def calculate_circumference(self):
#         return Circle.__pi * self.diameter
#
#     def calculate_area(self):
#         return Circle.__pi * self.radius * self.radius
#
#     def calculate_area_of_sector(self, angle):
#         return (angle / 360) * Circle.__pi * self.radius * self.radius


# class Circle:
#     __pi = 3.14
#
#     def __init__(self, diameter):
#         self.diameter = diameter
#         self.radius = diameter / 2
#
#     def calculate_circumference(self):
#         return Circle.__pi * self.diameter
#
#     def calculate_area(self):
#         pi = Circle.__pi
#         r = self.radius
#         return pi * (r ** 2)
#
#     def calculate_area_of_sector(self, angle):
#         pi = Circle.__pi
#         r = self.radius
#         return angle / 360 * pi * (r ** 2)
