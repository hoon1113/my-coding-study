from turtle import Turtle, Screen
import random
import time

#기본 테트리스 조각 모양
def peace(pos):
    p_body = Turtle()
    p_body.shape("square")
    p_body.color("white")
    p_body.up()
    p_body.goto(pos)
    p_body.append(p_body)

screen = Screen()
screen.setup(600,800)
screen.bgcolor("black")
screen.title("테트리스")
screen.tracer(0)
peace()
screen.mainloop()