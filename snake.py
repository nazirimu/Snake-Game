from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20


class Snake:

    # initializes the snakes body with 3 squares
    def __init__(self):
        self.width = 0
        self.snake_segment = []
        self.create_snake()
        self.head = self.snake_segment[0]

    # The create function is called to create the body
    def create_snake(self):
        for position in range(3):
            self.add_segment(position)

    # Adds the segment to the body of the snake
    def add_segment(self,position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.setpos(self.width, 0)
        self.width -= 20
        self.snake_segment.append(snake)

    # Extends the new segment to the snake when it is called.
    def extend(self):
        self.add_segment(self.snake_segment[-1].position())

    # moves the snake
    def move(self):
        for piece in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[piece - 1].xcor()
            new_y = self.snake_segment[piece - 1].ycor()
            self.snake_segment[piece].goto(new_x, new_y)
        self.snake_segment[0].forward(MOVE_DISTANCE)

    # Changes the direction of the snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

