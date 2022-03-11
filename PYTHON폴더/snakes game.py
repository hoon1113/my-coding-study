#터틀 모듈과 스크린 모듈 불러오기
from turtle import Turtle, Screen
#시간 모듈
import time
#랜덤 모듈
import random

#키 함수
def up():
    #만약 머리방향 270 방향이 아닐때만 머리 방향 90으로 보기 가능 (머리가 밑을 향할때 위를 못봄)
    if snakes[0].heading() != 270:
        snakes[0].setheading(90)
def down():
    #위와 같은원리 (위를 볼때 밑을 못봄)
    if snakes[0].heading() != 90:
        snakes[0].setheading(270)
def right():
    #같은원리
    if snakes[0].heading() != 180:
        snakes[0].setheading(0)
def left():
    #같은원리
    if snakes[0].heading() != 0:
        snakes[0].setheading(180)

#뱀 모양과 색깔
def create_snake(pos):
    snake_body = Turtle()
    snake_body.shape("square")
    snake_body.color("white")
    #지나가는 자리 표시 안되게 함(팬을 들고 이동)
    snake_body.up()
    #이동
    snake_body.goto(pos)
    snakes.append(snake_body)

#먹이 랜덤 함수
def rand_pos():
    rand_x = random.randint(-250,250)
    rand_y = random.randint(-250,250)
    return rand_x, rand_y

#점수 함수
def score_update():
    global score
    score +=1
    score_pen.clear()
    score_pen.write(f"점수 : {score}", font=("", 15, "bold"))

#게임 끝났을때 나오는 글
def game_over():
    score_pen.goto(0,0)
    score_pen.write("Game Over", False, "center", ("", 30, "bold"))

#화면 설정
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("green")
screen.title("Snake Game")
#화면 깜빡임 방지
screen.tracer(0)

#처음 기본 뱀 모양
start_pos = [(0,0),(-20,0),(-40,0)]
#게임을 하면서 바뀔 뱀 모양
snakes = []
#점수초기값
score = 0

#처음 기본뱀 길이 만큼 뱀모양 만들기
for pos in start_pos:
    create_snake(pos)

#먹이
food = Turtle()
food.shape("square")
food.color("snow")
food.up()
food.speed(0)
food.goto(rand_pos())

#점수
score_pen = Turtle()
#모양 숨김
score_pen.ht()
score_pen.up()
score_pen.goto(-270,250)
score_pen.write(f"점수 : {score}", font = ("", 15, "bold")) 

#키 적용
screen.listen()
screen.onkeypress(up,"Up")
screen.onkeypress(down,"Down")
screen.onkeypress(right,"Right")
screen.onkeypress(left,"Left")
#게임 실행
game_on = True
#뱀 움직임
while game_on:
    screen.update()
    time.sleep(0.07)
    #뱀이 움직일때 머리따라 몸이 움직이게 함
    for i in range(len(snakes) -1, 0, -1):
        snakes[i].goto(snakes[i-1].pos())

    #뱀머리 15만큼 움직임
    snakes[0].forward(15)

    #만약 뱀머리가 먹이와의 거리가 15밑일때 점수추가 꼬리하나 늘어남(리스트 하나 추가)
    if snakes[0].distance(food) < 15:
        score_update()

        food.goto(rand_pos())
        create_snake(snakes[-1].pos())
    
    #뱀이 벽에 대였을때 종료
    if snakes[0].xcor() >280 or snakes[0].xcor() < -280 or snakes[0].ycor() >280 or snakes[0].ycor() < -280:
        game_on = False
        game_over()

    #뱀이 머리가아닌 몸에 대였을때 종료
    for body in snakes[1:]:
        if snakes[0].distance(body) < 10:
            game_on = False
            game_over()
#화면 꺼지지않게 방지
screen.mainloop()
