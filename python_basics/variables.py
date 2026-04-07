# variables
# A variable in Python is a name used to store a value in memory so the program can use, change, or display that value later.

# Key points you should remember
# 1) A variable stores data
# 2) The value can change during program execution
# 3) Python does not require declaring the data type
# 4) The assignment operator = is used to create a variable
 
# Syntax: variable_name = value

# Allowed:
# name = "Ravi"
# user_age = 21
# _total = 100

# Not allowed:
# 1name = "Ravi"     # starts with number
# user name = 21     # space not allowed

#Key rules:
# Must start with a letter or underscore
# Cannot start with a number
# No spaces allowed
# Case-sensitive (age and Age are different)

# These four cover most real programs.
name = "Vivek"      # String
age = 22            # Integer
height = 5.8        # Float
is_student = True   # Boolean

# Meaning:
# String → text
# Integer → whole number
# Float → decimal number
# Boolean → True or False

# Multiple assignment
x, y, z = 1, 2.5, "Hello"
# same value to multiple variables:
a1 = b1 = c1 = 5
# Checking the type of variable
print(type(age))
# input 
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Practice problems
a = 10
b = 20
sum_ab = a + b
print(f"The sum of a and b is: {sum_ab}")

# Problem 2: Swap two variables
x = 5
y = 10
print(f"Before swap: x = {x}, y = {y}")
temp = x
x = y
y = temp
print(f"After swap: x = {x}, y = {y}")

# Problem 3: Calculate area of rectangle
length = 5.5
width = 3.2
area = length * width
print(f"Area of rectangle: {area}")

# Problem 4: String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Problem 5: Boolean operations
is_raining = True
has_umbrella = False
should_take_umbrella = is_raining and not has_umbrella
print(f"Should take umbrella: {should_take_umbrella}")
b = 20
sum_value = a + b
sub_value = a - b
mul = a * b
print("The sum of a and b is:", sum_value)
print("The subtraction of a and b is:", sub_value)
print("The multiplication of a and b is:", mul)
div = a / b
divv = a // b
    
print("The division of a and b is:", div)
print("The floor division of a and b is:", divv)