# ASSIGNMENT-9
#Question-1

try:
    a = 3
    a < 4
    a = a / (a - 3)
except ZeroDivisionError as msg:
    print('wrong', msg)
#Queation-2

try:
    l = [1, 2, 3]
    print(l[3])
except IndexError as msg:
    print('something went wrong', msg)
#Question-3
'''
NameError:hi there
'''
#Question-4

# output
'''
-5
a/b result in 0
'''
#Question-5

try:
    l = [1, 2, 3]
    print(l[3])
except IndexError as msg:
    print('Index errror occurs in list', msg)
# Value Error-
try:
    a = int(input('enter a number'))
    print(a + 2)
except ValueError as msg:
    print('Value error occurs in a list', msg)
# Import Error-
try:
    import abcde
except ImportError as msg:
    print(msg)
