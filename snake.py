from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
WIDTH = 600
HEIGHT = 600


class Snake:
    def __init__(self):
        self.segments = []

        self.create_snake()

        self.head = self.segments[0]
        self.head.color('CadetBlue')

        self.current_direction = RIGHT
        self.direction_changed = False

    def create_snake(self) -> None:
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos: tuple) -> None:
        new_seg = Turtle('square')
        new_seg.color('SpringGreen')
        new_seg.pu()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def grow(self) -> None:
        self.add_segment(self.segments[-1].position())

    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DIST)
        self.direction_changed = False

    def reset(self) -> None:
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color('CadetBlue')

    def update_direction(self, new_direction: int) -> None:
        # Update the current direction only if it's not the opposite direction
        if (new_direction != self.current_direction and
                new_direction != (self.current_direction + 180) % 360):
            self.current_direction = new_direction
            self.head.setheading(self.current_direction)
            self.direction_changed = True

    def up(self) -> None:
        if not self.direction_changed:
            self.update_direction(UP)

    def down(self) -> None:
        if not self.direction_changed:
            self.update_direction(DOWN)

    def left(self) -> None:
        if not self.direction_changed:
            self.update_direction(LEFT)

    def right(self) -> None:
        if not self.direction_changed:
            self.update_direction(RIGHT)
