from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.find_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)

    def add_score(self):
        self.clear()
        self.score += 1

    def show_score(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.show_score()

    def find_high_score(self):
        with open("data.txt", mode="r") as file:
            return int(file.read())

    def save_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
