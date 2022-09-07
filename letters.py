import turtle
from util import hypotenuse

# CONSTANTS OF LENGTH 
H = 70
W = 30
SPACE = 10

DIAG_B = (hypotenuse(W/3, H/7))/2
DIAG_AG = hypotenuse(W/3,H*(6/7))
DIAG_AL = hypotenuse(W*(1/6),H*(2/7))
DIAG_M = DIAG_AL
DIAG_N = hypotenuse(W/3,H*(4/7))
DIAG_Ñ = hypotenuse(W/3,H*(3/7))
DIAG_R = hypotenuse(W/3, H/7)
DIAG_Z = hypotenuse(W*(2/3),H*(5/7))

# CONSTANTS OF COLOR
PRIMARY = 'black'
WHITE = 'white'

# MOVEMENTS
LETTERS = {
        'A': [( 90, H/7,     PRIMARY), (-10, DIAG_AG, PRIMARY), (-80, W/3,     PRIMARY),
              (-80, DIAG_AG, PRIMARY), (-10, H/7,     PRIMARY), (-90, W/3,     PRIMARY),
              (-90, H*(2/7), PRIMARY), (  0, H/7,     WHITE  ), ( 14, DIAG_AL, PRIMARY),
              (152, DIAG_AL, PRIMARY), (104, W/3,     PRIMARY), (-90, H/7,     WHITE  ),
              (-90, W/3,     PRIMARY), ( 90, H*(2/7), PRIMARY), (-90, W/3,     PRIMARY),
        ],
        'B': [( 90, H,        PRIMARY), (-90, W*(2/3), PRIMARY), (-45, DIAG_R,  PRIMARY),
              (-45, H*(2/7),  PRIMARY), (-90, W*(2/3), PRIMARY), (-90, H*(2/7), PRIMARY),
              (-90, W/3,      PRIMARY), (-90, H*(2/7), PRIMARY), ( 90, W/3,     WHITE  ), 
              (-135, DIAG_B,  PRIMARY), ( 90, DIAG_B,  PRIMARY), (-45, H*(2/7), PRIMARY),
              (-90, W*(2/3),  PRIMARY), (-90, H*(2/7), PRIMARY), (-90, W/3,     PRIMARY), 
              (-90, H*(2/7),  PRIMARY), ( 90, W/3,     WHITE  ), (-135, DIAG_R, PRIMARY), 
              (-45, W*(2/3),  PRIMARY), 
        ],
        'C': [( 90, H,       PRIMARY), (-90, W,       PRIMARY), (-90, H/7,     PRIMARY), 
              (-90, W*(2/3), PRIMARY), ( 90, H*(5/7), PRIMARY), ( 90, W*(2/3), PRIMARY),
              (-90, H/7,     PRIMARY), (-90, W,       PRIMARY),
        ],
        'D': [( 90, H,        PRIMARY), (-90, W*(2/3), PRIMARY), (-45, DIAG_R,  PRIMARY),
              (-45, H*(5/7),  PRIMARY), (-90, W*(2/3), PRIMARY), (-90, H*(5/7), PRIMARY),
              (-90, W/3,      PRIMARY), (-90, H*(5/7), PRIMARY), ( 90, W/3,     WHITE  ), 
              (-135, DIAG_R,  PRIMARY), (-45, W*(2/3), PRIMARY),
        ],
        'E': [( 90, H,       PRIMARY), (-90, W,       PRIMARY), (-90, H/7,     PRIMARY), 
              (-90, W*(2/3), PRIMARY), ( 90, H*(2/7), PRIMARY), ( 90, W/3,     PRIMARY),
              (-90, H/7,     PRIMARY), (-90, W/3,     PRIMARY), ( 90, H*(2/7), PRIMARY),
              ( 90, W*(2/3), PRIMARY), (-90, H/7,     PRIMARY), (-90, W,       PRIMARY),
        ],
        'F': [( 90, H,       PRIMARY), (-90, W,       PRIMARY), (-90, H/7,     PRIMARY), 
              (-90, W*(2/3), PRIMARY), ( 90, H*(2/7), PRIMARY), ( 90, W/3,     PRIMARY),
              (-90, H/7,     PRIMARY), (-90, W/3,     PRIMARY), ( 90, H*(3/7), PRIMARY),
              (-90, W/3,     PRIMARY),
        ],
        'G': [( 90, H,       PRIMARY), (-90, W,       PRIMARY), (-90, H/7,     PRIMARY), 
              (-90, W*(2/3), PRIMARY), ( 90, H*(5/7), PRIMARY), ( 90, W/3,     PRIMARY),
              ( 90, H*(2/7), PRIMARY), ( 90, W/6,     PRIMARY), (-90, H/7,     PRIMARY),
              (-90, W/2,     PRIMARY), (-90, H*(4/7), PRIMARY), (-90, W,       PRIMARY),
        ],
        'H': [( 90, H,       PRIMARY), (-90, W/3,     PRIMARY), (-90, H*(3/7), PRIMARY), 
              ( 90, W/3,     PRIMARY), ( 90, H*(3/7), PRIMARY), (-90, W/3,     PRIMARY),
              (-90, H,       PRIMARY), (-90, W/3,     PRIMARY), (-90, H*(3/7), PRIMARY),
              ( 90, W/3,     PRIMARY), ( 90, H*(3/7), PRIMARY), (-90, W/3,     PRIMARY),
        ],
        'I': [( 90, H*(1/7), PRIMARY), (-90, W/3,     PRIMARY), ( 90, H*(5/7), PRIMARY),
              ( 90, W/3,     PRIMARY), (-90, H*(1/7), PRIMARY), (-90, W,       PRIMARY),
              (-90, H*(1/7), PRIMARY), (-90, W/3,     PRIMARY), ( 90, H*(5/7), PRIMARY),
              ( 90, W/3,     PRIMARY), (-90, H*(1/7), PRIMARY), (-90, W,       PRIMARY),
        ],
        'J': [( 90, H/14,    WHITE  ), (  0, H*(3/14), PRIMARY), (-90, W/3,     PRIMARY),
              (-90, H/7,     PRIMARY), ( 90, W/3,      PRIMARY), ( 90, H*(5/7), PRIMARY),
              ( 90, W/3,     PRIMARY), (-90, H/7,      PRIMARY), (-90, W*(2/3), PRIMARY),
              (-90, H*(6/7), PRIMARY), (-45, DIAG_R,   PRIMARY), (-45, W/2,     PRIMARY),
              (-45, DIAG_B,  PRIMARY),
        ],
        'K': [],
        'L': [( 90, H,       PRIMARY), (-90, W/3,     PRIMARY), (-90, H*(6/7), PRIMARY),
              ( 90, W*(2/3), PRIMARY), (-90, H/7,     PRIMARY), (-90, W,       PRIMARY),
        ],
        'M': [(  90, H,      PRIMARY), (-90, W/3,     PRIMARY), (-76, DIAG_M, PRIMARY),
              ( 152, DIAG_M, PRIMARY), (-76, W/3,     PRIMARY), (-90, H,      PRIMARY),
              ( -90, W/3,    PRIMARY), (-90, H*(4/7), PRIMARY), (166, DIAG_M, PRIMARY),
              (-152, DIAG_M, PRIMARY), (166, H*(4/7), PRIMARY), (-90, W/3,    PRIMARY),
        ],
        'N': [( 90, H,       PRIMARY), (-90, W/3,    PRIMARY), (-76, DIAG_N,  PRIMARY),
              (166, H*(4/7), PRIMARY), (-90, W/3,    PRIMARY), (-90, H,       PRIMARY),
              (-90, W/3,     PRIMARY), (-76, DIAG_N, PRIMARY), (166, H*(4/7), PRIMARY),
              (-90, W/3,     PRIMARY),
        ],
        'Ñ': [(    90, H*(6/7),  PRIMARY), (   -90, W/3,      PRIMARY),
              (-71.56, DIAG_Ñ,   PRIMARY), (161.56, H*(3/7),  PRIMARY), 
              (   -90, W/3,      PRIMARY), (    90, H*(1/16), WHITE  ),
              (    90, W,        PRIMARY), (   -90, H*(1/16), PRIMARY),
              (   -90, W,        PRIMARY), (   -90, H*(1/16), PRIMARY),
              (     0, H*(1/16), WHITE  ), (     0, H*(6/7),  PRIMARY),
              (   -90, W/3,      PRIMARY), (-71.56, DIAG_Ñ,   PRIMARY),
              (161.56, H*(3/7),  PRIMARY), (   -90, W/3,      PRIMARY),
        ],
        'O': [( 90, H,       PRIMARY), (-90, W/3,     PRIMARY), (-90, H/7,     WHITE  ), 
              (  0, H*(5/7), PRIMARY), ( 90, W/3,     PRIMARY), ( 90, H*(5/7), PRIMARY),
              ( 90, W/3,     PRIMARY), (-90, H/7,     WHITE  ), (-90, W*(2/3), PRIMARY),
              (-90, H,       PRIMARY), (-90, W,       PRIMARY),
        ],
        'P': [( 90, H,       PRIMARY), (-90, W*(2/3), PRIMARY), (-45, DIAG_R,  PRIMARY),
              (-45, H*(2/7), PRIMARY), (-45, DIAG_R,  PRIMARY), (-45, W/3,     PRIMARY),
              (-90, H/7,     WHITE  ), (  0, H*(2/7), PRIMARY),
              (-90, W/3,     PRIMARY), (-90, H*(2/7), PRIMARY), (-90, W/3,     PRIMARY),
              ( 90, H/7,     WHITE  ), (  0, H*(3/7), PRIMARY), (-90, W/3,     PRIMARY),
        ],
        'Q': [],
        'R': [( 90, H,       PRIMARY), (-90, W*(2/3), PRIMARY), (-45, DIAG_R,  PRIMARY),
              (-45, H*(2/7), PRIMARY), (-45, DIAG_R,  PRIMARY), ( 90, DIAG_R,  PRIMARY),
              (-45, H*(2/7), PRIMARY), (-90, W/3,     PRIMARY), (-90, H*(2/7), PRIMARY),  
              ( 45, DIAG_R,  PRIMARY), (-45, H/7,     WHITE  ), (  0, H*(2/7), PRIMARY),
              (-90, W/3,     PRIMARY), (-90, H*(2/7), PRIMARY), (-90, W/3,     PRIMARY),
              ( 90, H/7,     WHITE  ), (  0, H*(3/7), PRIMARY), (-90, W/3,     PRIMARY),
        ],
        'S': [( 90, H*(1/7), PRIMARY), (-90, W*(2/3), PRIMARY), ( 90, H*(2/7), PRIMARY),
              ( 90, W*(2/3), PRIMARY), (-90, H*(4/7), PRIMARY), (-90, W,       PRIMARY),
              (-90, H*(1/7), PRIMARY), (-90, W*(2/3), PRIMARY), ( 90, H*(2/7), PRIMARY),
              ( 90, W*(2/3), PRIMARY), (-90, H*(4/7), PRIMARY), (-90, W,       PRIMARY),
        ],
        'T': [],
        'U': [( 90, H,   PRIMARY), (-90, W/3,     PRIMARY), (-90, H*(6/7), PRIMARY),
              ( 90, W/3, PRIMARY), ( 90, H*(6/7), PRIMARY), (-90, W/3,     PRIMARY),
              (-90, H,   PRIMARY), (-90, W,       PRIMARY),
        ],
        'V': [],
        'W': [],
        'X': [],
        'Y': [],
        'Z': [( 90, H*(1/7), PRIMARY), (-22, DIAG_Z,     PRIMARY), (112, W*(2/3), PRIMARY),
              (-90, H/7,     PRIMARY), (-90, W,          PRIMARY), (-90, H/7,     PRIMARY),
              (-22, DIAG_Z,  PRIMARY), (112, W*(2/3),    PRIMARY), (-90, H/7,     PRIMARY),
              (-90, W,       PRIMARY),
        ],
}
                
class Letter:
    def __init__(self, letter, x, y):
        self.x = x
        self.y = y
        self.moves: list[tuple] = LETTERS[letter]


        self.pen = turtle.Turtle("turtle",visible=False)
        self.pen.penup()
        self.pen.goto(self.x, self.y)

    def draw(self):
        self.pen.pendown()
        self.pen.showturtle()

        for direction, amount, color in self.moves:
            self.pen.pencolor(color)
            self.pen.left(direction)
            self.pen.forward(amount)
        
        self.pen.right(180)
        self.pen.hideturtle()


if __name__ == '__main__':
    ws = turtle.Screen()
    ws.setup(1000,650, startx= 1700, starty= 200)
    test = Letter('J',-400, 200)
    test.draw()
    turtle.exitonclick()

