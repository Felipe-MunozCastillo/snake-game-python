from turtle import Turtle
import random


class Food(Turtle):
    """Clase para la creacion de la fruta que se comera
    la serpiente."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Metodo para aparicion aleatoria de la fruta."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
