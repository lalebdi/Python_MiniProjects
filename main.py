from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("pink")


# def square():
#     timmy_the_turtle.left(90)
#     timmy_the_turtle.forward(100)
#
# timmy_the_turtle.forward(100)
# square()
# square()
# square()

for _ in range(10):
    timmy_the_turtle.forward(15)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()


screen = Screen()
screen.exitonclick()

