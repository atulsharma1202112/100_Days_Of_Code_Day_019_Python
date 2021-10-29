from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_clock_wise():
    tim.right(90)


def move_counter_clock_wise():
    tim.left(90)


def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(move_forwards, "w")  # passing function as a input
screen.onkey(move_backwards, "s")  # passing function as a input
screen.onkey(move_clock_wise, "d")  # passing function as a input
# passing function as a input
screen.onkey(move_counter_clock_wise, "a")
screen.onkey(clear_screen, "c")  # passing function as a input
screen.exitonclick()
