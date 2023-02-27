class Class:
    __students_count = 22

    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float) -> None:
        if len(self.students) + 1 <= Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self) -> float:
        average_grade = sum(self.grades) / len(self.students)
        return average_grade

    def __repr__(self) -> str:
        class_name = self.name
        students = ", ".join(self.students)
        average_grade = Class.get_average_grade(self)
        return f"The students in {class_name}: {students}. Average grade: {average_grade:.2f}"


# a_class = Class("11B")
# a_class.add_student("Peter", 4.80)
# a_class.add_student("George", 6.00)
# a_class.add_student("Amy", 3.50)
# print(a_class)


# class Class:
#     __students_count = 22
#
#     def __init__(self, name):
#         self.name = name
#         self.students = []
#         self.grades = []
#
#     def add_student(self, name: str, grade: float):
#         if len(self.students) < 22:
#             self.students.append(name)
#             self.grades.append(grade)
#
#     def get_average_grade(self):
#         average_grade = sum(self.grades) / len(self.students)
#         return average_grade
#
#     def __repr__(self):
#         students = ", ".join(self.students)
#         return f"The students in {self.name}: {students}. Average grade: {Class.get_average_grade(self):.2f}"
