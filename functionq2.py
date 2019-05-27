def even_func(list1):
    i  = 0
    while i < len(list1):
        if list1[i] % 2 == 0:
            print "even number"
        else:
            print "odd number"
        i = i + 1
even_func([34,23,67,54,89])
