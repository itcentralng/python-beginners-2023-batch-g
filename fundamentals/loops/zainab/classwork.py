for num in range(2, 36):
    factors = 0
    for divisor in range(2, num):
        if num % divisor == 0:
            factors += 1
    if factors == 0:
        print(num)        



def combo_colors(c1, c2):
    primary_colors = ['red', 'blue', 'yellow']
    if (c1 == 'red' and c2 == 'blue') or (c1 == 'blue' and c2 == 'red'):
        return 'purple'
    elif (c1 == 'red' and c2 == 'yellow') or (c1 == 'yellow' and c2 == 'red'):
        return 'orange'
    elif (c1 == 'blue' and c2 == 'yellow') or (c1 == 'yellow' and c2 == 'blue'):
        return 'green'
c1 = 'red'
c2 = 'blue'
result = combo_colors(c1, c2)
print(f"{c1} and {c2}.")
