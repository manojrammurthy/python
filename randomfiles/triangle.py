import turtle

def draw_tri(me):
    for i in range(1,4):
        me.begin_fill()
        me.forward(80)
        me.left(120)

       
def tri_a():
    window = turtle.Screen()
    window.bgcolor("red")
    me = turtle.Turtle()
    me.color("yellow")
    me.shape("turtle")
    me.color("violet")
    for i in range(1,20):
        draw_tri(me)
        me.right(20)
    #me.ht()
    window.exitonclick()
tri_a()

