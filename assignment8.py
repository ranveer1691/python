##ASSIGNMENT-8
# Question-1
class circle:
    """______"""

    def __init__(self, r):
        self.radius = r

    def getArea(self):
        return 3.14 * self.radius * self.radius

    def getCircumference(self):
        return 2 * 3.14 * self.radius


t1 = circle(5)
print(t1.__doc__)
print("area of circle is ", t1.getArea())
print('circumference of circle is {}'.format(t1.getCircumference()))


# Question-2


class Student:
    def __init__(self, name, rno):
        self.n = name
        self.r = rno

    def Display(self):
        print('name {}\n rollno of {}'.format(self.n, self.r))

    def setAge(self, age):
        self.age = age
        print('here we have set age of {} as {} '.format(self.n, self.age))

    def setMarks(self, m):
        self.marks = m
        print('here we have set marks of {}  as {} '.format(self.n, self.marks))


t1 = Student('gabru', 1610991691)
t1.Display()
t1.setAge(20)
t1.setMarks(98)


# Question-3
class Temprature:
    def __init__(self):
        print("converting Temprature")

    def convertFahrenheit(self, c):
        self.c = c
        print('the {}C ->{}F'.format(self.c, ((self.c * 9 / 5) + 32)))

    def convertCelsius(self, f):
        self.f = f
        print('the {}F ->{}C'.format(self.f, ((self.f - 32) * 5 / 9)))


t1 = Temprature()
t1.convertFahrenheit(-10)
t1.convertCelsius(0);


# Question-4

class MovieDetails:
    def __init__(self, a, y, rr):
        self.a = a
        self.y = y
        self.rr = rr
        print("Create a class MovieDetails")

    def display(self):
        print('artist name {}\n year of release {}\n ratings {} star'.format(self.a, self.y, self.rr))

    def setaddmoviedetails(self, actorname):
        self.ac = actorname
        print('actorname added now using setter fun is {}'.format(self.ac))


t1 = MovieDetails('shahruk', 1998, 5)
t1.display()
t1.setaddmoviedetails('ranveersingh')


# Question-5

class Animal:
    def animal_attribute(self):
        print("base clas animal_attribute ")


class Tiger(Animal):
    def dis(self):
        print("derievd class called")


r = Tiger()
r.dis()
r.animal_attribute()


# question 6
# ans is A B
#        A B


# Question-7


class Shape:
    def __init__(self, ll, bb):
        self.l = ll
        self.b = bb

    def Area(self):
        '''area method created'''


class rectangle(Shape):

    def Area(self):
        print('area of rectangle is ', (self.l * self.b))


class square(Shape):

    def Area(self):
        print('area of square is ', (self.l * self.l))


r = rectangle(5, 6)
r.Area()
q = square(5, 6)
q.Area()