# IF STATEMENT = A BLOCK OF CODE THAT WILL EXECUTE IF IT'S CONDITION IS TRUE 

age = int ( input("HOW OLD ARE YOU  "))

if age >= 18 :
    print ("Yuo're an adult ")

elif age == 0 :
    print ("Your'e have not even born yet  ")
    
elif age <= 18 :        #  elif statement is used as else if !

    print ("You're a child ")

elif age == 0 :
    print ("Your'e have not even born yet  ")

else :
    print (" you are an asshole ")

# now if we are entering the value negative number but it's printing "YOu're a child "
# because it's also satisfying this block of code and as the code .....
# so we have to be very carreful about choosing the block of code [ in correct order ]