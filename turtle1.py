from turtle import *
from random import randint
from tkinter import *

speed(0)
penup()
goto(-140, 140)

for step in range(15):
        write(step, align='center')
        right(90)
        for num in range(8):
            penup()
            forward(10)
            pendown()
            forward(10)
        penup()
        backward(160)
        left(90)
        forward(20)

turtle1 = Turtle()
turtle1.color('red')
turtle1.shape('turtle')

turtle1.penup()
turtle1.goto(-160,100)
turtle1.pendown()

for turn in range(10):
    turtle1.right(36)

turtle2 = Turtle()
turtle2.color('blue')
turtle2.shape('turtle')

turtle2.penup()
turtle2.goto(-160,70)
turtle2.pendown()

for turn in range(72):
    turtle2.left(5)

turtle3 = Turtle()
turtle3.shape('turtle')
turtle3.color('green')

turtle3.penup()
turtle3.goto(-160,40)
turtle3.pendown()

for turn in range(60):
    turtle3.right(6)

turtle4 = Turtle()
turtle4.shape('turtle')
turtle4.color('orange')

turtle4.penup()
turtle4.goto(-160,10)
turtle4.pendown()

for turn in range(30):
    turtle4.left(12)
a=('winner')
goto(0,-100)
write(a)
a1=0
a2=0
a3=0
a4=0
for turn in range(300):
    k=randint(1,5)
    rd=randint(1,5)
    lmn=randint(1,5)
    rm=randint(1,5)
    turtle1.forward(k)
    turtle2.forward(rd)
    turtle3.forward(lmn)
    turtle4.forward(rm)
    a1+=k
    a2+=rd
    a3+=lmn
    a4+=rm
    
    if a1>=300:
        turtle1.goto(0,100)
        break
    elif a2>=300:
        turtle2.goto(0,100)
        break
    elif a3>=300:
        turtle3.goto(0,100)
        break
    elif a4>=300:
        turtle4.goto(0,100)