 # break statement

''''i = 1
result = 1
while (i <= 100):
    result = result*i
    if (i == 42):
        print("The desired number 42 has reached")
        break   # using the break statement we can easily terminate the statement....
    i = i+1

print("i:",i)
print("result",result)'''

# continue statement

j = 1
result = 1

while( j < 20):
    j = j+1
    if (j % 2 == 0):
        print("Skipping {}".format(j))
        continue
    print("Multiplying with {}".format(j))
    result = result * j
print("i :" , j)
print("result :",result) 