#ASSIGNMENT-13

#QUESTION-1
a=[5,6,8,9]
a=[i*i*i for i in a]
print(a)
#QUESTION-2
limit=int(input('enter the limit'))
a=[num for num in range(1,limit+1) if all(num % y != 0 for y in range(2, num))]
print(a)
#QUESTION-3
#LIST COMPREHENSION:-

# List comprehensions provide a concise way to create lists.
# We can create lists just like mathematical statements and in one line only.

#GENERATOR EXPRESSION:-

# In Python, to create iterators, we can use both regular functions and generators.
# Generators are written just like a normal function but we use yield() instead of return() for returning a result.
# It is more powerful as a tool to implement iterators.

#QUESTION-4

Celsius = [39.2, 36.5, 37.3, 37.8]
a=list(map(lambda x :(x*1.8)+32,Celsius))
print(a)

#QUESTION-5

a=[1,2,3,4,5]
a=list(map(lambda x:x*x,a))
print(a)

#QUESTION-6

def isPrime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
lst = [1,2,3,4,5,6,7,8,9,10]
f = list(filter(isPrime,lst))
print(f)

#QUESTION-7

from functools import *
lst = [1, 2, 3, 4, 5, 6, 7]
r = reduce(lambda x,y : x*y,lst)
print(r)