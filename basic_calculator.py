import re

print(" The Python Calculator")
print("Type quit to exit")

previous = 0

run = True

def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter the equation: ")
    else:
        equation = input(str(previous))
    if equation == "quit":
        print("Bye")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

    

while run:
    perform_math()