#question1

list=[]
x1 = input("enter first varible")
list.append(x1)
x2 = input("enter second varible")
list.append(x2)
x3 = input("enter third varible")
list.append(x3)
x4 = input("enter fourth varible")
list.append(x4)
x5 = input("enter fifth varible")
list.append(x5)
print(list)

#question 2

list2=['google','apple','facebook','microsoft','tesla']

list.append(list2)

print(list)

#question 3

print(list.count('apple'))

#question 4

list3 = [4,45,6656,67,3,5]
list4 = []
list4 = sorted(list3)
print(list4)


#question 5
z = []
x = [1,2,3,4,5]
y = [3,7,88,999,1001]
z = x + y
z.sort()
print(z)

#question 6

list=[1,2,3,4,5,6,7,8,9,10]
even = 0
odd = 0
for i in list:
    if(i%2==0):
        print(i,"even")
    if(i%2!=0):
        print(i,"odd")

##TUPLES


#Question 1
X=(1,2,3,4,5)
print(X[::-1])

#Question 2
X=(1,2,3,4,5,6,7,8,9)
print("Largest element is ",max(X))
print("Smallest elementi s ",min(X))

##STRINGS

#question1

r=input()
print(r.upper())

#question2

r=input()
print(r.isdigit())

#question3


a=input()
b="ranveer"
a=b
print(a)
