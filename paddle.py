# from turtle import Turtle
#
# STARTING_POSITIONS_USER = [(350, 20), (350, 0), (350, -20)]
# STARTING_POSITIONS_COMP = [(-400, 20), (-400, 0), (-400, -20)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
#
#
# class Paddle:
#
#     def __init__(self):
#         self.user_paddle_segments = []
#         self.comp_paddle_segments = []
#         self.create_paddle_user()
#         self.create_paddle_comp()
#         self.user_head = self.user_paddle_segments[0]
#         self.user_tail = self.user_paddle_segments[-1]
#         self.comp_head = self.comp_paddle_segments[0]
#         self.comp_tail = self.comp_paddle_segments[-1]
#
#
#     def create_paddle_user(self):
#         for position in STARTING_POSITIONS_USER:
#             paddle_seg = Turtle("square")
#             paddle_seg.penup()
#             paddle_seg.color("white")
#             paddle_seg.goto(position)
#             self.user_paddle_segments.append(paddle_seg)
#
#     def create_paddle_comp(self):
#         for position in STARTING_POSITIONS_COMP:
#             paddle_seg = Turtle("square")
#             paddle_seg.penup()
#             paddle_seg.color("white")
#             paddle_seg.goto(position)
#             self.comp_paddle_segments.append(paddle_seg)
#
#     def move_user(self):
#         for seg_num in range(len(self.user_paddle_segments) - 1, 0, -1):
#             new_x = self.user_paddle_segments[seg_num - 1].xcor()
#             new_y = self.user_paddle_segments[seg_num - 1].ycor()
#             self.user_paddle_segments[seg_num].goto(new_x, new_y)
#         self.user_head.forward(MOVE_DISTANCE)
#
#     def move_user_down(self):
#         for seg_num in range(len(self.user_paddle_segments) - 1, 0, -1):
#             new_x = self.user_paddle_segments[seg_num - 1].xcor()
#             new_y = self.user_paddle_segments[seg_num - 1].ycor()
#             self.user_paddle_segments[seg_num].goto(new_x, new_y)
#         self.user_head.forward(MOVE_DISTANCE)
#
#     def up(self):
#         self.user_head.setheading(UP)
#
#     def down(self):
#         self.user_head.setheading(DOWN)


from turtle import Turtle
MOVE_DISTANCE = 40


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
