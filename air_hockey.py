# This will create a game of air hockey using python.

import turtle
# Style of window
window= turtle.Screen()
window.title("Air Hockey by Tiara")
window.bgcolor("white")
window.setup(height=600, width=800)
window.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("circle")
paddle_a.shapesize(5,5,10)
paddle_a.color("red")
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("circle")
paddle_b.shapesize(5,5,10)
paddle_b.color("blue")
paddle_b.penup()
paddle_b.goto(350,0)


#Paddle A funtion
def paddle_a_up():
   y = paddle_a.ycor()
   y+=20
   paddle_a.sety(y)

def paddle_a_down():
   y = paddle_a.ycor()
   y-=20
   paddle_a.sety(y)

#Paddle B funtion
def paddle_b_up():
   y = paddle_b.ycor()
   y+=20
   paddle_b.sety(y)

def paddle_b_down():
   y = paddle_b.ycor()
   y-=20
   paddle_b.sety(y)

#Keyboard input for Paddle A
window.listen()
window.onkeypress(paddle_a_up,"w")

window.listen()
window.onkeypress(paddle_a_down,"s")

#Keyboard input for Paddle B
window.listen()
window.onkeypress(paddle_b_up,"Up")

window.listen()
window.onkeypress(paddle_b_down,"Down")


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(2,2,4.5)
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx = .2
ball.dy = -.2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Red Team: 0          Blue Team : 0 ", align="center", font = ("Courier", 20, "bold"))

#Main Game loop
while True:
   window.update()

#move ball
   ball.setx(ball.xcor()+ ball.dx)
   ball.sety(ball.ycor()+ ball.dy)

#border checking
   if ball.ycor() > 290:
      ball.sety(290)
      ball.dy *= -1

   if ball.ycor() < -290:
      ball.sety(-290)
      ball.dy *= -1

   if ball.xcor() > 390:
      ball.goto(0,0)
      ball.dx *= -1  
      score_a +=1
      pen.clear()
      pen.write("Red Team:{}          Blue Team:{} " .format(score_a, score_b), align="center", font = ("Courier", 20, "bold"))


   if ball.xcor() < -390:
      ball.goto(0,0)
      ball.dx *= -1  
      score_b +=1
      pen.clear()
      pen.write("Red Team:{}          Blue Team:{} " .format(score_a, score_b), align="center", font = ("Courier", 20, "bold"))


#collision
   if (ball.xcor() > 280 and ball.xcor() < 290) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50 ):
      ball.setx(280)
      ball.dx *= -1

   if (ball.xcor() < -280 and ball.xcor() > -290) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50 ):
      ball.setx(-280)
      ball.dx *= -1
