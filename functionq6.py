def small_number(list1,list2):
    i = 0
    new = []
    while i < len(list1):
        j = 0
        while j < len(list1):
            if list1[i] <= list2[j]:
                new.append(list1[i])
            j = j  + 1
        i = i  + 1
        print new
small_number([1,7,9,11],[2,4,8,15])

