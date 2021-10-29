from turtle import Turtle, Screen
import random

# race on off variable
is_race_on = False

# declaring the screen
screen = Screen()

# setting up the height and width of the screen
screen.setup(width=500, height=400)

# asking the user input and saving it to the variable
user_bet = screen.textinput(
    title="Make Your bet", prompt="Which turtle will win the race? Enter a color:")

# colors for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# declaring the y positions
y_positions = [-100, -60, -20, 20, 60, 100]

# empty list
all_turtles = []


for turtle_index in range(0, 6):
    # declaring the turtles
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(
                    f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(
                    f"You have lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
