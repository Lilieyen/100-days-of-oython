import turtle as t
import random
# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract('download.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     my_tuple = (r, g, b)
#     rgb_colors.append(my_tuple)
#
# print(rgb_colors)

# Make a hirst 10 by 10 painting using turtle
# thickness of dot is 20, spacing is 50
hirst = t.Turtle()
t.colormode(255)
colors = [(249, 246, 239), (238, 251, 246), (252, 242, 249), (241, 245, 251), (36, 19, 15), (196, 145, 125), (28, 106, 158), (8, 22, 46), (140, 87, 54), (237, 215, 87), (212, 73, 98), (199, 133, 154), (162, 14, 37), (158, 61, 91), (228, 82, 61), (13, 54, 29), (162, 165, 32), (116, 172, 198), (39, 127, 77), (78, 12, 22), (120, 189, 158), (17, 207, 179), (17, 93, 52), (11, 57, 142), (22, 173, 208), (136, 225, 209), (149, 22, 15), (238, 211, 4), (227, 169, 188), (237, 170, 162)]

hirst.speed("fastest")
hirst.hideturtle()
hirst.penup()

hirst.setheading(225)
hirst.fd(300)
hirst.setheading(0)

no_of_dots = 100
for dot_count in range(1, no_of_dots + 1):
    hirst.dot(20, random.choice(colors))
    hirst.fd(50)

    if dot_count % 10 == 0:
        # only when you get to 10, 20, 30, 40 and so on should you make a turn
        hirst.setheading(90)
        hirst.fd(50)
        hirst.setheading(180)
        hirst.fd(500)
        hirst.setheading(0)


screen = t.Screen()
screen.exitonclick()
