from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEADINGS = [0, 90, 180, 270]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.snake_segments = []
        self.snake_body()
        self.head = self.snake_segments[0]

    def snake_body(self):
        for position in STARTING_POSITIONS:
            self.addsegment(position)

    def addsegment(self, position):
        snake_segment = Turtle("square")
        snake_segment.speed("fast")
        snake_segment.color("green")
        snake_segment.up()
        snake_segment.goto(position)
        self.snake_segments.append(snake_segment)

    def extendsegements(self):
        self.addsegment(self.snake_segments[-1].position())

    def move(self):

        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def reset_snake(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.snake_body()
        self.head = self.snake_segments[0]

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