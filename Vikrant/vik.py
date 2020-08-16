#  # Testing Git folder
#
#
#
#
#
# # Trying Classes and Objects
#
# class Tab():
#
#     def __init__(self,title, is_current, page, class_page):
#         self.title = title
#         self.is_current = is_current
#         self.page = page
#         self.length = class_page.length
#         self.type = class_page.type
#
#     def close():
#         return "{} is currently {}".format(self.title, self.is_current)
#
#     def reload():
#         return "{} is currently reloading".format(self.page)
#
#
# class Page(Tab):
#
#     def __init__(self,length,type):
#         self.length = length
#         self.type = type
#
#
#
#
#
#
# class Person:
#
#     description = "general person"
#
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print("My name is {} and I am {} years old".format(self.name, self.age))
#
#     def eat(self, food):
#         print("{} eats {}".format(self.name, food))
#
#     def action(self):
#         print("{} spins".format(self.name))
#
#
#
# class Baby(Person):
#
#     description = "baby" # overwriting
#
#     def __str__(self):
#         return '__str__ for Baby'.format(self=self)
#
#     def __repr__(self):
#         return '__repr__ for Baby'
#
#     def speak(self):
#         print("ba ba ba")
#
#     def nap(self):
#         print("{} takes a nap".format(self.name))
#
#
#
# person = Person("Steve", 20)
# person.speak()
# person.eat("pasta")
# person.action()
#
#
# baby = Baby("Ian", 1) # attributes inherited from parent class
# baby.speak()
# baby.eat("Baby food")
# baby.action()
#
# print(person.description)
# print(baby.description)
#
#
#
# print(isinstance(baby, object))
# print(baby) # memory adress on Cpython

# import datetime
# today = datetime.date.today()
# print(str(today))
# print(repr(today))
#
#
# # __str__ __repr__ # dunder methods
#
#
#
# class Car:
#
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
#
#     def __repr__(self):
#         return 'Car({self.color}, {self.mileage})'.format(self=self)
#
# my_car = Car('Red', 37200)
# print(my_car)
# print(str(my_car))
#
#
# al = str([today, today, today])
# print(al)

#
# class Square:
#
#     def __init__(self, length):
#         self.length = length
#
#     def area(self):
#         return self.length * self.length
#
#     def perimeter(self):
#         return 4 * self.length
#
#
#
#
# class Cube(Square):
#     # same parameeters as Square so no need to define init
#
#     def surface_area(self):
#         face_area = self.area()
#         return face_area * 6
#
#     def volume(self):
#         face_area = super().area()
#         return face_area * self.length
#
#
#
# # Multiple Inhritance
#
#
# class Triangle:
#
#     def __init__(self, base, height):
#         self.base = base
#         self.slant_height = slant_height
#
#     def what_am_i(self):
#         return 'RightPyramid'


# Inheritance and Composition
