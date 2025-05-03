from turtle import Turtle

FONT = ('Courier', 16, "normal")
ALIGN = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore= int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 375)
        self.writescore()

    def writescore(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as update_txt:
                update_txt.write(f"{self.score}")
            self.highscore = self.score

        self.score = 0
        self.writescore()

    def increasecore(self):
        self.score += 1
        self.writescore()

    def game_continue(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=("Courier", 20, "bold"))
        self.goto(0, -20)
        self.write("Continue? Y/N", align=ALIGN, font=("Courier", 20, "bold"))
        self.goto(0, 375)
