# elif statement is used to  check the multiple condition 

today = 'Wednesday'
if today == 'Monday':
    print("Today is Monday")

elif today == 'Tuesday':
    print("Today is Tuesday")

elif today == 'Wednesday':
    print("Today is wednesday")  # it's going to print because the condition is fullfilled...

elif today == 'Friday':
    print("Today is Friday")

elif today == 'Saaturday':
    print("Today is saturday")



# Using if , elif  &  else statement together
a_number = 41
if a_number % 2 == 0:
    print("{} is divisible by 2".format(a_number))
elif (a_number % 3 == 0):
    print("{} is  divisible by 3".format(a_number))
elif (a_number % 4 ==0):
    print("{} is divisible by 4".format(a_number))
else:
    print("All conditions are checked.. Mission failed")