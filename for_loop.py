''' A 'for' loop is used for iterating or looping over sequences i.e. lists ,
    dictionaries , string and ranges.'''

days =['monday','tuesday','wednesday','friday','saturday']
for day in days:
    print(day)

# loop over a dictionary ( very useful )
person = {
    'name':'Eman Gope',
    'sex' :'male',
    'age': 19 ,
    'girlfriend':'Sumana Gope'
}
for key in person:
    print("key :" , key ," , " 'Value :',person[key])

for value in person.values():
    print(value)

# to print something within a range we also use the for loop

for i in range(10):  # this print upto 9
    print(i)

print("next code")

for j in range(3,10):  # this wll print from 3 to 9
    print(j)

print("next code")
for k in range(3,14,4):  #( start index , end index(-1),iteratation gap) so output = 3,7,11
    print(k)

 # checking the index of a list 

a_list = [ 'Monday','Tuesday','Wednesday','Thrusday','Friday']
for i in range(len(a_list)):
    print("The value at position {} is {}".format(i,a_list[i]))

print('\n')

# break and continue in for loop
weekdays = [ 'Monday','Tuesday','Wednesday','Thrusday','Friday']

for day in weekdays :
    print('Today is {}'.format(day))
    if( day == 'Wednesday'):
        print("I don't work after Wednesday")
        break

print("\n")

for day in weekdays :
    print('Today is {}'.format(day))
    if( day == 'Wednesday'):
        print("I don't work after Wednesday")
        continue