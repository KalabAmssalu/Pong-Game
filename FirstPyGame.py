import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @Kalab_KABA")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#boarder left

boarder_left = turtle.Turtle()
boarder_left.speed(0)
boarder_left.shape("square")
boarder_left.color("blue")
boarder_left.shapesize(stretch_wid=30, stretch_len=1)
boarder_left.penup()
boarder_left.goto(-400, 0)

#boarder right

boarder_right = turtle.Turtle()
boarder_right.speed(0)
boarder_right.shape("square")
boarder_right.color("blue")
boarder_right.shapesize(stretch_wid=30, stretch_len=1)
boarder_right.penup()
boarder_right.goto(400, 0)

#boarder top

boarder_top = turtle.Turtle()
boarder_top.speed(0)
boarder_top.shape("square")
boarder_top.color("blue")
boarder_top.shapesize(stretch_wid=1, stretch_len=41)
boarder_top.penup()
boarder_top.goto(0, 300)

#boarder bottom

boarder_bottom = turtle.Turtle()
boarder_bottom.speed(0)
boarder_bottom.shape("square")
boarder_bottom.color("blue")
boarder_bottom.shapesize(stretch_wid=1, stretch_len=41)
boarder_bottom.penup()
boarder_bottom.goto(0, -300)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1


#Center_point

center_point = turtle.Turtle()
center_point.speed(0)
center_point.shape("circle")
center_point.color("pink")
center_point.penup()
center_point.goto(0, 0)

#centeral_line

central_line = turtle.Turtle()
central_line.speed(0)
central_line.shape("square")
central_line.color("pink")
central_line.shapesize(stretch_wid=29.4, stretch_len=0.1)
central_line.penup()
central_line.goto(0, 0)


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A:0   player B:0", align="center", font = ("courier", 20, "normal"))

# score
score_a = 0
score_b = 0 
# Function 

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding 
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#main game loop
while True:
    wn.update()
    

# move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("player A:{}   player B:{}".format(score_a, score_b) , align="center", font = ("courier", 20, "normal"))
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A:{}   player B:{}".format(score_a, score_b) , align="center", font = ("courier", 20, "normal"))
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

