def is_perfect(some_number):
    sum_divisors = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            sum_divisors += divisor
        else:
            continue
    if sum_divisors == some_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(is_perfect(number))
