##ASSIGNMENT-5

#Question-1

year = int(input("Enter year:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("Leap Year")
else:
    print("Isn't a leap year")

#Question=2

length = int(input("Enter length"))
breadth = int(input("Enter breadth"))
if(length==breadth):
    print("It's a Square")
else:
    print("It's a Rectangle")

#Question-3

age1 = int(input("enter age of first person: "))
age2 = int(input("enter age of second person: "))
age3 = int(input("enter age of third person: "))
print("oldest",max(age1,age2,age3))
print("youngest",min(age1,age2,age3))


#Question-4

age = int(input("Enter Age: "))
sex = input("Enter sex(M or F: ")
ms = input("Enter marital status ( Y or N): ")

if(sex == 'F'):
    print("She will work only in urban areas. ")
elif(sex == 'M' and age>19 and age<41):
    print("He can work Anywhere")
elif(sex == 'M' and age>39 and age<61) :
    print("He will work only in urban areas. ")
else:
    print("ERROR")



#Question-5

cost = int(input("Enter the cost"))
if(cost >= 1000):
    cost = cost-(cost*0.1)
    print(cost,"After discount")
else:
    print(cost)


##--LOOPS

#question-1

for i in range(0,10):
    n=int(input("Enter integer: "))
    print(n)

#question-2

while(True):
    print("This is a infinite loop")

#question-3

n = int(input("enter the size: "))
lst = []
for i in range(0, n):
    x = int(input())
    lst.append(x)
list1 = []
for i in lst:
    list1.append(i*i)
print (list1)


##Question-4

st=[]
fl=[]
iy=[]
l=[1,2,3,4,'a','b','c','d',9.00,1.00,8.786]
for i in l:
    if(type(i) is str):
        st.append(i)
    elif(type(i) is float ):
        fl.append(i)
    elif(type(i) is int):
        iy.append(i)
print("List of integer type is ",iy)
print("List of float type is ",fl)
print("List of string type is",st)

##Question--5

for num in range(1,101):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)



##Question--6

for i in range(0, 5):
    for j in range(0, i+1):
        print("* ", end="")
    print()

##Question--7

n = int(input())
x=[]
for i in range(0,n):
    lst = int(input())
    x.append(lst)
t = int(input("Enter the number to search"))
pos = -1
for i in range(0,n):
    if x[i] == t:
        pos = i
        x.pop(pos)
        break
if pos == -1:
    print("Item not found.")
else:
    print("Item deleted.")
print (x)
