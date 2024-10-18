# Strings: ordered, immutable,text representation
from timeit import default_timer as timer

from numba import string
from sympy.codegen.ast import integer

#Concatenate string
my_string = 'greetings'
my_string2 = "david"
sentence= my_string+' '+my_string2 # '+' operator can be used to concatenate strings
print(sentence)

#use of slicing operator in string[Slicing operator does not consider the element at end index]
name="John Doe"
print(name[0:4])#start index 0, end index 4
print(name[0:]) #start index 0, end index 7 [if not provided by default it's the last element]
print(name[:5]) #start index [if not provided by default it's the first element], end index 5
print(name[-2:])#start index -2[negative index is considered from the last element,
# e is at -1 pos,o is at-2 pos and so on],end index 7
print(name[:-1])#start index is 0,end index is -1

#similarly list can also be sliced
my_list=[11,22,33,44,55,66,77]
print(my_list[0:3])

#slicing with :: operator
my_numb=[11,22,33,44,55,66,77]
print("My Numb")
print(my_numb[0::2])#start with 0 index ,here 2 is a span(gap) take every second element
print(my_numb[::3])#starts with 0 index by default,here 3 is a span(gap) take every second element
print(my_numb[-4::2])#start index -2,here 2 is a span
print(my_numb[-4::])#start index,if no span is mention all elements till the last is considered
print(my_numb[0::-1])#when start is 0,span is negative just first value is displayed at output
# [left direction to be traversed in search of element,since 0 is the left most element]
print(my_numb[-2::-5])#start is -2,span is -5 [left direction to be traversed in search of element]
print(my_numb[::-1])#reverses the array or string

#The capitalize() method in Python returns a copy of the string
# with the first character capitalized and all other characters in lowercase
name="JOHn DoE"
print(name.capitalize())

# the strip() method removes any leading and trailing whitespace from the string
name="   JOHn DoE    "
print(name.strip().upper())

# The startswith() method in Python checks whether a string begins with a specified substring and returns True or False
print(name.startswith('p'))

# The find() method in Python searches
# for a specified substring within a string and returns the index of the first occurrence.
# If the substring is not found, it returns -1.
name="JOHn DoE"
print(name.find('Do'))

# The replace() method in Python replaces occurrences of a specified substring with another substring.
name="JOHN DOE JOHN"
print(name.replace('JOHN','MATTHEW'))

#STRING TO LIST
# The split() method in Python splits a string into a list based on a specified delimiter
msg='How you doing'
my_list=msg.split(' ')
print(my_list)

# LIST TO STRING
# The join() method in Python combines elements of a list into a single string, using a specified separator
my_name_lst=['John','Doe']
my_name_str=' '.join(my_list)
print(my_name_str)
print(type(my_name_str))


#Replication
my_list = ['a'] * 1000000
# print(my_list)

#List to string conversion
#Calculating time difference between simple concatenate and join method ,using same string above

#Method 1 using simple concatenate
start = timer()
my_sen = ""
for items in my_list:
    my_sen += items
stop = timer()
print(stop - start)


#Method 2 using simple join, much faster with large number
start_1 = timer()
my_new_string=''.join(my_list)
stop1 = timer()
print(stop1 - start_1)



var=4.34234235
var2=6
my_string="the variable is %s" %var
# my_string="the variable is %d" %var
# my_string="the variable is %.2f" %var
# my_string="the variable is {:.2f} and {}".format(var,var2)
print(my_string)

# formatting
# %s-string
# %d-integer
# %.2f [float with two decimal points]