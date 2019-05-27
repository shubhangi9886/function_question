def odd_func(list1,list2):
    i = 0
    while i < len(list1):
        if list1[0] + list2[0] % 2 != 0:
            print "Yes odd number" 
        else:
            print "Not even number"
        i  = i + 1
odd_func([23,46,49,50],[24,54,87,34])
  