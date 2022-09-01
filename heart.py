import turtle

"""
Draws a heart without using python loops, only the set of operations provided
by the module. 
"""
class HeartTurtle:
    def __init__(self, size, color, startx, starty):
        self.size = size
        self.color = color
        self.pen = turtle.Turtle("turtle",visible=False)
        self.pen.turtlesize(1)
        self.pen.pensize(2)
        self.pen.color("black")

        self.pen.penup()
        self.pen.goto(startx, starty)

    def draw(self):
        self.pen.pendown()
        self.pen.showturtle()

        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.left(45)
        self.pen.forward(self.size)
        self.pen.circle(self.size/2,180)
        self.pen.left(90)
        self.pen.circle(-self.size/2,-180)
        self.pen.left(180)
        self.pen.forward(self.size)
        self.pen.end_fill()
