# Collect user's name and number to check

name = input("Please enter your name: ")
number = int(input("Please enter a number: "))

# Welcome the user and print out their number

print("Welcome, {}! Your number, {}...".format(name, number))

# FizzBuzz conditions. 
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************

# Create variables for Fizz and Buzz, and store the results as a boolean

is_fizz = number % 3 == 0
is_buzz = number % 5 == 0

# Using the variables, check the condition of the value, and print the necessary
# string

if (is_fizz) and (is_buzz):
  print("is a FizzBuzz number.")
elif is_fizz:
  print("is a Fizz number.")
elif is_buzz:
  print("is a Buzz number.")
else:
  print("is neither a fizzy or a buzzy number.")
