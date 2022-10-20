note_list = []
while True:
    command = input()
    if command == "End":
        break
    else:
        split_command = command.split("-")
        importance = int(split_command[0])
        note = split_command[1]
        note_list.append([importance, note])
update_note_list = sorted(note_list)
note_list.clear()
# for element in update_note_list:
#     current_element = element[1]
#     note_list.append(current_element)
note_list = [element[1] for element in update_note_list]
print(note_list)


# note_list = []
# while True:
#     command = input()
#     if command == "End":
#         break
#     else:
#         split_command = command.split("-")
#         importance = int(split_command[0])
#         note = split_command[1]
#         note_list.append([importance, note])
# sorted_list = [note[1] for note in sorted(note_list)]
# print(sorted_list)
