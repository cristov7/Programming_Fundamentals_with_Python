number = int(input())
for numbers in range(1, number + 1):
    sum_of_digits = 0
    digits = numbers
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)
    if sum_of_digits == 5 \
            or sum_of_digits == 7 \
            or sum_of_digits == 11:
        print(f"{numbers} -> True")
    else:
        print(f"{numbers} -> False")
