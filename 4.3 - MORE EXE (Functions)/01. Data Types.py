def type_function(variable):
    if variable == "int":
        number = int(input())
        result = number * 2
        return result
    elif variable == "real":
        number = float(input())
        result = number * 1.5
        return f"{result:.2f}"
    elif variable == "string":
        text = input()
        return f"${text}$"


enter_type = input()
print(type_function(enter_type))


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
