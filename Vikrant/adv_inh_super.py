
# Inheritance and Composition


# class MyClass:
#
#     pass
#
# c = MyClass()
# print(dir(c))

class MyError(Exception):

    def __init__(self,message):
        super().__init__(message)


raise MyError("Vikrant Gawde")

# What is an interface?

class PayrollObject:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return '$12345';
