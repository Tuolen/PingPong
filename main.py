import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
TIME_CONSTANT = 0.08

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Detect collision with the wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() >= 330:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() <= -330:
        ball.bounce_x()
    if ball.xcor() >= 400:
        ball.reset()
        scoreboard.l_point()
    if ball.xcor() <= -400:
        ball.reset()
        scoreboard.r_point()



screen.exitonclick()