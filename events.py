from turtle import Turtle, Screen

ninja = Turtle()
screen = Screen()


def move_forward():
    ninja.forward(10)


def move_backward():
    ninja.backward(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun= (lambda : ninja.right(5)))
screen.onkey(key="d", fun=lambda : ninja.left(5))
screen.exitonclick()