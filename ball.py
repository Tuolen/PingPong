from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_distance = 10
        self.y_distance = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_distance
        new_y = self.ycor() + self.y_distance
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_distance *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_distance *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.move_speed = 0.1
        self.x_distance = 10
        self.y_distance = 10
        self.goto(0, 0)
        self.bounce_x()


