for num in range(2, 36):
    factors = 0
    for divisor in range(2, num):
        if num % divisor == 0:
            factors += 1
    if factors == 0:
        print(num)        