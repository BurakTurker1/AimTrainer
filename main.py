import turtle
import time
import random

Game_Screen = turtle.Screen()
Game_Screen.title("Aim Trainer")
Game_Screen.bgcolor("#cd7014")

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")

while True:
    random_x = random.randint(-200, 200)
    random_y = random.randint(-200, 200)
    turtle_instance.penup()
    turtle_instance.speed(1)
    turtle_instance.setpos(random_x, random_y)
    turtle_instance.pendown()
turtle.mainloop()

