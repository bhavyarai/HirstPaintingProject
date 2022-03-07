# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('hirstspotpaint.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random
t.colormode(255)
timmy = t.Turtle()
screen = t.Screen()
color_list = [(190, 18, 44), (245, 232, 62), (220, 64, 106), (197, 175, 15), (201, 75, 29), (10, 143, 88),
              (210, 236, 242), (14, 126, 177), (106, 182, 211), (251, 220, 228), (10, 167, 215), (242, 232, 1),
              (24, 40, 78), (211, 150, 90), (34, 43, 112), (77, 176, 94), (215, 65, 48), (186, 42, 60), (221, 129, 156),
              (125, 185, 112), (239, 162, 182), (5, 60, 40), (146, 208, 221), (6, 90, 53), (4, 86, 111), (165, 28, 27),
              (238, 170, 162), (162, 212, 176)]
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
#timmy.setposition(0, 0)
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
for dot_count in range(1, 101):
    color = random.choice(color_list)
    timmy.dot(20, color)
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen.exitonclick()
