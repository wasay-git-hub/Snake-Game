from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.place_food()

    def place_food(self):
        rand1 = random.randint(-270, 270)
        rand2 = random.randint(-270, 270)
        self.teleport(rand1, rand2)