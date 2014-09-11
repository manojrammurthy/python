import turtle

def draw_square(some_turtle):
    #range gives values 1,2,3,4(last 5 will be truncated)
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad=turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #angie = turtle.Turtle()
    #angie.shape("circle")
    #angie.color("blue")
    #angie.circle(100)
    window.exitonclick()
    
draw_art()