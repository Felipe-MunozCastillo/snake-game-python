from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.my_snake = []
        self.create_snake(position_x=0, position_y=0)
        self.head = self.my_snake[0]

    def create_snake(self, position_x, position_y):
        for number in range(3):
            snake = Turtle(shape="square")
            snake.penup()
            snake.color("white")
            snake.goto(position_x + (number * -20), position_y)
            self.my_snake.append(snake)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.my_snake.append(snake)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.my_snake[-1].position())

    def move(self):
        for seg_num in range(len(self.my_snake) - 1, 0, -1):
            new_x = self.my_snake[seg_num - 1].xcor()
            new_y = self.my_snake[seg_num - 1].ycor()
            self.my_snake[seg_num].goto(new_x, new_y)
        self.my_snake[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def reset(self):
        for seg in self.my_snake:
            seg.goto(1000, 1000)
        self.my_snake.clear()
        self.create_snake(0,0)
        self.head = self.my_snake[0]
