from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50 ,80]
turtles = []
for t_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t_index])
    new_turtle.penup()
    new_turtle.goto(x=-
    230, y=y_position[t_index])
    turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor().title()
            if winner == user_bet:
                print(f"You win! {winner} turtle wins!")
            else:
                print(f"You lose! {winner} turtle wins!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()