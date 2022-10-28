class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    command = input()
    if command == "End":
        print(f'Going: {", ".join(party.people)}')
        print(f'Total: {len(party.people)}')
        break
    else:
        name = command
        party.people.append(name)


# class Party:
#     def __init__(self):
#         self.people = []
#
#
# party = Party()
# line = input()
# while line != "End":
#     party.people.append(line)
#     line = input()
# print(f'Going: {", ".join(party.people)}')
# print(f'Total: {len(party.people)}')


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Party:
#     def __init__(self):
#         self.people = []
#
#     def invite(self, person):
#         self.people.append(person)
#
#     def name_of_attendees(self):
#         return ", ".join([person.name for person in self.people])
#
#     def number_of_guests(self):
#         return len(self.people)
#
#
# party = Party()
# while True:
#     command = input()
#     if command == "End":
#         break
#     else:
#         name = command
#         person = Person(name)
#         party.invite(person)
# print(f"Going: {party.name_of_attendees()}")
# print(f"Total: {party.number_of_guests()}")
