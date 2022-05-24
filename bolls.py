import turtle,random

bed = turtle.Turtle()
bed.speed(0)
bed.hideturtle()
bed.pensize(10)
bed.color('green')
bed.up()
bed.goto(300,300)
bed.down()
bed.goto(300,-300)
bed.goto(-300,-300)
bed.goto(-300,300)
bed.goto(300,300)

balls = []
count = 5
for i in range(count):
    ball = turtle.Turtle()
    ball.hideturtle()
    ball.shape('circle')

    ball.color('red')
    ball.up()
    randx = random.randint(-290,290)
    randy = random.randint(-290,290)
    red = random.random()
    green = random.random()
    blue = random.random()
    ball.color(red,green,blue)
    ball.goto(randx,randy)
    ball.showturtle()
    dx = random.randint(-5,5)
    dy = random.randint(-5,5)
    balls.append([ball,dx,dy])

while True:
    for i in range(count):
        balls[i]
        x,y = balls[i][0].position()
        if x+balls[i][1] >=300 or x+balls[i][1]<=-300:
            balls[i][1] = -balls[i][1]
        if y+balls[i][2] >=300 or y+balls[i][2]<=-300:
            balls[i][2] = -balls[i][2]

        balls[i][0].goto(x+balls[i][1],y+balls[i][2])
