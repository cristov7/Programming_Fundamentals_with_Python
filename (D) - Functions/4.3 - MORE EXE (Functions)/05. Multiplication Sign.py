def multiplication_sign(number_1: int, number_2: int, number_3: int):
    numbers_list = [number_1, number_2, number_3]
    counter_minus = 0
    for number in numbers_list:
        if number == 0:
            return "zero"
        else:
            if number < 0:
                counter_minus += 1
            else:
                continue
    if counter_minus % 2 == 0:
        return "positive"
    else:
        return "negative"


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(multiplication_sign(first_number, second_number, third_number))


# def chk_sign(l):
#
#     if all(l):
#
#         negatives = [num for num in l if abs(num) != num]
#
#         if len(negatives) % 2 == 1:
#             return 'negative'
#
#         return 'positive'
#
#     return 'zero'
#
#
# nums = [int(input()) for _ in range(3)]
#
# print(chk_sign(nums))
