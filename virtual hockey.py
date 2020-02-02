'''Player A controls: w/s
   Player B controls: Up/down
   Game over once scored 10 points. '''

import turtle

wn = turtle.Screen()
wn.title("Virtual Hockey(ninja)")

wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350,-270)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350,270)



#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

#Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align='center',font=('Courier',28,'normal'))


#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')


while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ ball.dy)


    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1   
    if ball.xcor() > 370:
        ball.goto(0,0)
        score_a += 1 
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align='center',font=('Courier',28,'normal'))
        ball.dx *= -1 ** 0.9
    if ball.xcor() < -370:
        ball.goto(0,0)
        score_b += 1 
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align='center',font=('Courier',28,'normal'))
        ball.dx *= -1 ** 0.9
    if score_a >= 10 or score_b >= 10:
        style = ('Verdana',40,'bold')
    #     style1 = ('Arial',20,'italic')
        turtle.color('White')
    #     # turtle.write('Player A : '+str(score_a)+' | '+'Player B : '+str(score_b),font=style1)
        turtle.write('GAME OVER!', font=style, align='center')
        turtle.penup()
        wn.delay(5000)
        wn.bye()
        
        
        score_a = 0
        score_b = 0
    if paddle_a.ycor() > 245:
        paddle_a.sety(245)
    if paddle_a.ycor() < -245:
        paddle_a.sety(-245)        
    if paddle_b.ycor() > 245:
        paddle_b.sety(245)
    if paddle_b.ycor() < -245:
        paddle_b.sety(-245)   

    #collision
    if (ball.xcor() > 340 and ball.xcor() < 345) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor() -40): 
        ball.setx(340)
        ball.dx *= - 1   
    if (ball.xcor() < -340 and ball.xcor() < -345) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor() -40): 
        ball.setx(-340)
        ball.dx *= - 1   
    # print("score_a: {} | score_b: {}".format(score_a,score_b))    