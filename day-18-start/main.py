# from turtle import Turtle, Screen
import random
import turtle as t

tim = t.Turtle()

# tim.pensize(5)
tim.speed("fastest")
t.colormode(255)

# tim.shape("turtle")
# tim.color("blue")

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
# "Wheat", "SlateGray", "LightSeaGreen", "SeaGreen", "DeepSkyBlue"]

# Make the turtle form a square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# Draw a dashed line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Draw different shapes from triangle to decagon
# def draw_shape(number_of_sides):
#     angle = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_sides in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_sides)

# Make the turtle do a random walk
# my_tuple = ()
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_tuple = (r, g, b)
#     return my_tuple
#
# directions = [0, 90, 180, 270]
# for _ in range(200):
#     tim.forward(10)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())


# Draw a spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple

def draw_spirograph(dst_btn_circles):
    tilt = 360 / dst_btn_circles
    for _ in range(int(tilt)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + dst_btn_circles)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
