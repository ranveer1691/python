#ASSIGNMENT-6

##Question-1

def area(num):
    ar = float(4 * 3.14 * num * num)
    return ar
r = int(input("radius of a sphere: "))
x = area(r)
print(x, " Area of Sphere")


##Question-2

def perfect(num):
    sm = 0
    for j in range(1, num):
        if num % j == 0:
            sm += j

    return sm == num


for i in range(1, 1001):
    if perfect(i):
        print(i)


##Question-3

def table(num):
    for j in range(1, 11):
        y = num * j
        print(num, " x ", j, " = ", y)


x = int(input("enter number"))
table(x)

# Question-4

def power(a, b):
    x = a
    if b == 1:
        return a
    if b > 0:
        b -= 1
        x *= power(a, b)
        return x
    return 1


p = int(input("Enter Number: "))
q = int(input("Enter Power: "))
print(power(p, q))
