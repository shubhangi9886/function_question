new = []
def same_elements(list1):
    i = 0
    while i < len(list1):
        if list1[i] not in new:
            new.append(list1[i])
        i = i +  1
    print new
same_elements([1,2,3,3,3,3,4,5])