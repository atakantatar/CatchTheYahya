import turtle
import random

turtleScreen = turtle.Screen()
turtleScreen.bgcolor("light blue")
turtleScreen.title("Catch The Yahya!")
points = 0
time = 20
yahya = turtle.Turtle()
yahya.hideturtle()
yahya.penup()
yahya.color("dark blue")

mistik = turtle.Turtle()
mistik.hideturtle()
mistik.penup()

turtle1 = turtle.Turtle()
turtle1.penup()
turtle1.hideturtle()
turtle1.color("dark green")
for a in range(20):
    xAxis = round(random.uniform(-330.0,330.0),4)
    yAxis = round(random.uniform(-230.0,230.0),4)
    xClick = 0.0
    yClick = 0.0
    def get_mouse_click_coor(x, y):
        global xClick, yClick
        xClick = x
        yClick = y

    turtle.onscreenclick(get_mouse_click_coor)

    drawingBoard = turtle.Screen()
    drawingBoard.bgcolor("light blue")

    mistik.setposition(0, 280)
    mistik.write(f"Time: {time}", align="center", font=('Arial', 27, 'normal'))

    yahya.setposition(0, 320)
    yahya.write(f"Score: {points}", align="center",font=('Arial', 27, 'normal'))

    turtle1.speed("fastest")
    turtle1.setx(xAxis)
    turtle1.sety(yAxis)
    turtle1.pendown()
    turtle1.begin_fill()
    turtle1.pensize(5)
    turtle1.circle(15)
    turtle1.end_fill()
    turtle1.left(90)
    turtle1.fd(15)
    turtle1.left(45)
    turtle1.fd(25)
    turtle1.left(180)
    turtle1.fd(50)
    turtle1.left(180)
    turtle1.fd(25)
    turtle1.left(90)
    turtle1.fd(25)
    turtle1.left(180)
    turtle1.fd(50)
    turtle1.left(180)
    turtle1.fd(25)
    turtle1.left(135)
    turtle1.fd(25)
    turtle1.pensize(9)
    turtle1.fd(5)
    turtle1.penup()
    turtle1.speed("slowest")
    turtle1.fd(80)
    turtle1.pendown()
    drawingBoard.clearscreen()
    if xClick - 30.0 < xAxis < xClick +30.0 and yClick-30.0<yAxis<yClick+30.0:
        points +=1
    time -=1
    print(points)
turtleScreen = turtle.Screen()
turtleScreen.bgcolor("light blue")
turtleScreen.title("Beypazarı Maden Suyu")

mistik.setposition(0, 280)
mistik.write(f"Game Over!", align="center", font=('Arial', 35, 'normal'))

yahya.setposition(0, 320)
yahya.write(f"Points: {points}", align="center",font=('Arial', 35, 'normal'))

turtle.mainloop()
