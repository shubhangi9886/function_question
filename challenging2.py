def multiply_func(numbers):
    i = 0
    multiply = 1
    while i < len(numbers):
        multiply = multiply * numbers[i]
        i = i + 1
    print multiply
multiply_func((8, 2, 3, -1, 7))