from turtle import Turtle, Screen
import turtle



screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) # Turn off screen updates for smoother animation

pen = turtle.Turtle()
pen.speed(0) # Fastest speed
pen.color("white")
pen.penup()
pen.goto(0, -100) # Start position below center for drawing circles
pen.pendown()
radius = 10
max_radius = 150
min_radius = 10
increasing = True # Flag to control growth direction
animation_speed = 5 # Adjust for animation speed (lower is faster)
def animate_circle():
    global radius, increasing

    pen.clear() # Clear previous drawing
    pen.circle(radius)

    if increasing:
        radius += 1
        if radius >= max_radius:
            increasing = False
    else:
        radius -= 1
        if radius <= min_radius:
            increasing = True

    screen.update() # Update the screen to show the new circle
    screen.ontimer(animate_circle, animation_speed) # Schedule next frame

animate_circle()
screen.mainloop() # Keep the window open until manually closed
screen.exitonclick()




