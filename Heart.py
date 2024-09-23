import turtle

def draw_heart(turtle, size, color):
    turtle.begin_fill()
    turtle.color(color)
    turtle.left(140)
    turtle.forward(size)

    turtle.circle(-size // 2, 200)

    turtle.left(120)
    turtle.circle(-size // 2, 200)

    turtle.forward(size)
    turtle.end_fill()
    turtle.setheading(0)

def draw_hearts():
    turtle.bgcolor('lightgreen')
    turtle.speed(3)
    turtle.width(3)

    sizes = [300, 250, 200, 150, 100]
    colors = ['#3A8812', '#94DF6C', '#508F2F','#ABEB8A', '#3A8812']
    for size, color in zip(sizes, colors):
        turtle.penup()
        turtle.goto(0, -size// 2)
        turtle.pendown()
        draw_heart(turtle, size, color)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.write('I love you kathyy!!', align = 'center', font = ('Weddingday Font', 20, 'normal'))
    turtle.done()

draw_hearts()