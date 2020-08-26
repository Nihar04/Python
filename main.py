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
    #learning if statements
    is_male = True
is_tall = True

if is_male and is_tall:
    print("You are male and tall both")
elif is_male  and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You aren't a male but is tall")
else:
    print("You are neither male nor tall")

    
 #   THE GUESSING GAME
secert_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
outofguesses = False

while guess != secert_word and not (outofguesses):
  if guess_count< guess_limit:
      guess = input("Enter your guess:")
      guess_count += 1
  else:
   outofguesses = True

if outofguesses:
    print("You are out of guesses ,You Lose!")
else:
   print("you win!")
