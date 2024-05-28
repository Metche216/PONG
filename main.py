from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONGAME')
screen.tracer(0)
screen.listen()

p1_paddle = Paddle(-350)
p2_paddle = Paddle(350)



screen.onkeypress(p2_paddle.up, "Up")
screen.onkeypress(p2_paddle.down, "Down")
screen.onkeypress(p1_paddle.up, "w")
screen.onkeypress(p1_paddle.down, "s")



game_on = True
while game_on:
    screen.update()














screen.exitonclick()