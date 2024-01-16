# #  Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:
# #
# #
# #     def __init__(self,a,b,r):
# #         self.a = a
# #         self.b = b
# #         self.r = r
# # 2 – Define a Area() method of the class which calculates the area of ​​the circle.
# # 3 – Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
# # 4 – Define a testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not.
# from math import pi
# class Circle:
#     def __init__(self,a,b,r):
#             self.a = a
#             self.b = b
#             self.r = r
#
#     def Area(self):
#         return pi*(self.r)**2
#
#     def Perimeter(self):
#         return 2*pi*(self.r)
#
#     def tetbelongs(self, A):
#         if ((self.a - A[0]) ** 2 + (self.b - A[1]) ** 2 == (self.r) ** 2):
#             return True
#         else:
#             return False
#
# myCircle=Circle(1,0,1)
# area = myCircle.Area()
# perimeter = myCircle.Perimeter()
# A= (1,1)
# test_belong = myCircle.tetbelongs(A)
#
# print("area",area)
# print("perimeter",perimeter)
# print("de",test_belong)


# Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student  which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# Create a student object via an instantiation on the Student class and then test the displayStudent method.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Person name :", self.name)
        print("age :", self.age)


class Student(Person):
    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def display_1(self):
        print("Person name :", self.name)
        print("age :", self.age)
        print("section", self.section)


my_class = Person("padmakshi",12)

print("-------------------------------------")
my_student= Student("princy",34,"A")
my_class.display()
my_student.display_1()