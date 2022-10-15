from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 280
RIGHT = 0

class Snake:

    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        # make 3 new turtles with a square shape
        for snake_index in STARTING_POSITIONS:
            self.add_segment(snake_index)

    def add_segment(self, snake_index):
        # Create a snake
        snaky = Turtle(shape="square")
        snaky.color("white")
        snaky.penup()
        snaky.goto(snake_index)
        self.all_snakes.append(snaky)

    def reset(self):
        for segment in self.all_snakes:
            segment.goto(1000, 1000)
        self.all_snakes.clear()
        self.create_snake()
        self.head = self.all_snakes[0]

    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.all_snakes[-1].position())

    def move(self):
        for snaky_seg in range(len(self.all_snakes) - 1, 0, -1):
            # here we get hold of the second to last snake segment's x and y coordinates
            new_x = self.all_snakes[snaky_seg - 1].xcor()
            new_y = self.all_snakes[snaky_seg - 1].ycor()
            # then we move the last snake segment to the second last snake segment's position
            self.all_snakes[snaky_seg].goto(new_x, new_y)
        # then we move the first snake segment forward
        self.head.fd(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
