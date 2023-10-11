from turtle import *

t = Turtle()

OUTLINE = "black"
DIS = 50
ANG = 30

cO = "orange"
cW = "white"
cR = "red"
cG = "green"
cY = "yellow"
cB = "blue"

topColour = [cO,cW,cW,cR,cY,cG,cW,cO,cB]
leftColour = [cG,cR,cY,cB,cB,cO,cR,cW,cY]
rightColour = [cG,cY,cR,cB,cR,cY,cR,cR,cO]

t.pensize(3)
t.speed(0)

def topSide():
    count = 0
    t.left(ANG)
    for i in range(3):
        for j in range(3):
            makeSQ(topColour[count])
            t.left(ANG*2)
            t.forward(DIS)
            count += 1
            print(count)

        t.left(ANG*4)
        t.forward(DIS)
        t.left(ANG*2)
        t.forward(DIS*3)
        t.left(ANG*6)

def makeSQ(colour):
    c = colour
    t.color(OUTLINE,c)
    t.begin_fill()
    t.forward(DIS)
    t.left(ANG*4)
    t.forward(DIS)
    t.left(ANG*2)
    t.forward(DIS)
    t.left(ANG*4)
    t.forward(DIS)
    t.end_fill()

def leftSide():

    count = 0
    t.right(ANG * 4)
    t.forward(DIS*3)
    t.left(ANG*2)

    for i in range(3):
        for j in range(3):
            makeSQ(leftColour[count])
            t.left(ANG * 2)
            t.forward(DIS)
            count += 1
            print(count)

        t.left(ANG * 4)
        t.forward(DIS)
        t.left(ANG * 2)
        t.forward(DIS * 3)
        t.left(ANG * 6)

def rightSide():

    count = 0
    t.forward(DIS*3)
    t.right(ANG*2)

    for i in range(3):
        for j in range(3):
            makeSQ(rightColour[count])
            t.left(ANG * 2)
            t.forward(DIS)
            count += 1
            print(count)

        t.left(ANG * 4)
        t.forward(DIS)
        t.left(ANG * 2)
        t.forward(DIS * 3)
        t.left(ANG * 6)


topSide()
leftSide()
rightSide()








mainloop()