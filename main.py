# print("Hello world !")
# print("My name is is Nihar ")
# print("this is just the starting");  # semicolon not required in python - you will fall in love with how easy it is

# Here's another way of doing the same thing as above using Main function


# defining main function
def main():
    print("Hello world !")
    print("My name is is Nihar ")
    print("this is just the start")

if __name__ == "__main__":
    main() # calling above main function
    
    # Learning 'input' tool and making a basic calculator
    
    num1 = input("Enter a number")
    num2 = input("Enter another number")
    result = float(num1) + float(num2)
    print(result)
