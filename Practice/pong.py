import turtle
import winsound

win = turtle.Screen()
win.title("Pong by Shawn")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Beat A
beat_a = turtle.Turtle()
beat_a.speed(0)
beat_a.shape("square")
beat_a.shapesize(stretch_wid = 5, stretch_len = 1)
beat_a.color("white")
beat_a.penup()
beat_a.goto(-350, 0)

# Beat B
beat_b = turtle.Turtle()
beat_b.speed(0)
beat_b.shape("square")
beat_b.shapesize(stretch_wid = 5, stretch_len = 1)
beat_b.color("white")
beat_b.penup()
beat_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0 V.S. Player B: 0", align = "center", font = ("JetBrains Mono", 20, "normal"))

# Function
def beat_a_up():
    y = beat_a.ycor()
    y += 30
    beat_a.sety(y)

def beat_a_down():
    y = beat_a.ycor()
    y -= 30
    beat_a.sety(y)

def beat_b_up():
    y = beat_b.ycor()
    y += 30
    beat_b.sety(y)

def beat_b_down():
    y = beat_b.ycor()
    y -= 30
    beat_b.sety(y)

# Keyboard input
win.listen()
win.onkeypress(beat_a_up, "w")
win.onkeypress(beat_a_down, "s")
win.onkeypress(beat_b_up, "Up")
win.onkeypress(beat_b_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("./Game/bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("./Game/bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} V.S. Player B: {score_b}", align = "center", font = ("JetBrains Mono", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} V.S. Player B: {score_b}", align = "center", font = ("JetBrains Mono", 20, "normal"))

    if beat_a.ycor() > 250:
        beat_a.sety(250)

    if beat_a.ycor() < -250:
        beat_a.sety(-250)

    if beat_b.ycor() > 250:
        beat_b.sety(250)

    if beat_b.ycor() < -250:
        beat_b.sety(-250)

    # Beat and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < beat_b.ycor() + 40 and ball.ycor() > beat_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("./Game/bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < beat_a.ycor() + 40 and ball.ycor() > beat_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("./Game/bounce.wav", winsound.SND_ASYNC)
