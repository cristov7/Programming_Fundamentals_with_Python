def add(course: list, title: str):
    if title not in course:
        course.append(title)


def insert(course: list, title: str, index: int):
    if title not in course:
        course.insert(index, title)


def remove(course: list, title: str):
    if title in course:
        if f"{title}-Exercise" in course:
            course.remove(f"{title}-Exercise")
        course.remove(title)


def swap(course: list, first_title: str, second_title: str):
    if first_title in course and second_title in course:
        first_course_index = course.index(first_title)
        second_course_index = course.index(second_title)
        course[first_course_index], course[second_course_index] = \
            course_list[second_course_index], course_list[first_course_index]
        index = course.index(second_title) + 1
        if index < len(course):
            if course[index] == f"{first_title}-Exercise":
                course.pop(index)
                index = course.index(first_title) + 1
                course.insert(index, f"{first_title}-Exercise")
        index = course.index(first_title) + 1
        if index < len(course):
            if course[index] == f"{second_title}-Exercise":
                course.pop(index)
                index = course.index(second_title) + 1
                course.insert(index, f"{second_title}-Exercise")


def exercise(course: list, title: str):
    if title in course and f"{title}-Exercise" not in course:
        index = course.index(title)
        course.insert(index + 1, f"{title}-Exercise")
    elif title not in course:
        course.append(title)
        course.append(f"{title}-Exercise")


course_list = input().split(', ')
while True:
    command = input().split(':')
    if command[0] == "course start":
        break
    else:
        lesson_title = command[1]
        if command[0] == 'Add':
            add(course_list, lesson_title)
        elif command[0] == "Insert":
            current_index = int(command[-1])
            insert(course_list, lesson_title, current_index)
        elif command[0] == "Remove":
            remove(course_list, lesson_title)
        elif command[0] == "Swap":
            second_lesson_title = command[-1]
            swap(course_list, lesson_title, second_lesson_title)
        elif command[0] == "Exercise":
            exercise(course_list, lesson_title)
for curr_index, lesson_name in enumerate(course_list):
    print(f"{curr_index + 1}.{lesson_name}")


# def add_lesson(list_of_lessons, title):
#     if title not in list_of_lessons:
#         list_of_lessons.append(title)
#     return list_of_lessons
#
#
# def insert_lesson(list_of_lessons, title, index):
#     if title not in list_of_lessons:
#         list_of_lessons.insert(index, title)
#     return list_of_lessons
#
#
# def remove_lesson(list_of_lessons, title):
#     if title in list_of_lessons:
#         title_index = list_of_lessons.index(title)
#         if title_index + 1 in range(len(list_of_lessons)):
#             if "Exercise" in list_of_lessons[title_index + 1]:
#                 list_of_lessons.pop(title_index + 1)
#         list_of_lessons.remove(title)
#     return list_of_lessons
#
#
# def swap_lessons(list_of_lessons, first_lesson, second_lesson):
#     if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
#         first_position = list_of_lessons.index(first_lesson)
#         second_position = list_of_lessons.index(second_lesson)
#         first_has_exercise = False
#         second_has_exercise = False
#         if first_position + 1 in range(len(list_of_lessons)):
#             first_has_exercise = "Exercise" in list_of_lessons[first_position + 1]
#         if second_position + 1 in range(len(list_of_lessons)):
#             second_has_exercise = "Exercise" in list_of_lessons[second_position + 1]
#         list_of_lessons[first_position], list_of_lessons[second_position] = \
#             list_of_lessons[second_position], list_of_lessons[first_position]
#         if first_has_exercise and second_has_exercise:
#             list_of_lessons[first_position + 1], list_of_lessons[second_position + 1] = \
#                 list_of_lessons[second_position + 1], list_of_lessons[first_position + 1]
#         elif not first_has_exercise and second_has_exercise:
#             list_of_lessons.insert(first_position + 1, list_of_lessons.pop(second_position + 1))
#         elif first_has_exercise and not second_has_exercise:
#             list_of_lessons.insert(second_position + 1, list_of_lessons.pop(first_position + 1))
#     return list_of_lessons
#
#
# def exercise(list_of_lessons, title):
#     if title in list_of_lessons and f"{title}-Exercise" not in list_of_lessons:
#         lesson_index = list_of_lessons.index(title)
#         list_of_lessons.insert(lesson_index + 1, f"{title}-Exercise")
#     elif title not in list_of_lessons:
#         list_of_lessons.append(title)
#         list_of_lessons.append(f"{title}-Exercise")
#     return list_of_lessons
#
#
# lessons = input().split(", ")
# command = input().split(":")
# while len(command) > 1:  # while command[0] != "course start"
#     action = command[0]
#     lesson_title = command[1]
#     lesson_title_or_index = command[-1]
#     if action == "Add":
#         lessons = add_lesson(lessons, lesson_title)
#     elif action == "Insert":
#         lessons = insert_lesson(lessons, lesson_title, int(lesson_title_or_index))
#     elif action == "Remove":
#         lessons = remove_lesson(lessons, lesson_title)
#     elif action == "Swap":
#         lessons = swap_lessons(lessons, lesson_title, lesson_title_or_index)
#     elif action == "Exercise":
#         lessons = exercise(lessons, lesson_title)
#     command = input().split(":")
# for index, lesson_name in enumerate(lessons):
#     print(f"{index + 1}.{lesson_name}")


# lessons_and_exercises_list = input().split(", ")
# while True:
#     command = input()
#     if command == "course start":
#         break
#     else:
#         command_list = command.split(":")
#         if command_list[0] == "Add":
#             topic = command_list[1]
#             if topic not in lessons_and_exercises_list:
#                 lessons_and_exercises_list.append(topic)
#             else:
#                 continue
#         elif command_list[0] == "Insert":
#             topic = command_list[1]
#             index = int(command_list[2])
#             if topic not in lessons_and_exercises_list:
#                 lessons_and_exercises_list.insert(index, topic)
#             else:
#                 continue
#         elif command_list[0] == "Remove":
#             topic = command_list[1]
#             if topic in lessons_and_exercises_list:
#                 lessons_and_exercises_list.remove(topic)
#             else:
#                 continue
#         elif command_list[0] == "Swap":
#             first_topic = command_list[1]
#             second_topic = command_list[2]
#             if first_topic in lessons_and_exercises_list and second_topic in lessons_and_exercises_list:
#                 if first_topic + "-Exercise" not in lessons_and_exercises_list and \
#                         second_topic + "-Exercise" not in lessons_and_exercises_list:
#                     index_first_topic = lessons_and_exercises_list.index(first_topic)
#                     index_second_topic = lessons_and_exercises_list.index(second_topic)
#                     lessons_and_exercises_list[index_first_topic], lessons_and_exercises_list[index_second_topic]\
#                         = lessons_and_exercises_list[index_second_topic], lessons_and_exercises_list[index_first_topic]
#                 else:
#                     if first_topic + "-Exercise" in lessons_and_exercises_list:
#                         index_first_topic = lessons_and_exercises_list.index(first_topic)
#                         index_first_topic_exercise = lessons_and_exercises_list.index(first_topic) + 1
#                         index_second_topic = lessons_and_exercises_list.index(second_topic)
#                         lessons_and_exercises_list[index_first_topic], lessons_and_exercises_list[index_second_topic] \
#                             = lessons_and_exercises_list[index_second_topic], lessons_and_exercises_list[
#                             index_first_topic]
#                         lessons_and_exercises_list.remove(first_topic + "-Exercise")
#                         lessons_and_exercises_list.insert(index_second_topic + 1, first_topic + "-Exercise")
#                     else:
#                         index_first_topic = lessons_and_exercises_list.index(first_topic)
#                         index_second_topic = lessons_and_exercises_list.index(second_topic)
#                         index_second_topic_exercise = lessons_and_exercises_list.index(second_topic) + 1
#                         lessons_and_exercises_list[index_first_topic], lessons_and_exercises_list[index_second_topic] \
#                             = lessons_and_exercises_list[index_second_topic], lessons_and_exercises_list[
#                             index_first_topic]
#                         lessons_and_exercises_list.remove(second_topic + "-Exercise")
#                         lessons_and_exercises_list.insert(index_first_topic + 1, second_topic + "-Exercise")
#             else:
#                 continue
#         elif command_list[0] == "Exercise":
#             topic = command_list[1]
#             if topic in lessons_and_exercises_list:
#                 index = int(lessons_and_exercises_list.index(topic))
#                 if topic + "-Exercise" not in lessons_and_exercises_list:
#                     lessons_and_exercises_list.insert(index + 1, topic + "-Exercise")
#                 else:
#                     continue
#             else:
#                 lessons_and_exercises_list.append(topic)
#                 lessons_and_exercises_list.append(topic + "-Exercise")
# for number, lesson in enumerate(lessons_and_exercises_list):
#     number += 1
#     print(f"{number}.{lesson}")
