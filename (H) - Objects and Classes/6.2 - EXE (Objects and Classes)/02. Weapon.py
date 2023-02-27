class Weapon:
    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self) -> str:
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"

    def __repr__(self) -> str:
        amount_of_bullets = self.bullets
        return f"Remaining bullets: {amount_of_bullets}"


# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)


# class Weapon:
#     def __init__(self, bullets: int):
#         self.bullets = bullets
#
#     def shoot(self):
#         if self.bullets > 0:
#             self.bullets -= 1
#             return "shooting..."
#         else:
#             return "no bullets left"
#
#     def __repr__(self):
#         return f"Remaining bullets: {self.bullets}"
