from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONGAME')
screen.tracer(0)
screen.listen()

p1_paddle = Paddle(-350)
p2_paddle = Paddle(350)

ball = Ball()

score = Scoreboard()

test = Turtle()
test.color('white')
test.penup()
test.goto(x=320, y=300)
test.pendown()
test.goto(x=320, y=-300)

screen.onkeypress(p2_paddle.up, "Up")
screen.onkeypress(p2_paddle.down, "Down")
screen.onkeypress(p1_paddle.up, "w")
screen.onkeypress(p1_paddle.down, "s")


# direction = "UR"

game_on = True
while game_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #DETECT COLLISION WITH RIGHT PADDLE
    if ball.x_move > 0 and ball.distance(p2_paddle) < 50 and ball.xcor() > 320  or ball.x_move < 0 and ball.distance(p1_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    
    #DETECT SCORE
    if ball.xcor() > 380:
        score.l_scored()
        ball.reset()
    elif ball.xcor() < -380:
        score.r_scored()
        ball.reset()



screen.exitonclick()