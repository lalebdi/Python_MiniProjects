print("This costs " + str(6) + " dollars")

splitting_text = "Hello:Leah".split(":")
print(splitting_text)

greeting = "My name is " + splitting_text[1]
print(greeting)

me = {"name" : "Leah", "age" : 21, "hobby": "running"}
print(me)
print(me['hobby'])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  pep is python's style guide
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def function_test(str1):
#     print("Hi ", str1)

# x = input("What's your name? ")
# function_test(x)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Default arguments:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def print_something(name, age = 21): # when you do a default argument, just like the case with age, you only need to throw pass argument. If you add the other argument you, it will take it instead. 
    print("Hi, my name is ", name, "and I am ", age, "years old")

print_something("Natasha")
print_something("Leah", 22)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Keyword Argument: None === null
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def second_print(name = "someone", age = "Old"):
    print("I am the second funtion. So, Hi", name, "you are", age, "years old")

second_print("Bella", 9)
second_print( age = 7, name= "Maryusa") # <- these are the keyword arguments. 
second_print()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Infinte arguments:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def print_people(*people): # the * will tell the function that there going to be more than one argument. It needs a for loop
    for person in people:
        print("This person's name is ", person)

print_people("Leah", "Natasha", "Bella")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Return Values:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def do_math(num1, num2):
    return num1 + num2

math1 = do_math(2, 4)
print(math1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Regex: is a way to match something and do something about it
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import re

string= " 'I AM NOT YELLING', she said, Though we knew it to not be true."

print(string)
# Rules are contained in []
new = re.sub('[A-Z]', '', string) # substitue function and it take 3 params (the match we wannt to make, what we want to replace them with, the varibale we want to manipulate )
print(new) # removed the capital letters
new = re.sub('[a-z]', '', string) # removing the small letters
print(new)
new = re.sub('[.,\']', '', string) # removing the punctuations. these are the dot, comma, then the escape and the apostrophy
print(new)
new = re.sub('[.,\'A-Z]', '', string) # removing the punctuations and capital letters
print(new)
string = string + " 6 298 - 345"
new = re.sub('[^0-9]', '', string) # removing everything but the numbers
print(new)