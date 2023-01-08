def type_function(some_type):
    if some_type == "int":
        return "int"
    elif some_type == "real":
        return "real"
    elif some_type == "string":
        return "string"
    else:
        raise SystemExit("Invalid type...")


def calculating_function(some_type: str, some_string: str):
    if some_type == "int":
        number = int(some_string)
        command = 2
        result = number * command
        return result
    elif some_type == "real":
        number = float(some_string)
        command = 1.5
        result = number * command
        formatting_result = f"{result:.2f}"
        return formatting_result
    elif some_type == "string":
        formatting_string = "$" + some_string + "$"
        return formatting_string


current_type = input()
valid_type = type_function(current_type)
single_string = input()
calculation = calculating_function(valid_type, single_string)
print(calculation)


# def type_function(variable):
#     if variable == "int":
#         number = int(input())
#         result = number * 2
#         return result
#     elif variable == "real":
#         number = float(input())
#         result = number * 1.5
#         return f"{result:.2f}"
#     elif variable == "string":
#         text = input()
#         return f"${text}$"
#
#
# enter_type = input()
# print(type_function(enter_type))


# def datatype_check(typ, data):
#
#     if typ == 'int':
#         return int(data) * 2
#
#     elif typ == 'real':
#         return float(data) * 1.5
#
#     elif typ == 'string':
#         return f'${data}$'
#
#
# typ = input()
# data = input()
#
# print(datatype_check(typ, data))
