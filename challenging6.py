new_list = []
def even_numbers(list1):
    i = 0
    while i < len(list1):
        if list1[i] % 2 == 0:
            new_list.append(list1[i])
        i = i + 1
    print new_list
even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])