import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

# we have to create 6 new turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)



# Make the turtles move at random paces
if user_bet:
    is_race_on = True  # Only after a bet is made should the while loop below start to run

while is_race_on:
    for new_turtle in all_turtles:
        random_distance = random.randint(0, 10)
        new_turtle.fd(random_distance)
        if new_turtle.xcor() > 230:
            is_race_on = False
            winner_turtle_color = new_turtle.pencolor()
            if winner_turtle_color == user_bet:
                print(f"You've won! The {winner_turtle_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_turtle_color} turtle is the winner!")


screen.exitonclick()
