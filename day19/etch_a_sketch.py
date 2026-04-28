from turtle import Turtle, Screen

chaz = Turtle()
screen = Screen()

def move_forward():
    chaz.forward(10)
def move_backward():
    chaz.backward(10)
def turn_left():
    chaz.left(10)
def turn_right():
    chaz.right(10)
def clear():
    chaz.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()