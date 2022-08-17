
import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Rectangle():
    for i in range(4):
        tao.forward(100)
        tao.left(90)

def Faceoof():
    for i in range(3):
        tao.forward(100)
        tao.left(114.4)
        tao.forward(100)
        tao.left(123.6)
        tao.forward(100)
    tao.penup()
    tao.goto(0,-125)
    tao.pendown()
    tao.circle(150)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Faceoof()




# for i in range(10):
#     tao.circle(50)
#     tao.left(36)