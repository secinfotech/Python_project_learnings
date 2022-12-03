import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
directions = [0, 90, 180, 270]
tim.width(20)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    changing_color = (r, g, b)
    return changing_color


for _ in range(500):
    tim.color(random_color())
    tim.forward(50)
    tim.setheading(random.choice(directions))
