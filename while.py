''' While loop is used for itration ( repetation of same process ).....
'''
result = 1
i = 1

while ( i<= 10):
    result = result*i
    i = i + 1
print('The factorial of 10 is: {}'.format(result))


# using time function 

import time
start_time = time.time()

result = 1
i = 1

while ( i<= 50):
    result = result*i  
    i = i + 1
print('The factorial of 50 is: {}'.format(result))

print(start_time)

