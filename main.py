# from colorgram import extract
#
# rgb_colors = []
# colors = extract("hirst.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen, colormode
from random import choice

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61),
              (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39),
              (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202),
              (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205),
              (223, 178, 169)]

screen = Screen()
t = Turtle()
t.hideturtle()
t.speed("fastest")
t.penup()
t.setpos(-320, -270)
colormode(255)
# print(screen.window_width(), screen.window_height())

for i in range(10):
    for j in range(10):
        # t.color(choice(color_list))
        t.dot(20, choice(color_list))
        if j != 9:
            t.forward(64)
    if i != 9:
        t.left(90)
        t.forward(54)
        t.right(90)
        t.back(576)

screen.exitonclick()
