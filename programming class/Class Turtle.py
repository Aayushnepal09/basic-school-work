# importing turtle
"""import turtle
screen=turtle.Screen()"""
'''or'''
'''from turtle import *
screen=Screen()
'''

from turtle import *

screen = Screen()
pen = Turtle()
pen.speed(2)
pen.begin_fill()
pen.width(0)
pen.shape('turtle')
pen.fillcolor('red')
pen.color('blue')
bgcolor('red')
'''pen.forward(200)    #random
pen.left(25)
pen.backward(200)
pen.right(50)'''
for i in range(5):  # star
    pen.forward(300)
    pen.left(144)
pen.end_fill()
# done
screen.exitonclick()
