def prime_func(a):
    user = int(raw_input("enter your number"))
    i = 2
    while  i < user:
        if user % i == 0:
            print "Not prime",user
            break
            i = i + 1
    else:
        print "Yes prime",user
prime_func(23)
