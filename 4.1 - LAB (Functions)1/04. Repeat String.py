# string_text = input()
# counter = int(input())
#
#
# def repeat_string_text(string_text, counter):
#     return string_text * counter
#
#
# print(repeat_string_text(string_text, counter))


string_text = input()
counter = int(input())
repeat_string_text = lambda string_text, counter: string_text * counter
print(repeat_string_text(string_text, counter))
