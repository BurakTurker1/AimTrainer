import turtle
import random
import time

Game_Screen = turtle.Screen()
Game_Screen.title("Aim Trainer")
Game_Screen.bgcolor("#cd7014")  # cd7014

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")

time_left = 15
random_x = 0.0
random_y = 0.0

turtle_write_skor = turtle.Turtle()
turtle_write_time = turtle.Turtle()

turtle_write_skor.penup()
turtle_write_time.penup()

turtle_write_skor.goto(0, 300)
turtle_write_time.goto(0, 250)

turtle_write_skor.hideturtle()
turtle_write_skor.isvisible()

turtle_write_time.hideturtle()
turtle_write_time.isvisible()


def turtle_time():
    global time_left
    while time_left > 0:
        turtle_write_time.clear()
        turtle_write_time.write(f"Süre: {time_left}", move=False, align='center', font=('arial', 12, ''))
        time_left -= 1
        time.sleep(1)



yazi_skor = turtle_write_skor.write("Skor: ", move=False, align='center', font=('arial', 12,''))
turtle_time()

while True:
    random_x = random.randint(-200, 200)
    random_y = random.randint(-200, 200)
    turtle_instance.penup()
    turtle_instance.speed(1)
    turtle_instance.setpos(random_x, random_y)
    turtle_instance.pendown()
turtle.mainloop()