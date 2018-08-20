##ASSIGNMENT-4

##question 1

list = [1,2,3,4,5,6,7]
list.reverse()
print(list)

##question 2

str = ('J','a','A','T','T','l','o')
upper = 0
for i in str:
    if(i>="A" and i<="Z"):
        upper=upper+1
        print(i)

##question 3

x = input()
l=[]
a=x.split(',')
for i in a:
    l.append(int(i))
print(l)

##question 4

string = input("Enter string:")
if(string == string[::-1]):
    print("The string is a palindrome")
else:
    print("The string isn't a palindrome")


##question 5
import copy as c
x = [1,2,3,[4,5],6]
x2=c.deepcopy(x)
x[2]=88
print(x)
print(x2)


#difference --
import copy as c
x = [1,2,3,[4,5],6]
x2=c.deepcopy(x)
x[2]=88
print(x)
print(x2)  #only x is modified

import copy as c
x = [1,2,3,[4,5],6]
x2=c.copy(x)
x[3][1]=88
print(x)
print(x2)   #both x & x2 is modified