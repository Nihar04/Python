
# How to merge two dictionaries in python
x = {'a':1, 'b':2, 'c':3}
y = {'b':3, 'c':8}



z = {**x,**y}
print(z)



# Different ways to test multiple flags in python
x,y,z = 1,0,1

if x == 1 or y == 1 or z == 1:
     print("passed")


if 1 in (x,y,z):
    print("passed")

if x or y or z:
    print("passed")

if any((x,y,z)):
    print("passed")


# How to sort a python dictionary by value
xs = {'a':4, 'b':3, 'c':2, 'd':1}

# print(sorted(xs.items(), key=lambda x:x[2]))
print(xs.items())
# operator.itemgetter(1)

import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))
