import turtle


def draw_square(t1):
    for i in range(4):
        t1.fd(100)
        t1.rt(90)
def draw_triangle(t3):

    for i in range(3):
        t3.fd(200)
        t3.rt(120)

def draw_all():
    window = turtle.Screen()
    window.bgcolor("red")
    t1 = turtle.Turtle()
    t1.color("green")
    t1.shape("turtle")
    t1.speed("slowest")
    draw_square(t1)

    t2 = turtle.Turtle()
    t2.color("yellow")
    t2.shape("classic")
    t2.circle(50)

    t3 = turtle.Turtle()
    t3.color("blue")
    draw_triangle(t3)
    window.exitonclick()
draw_all()

#draw_circle()
#draw_triangle()