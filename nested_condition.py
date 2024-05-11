a_number = 15

if (a_number % 2 == 0):
    print("{} is even ".format(a_number))
    if ( a_number % 3 == 0 ):
        print("{} is also divisible by 3".format(a_number))
    else:
        print("{} is not divisble by 3".format(a_number))
else:
    print("{} is a odd ".format(a_number))
    if ( a_number % 5 == 0):
        print("{} is also divisible by 5".format(a_number))
    else:
        print("{} is not divisible by 5".format(a_number))