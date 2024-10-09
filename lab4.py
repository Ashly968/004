import turtle
import random

"""PUT YOUR FUNCTIONS HERE"""

# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""

def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)

# Example usage
#draw_square(t, 100)

def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

# Example usage
#draw_circle(t, 50)

def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    draw_stem(t, x, y, radius)

    # Drawing the stem
def draw_stem(t, x, y, radius):
    t.penup()
    t.goto(x, y + 1.9*radius)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    for _ in range(2):  # Create a simple zigzag mouth
        t.forward(radius // 5)
        t.left(90)
        t.forward(radius // 2)
        t.left(90)
    t.end_fill()

def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y-130)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y-130)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.left(60)
    t.end_fill()

def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y+30)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-250, 250)
        y = random.randint(0, 250)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

def  draw_jack_o_lantern(t, x, y, radius):
    draw_pumpkin(t, x+1, y, radius)
    draw_eye(t, x - .3*radius, y+2.5*radius, .3*radius)  # Left eye
    draw_eye(t, x + .3*radius, y+2.5*radius, .3*radius)  # Right eye
    draw_mouth(t, x - .3*radius, y+2.1*radius, .8*radius)  # Mouth

# Draw three jack-o-lanterns
draw_jack_o_lantern(t, -150, -280, 100)
draw_jack_o_lantern(t, 0, -280, 80)
draw_jack_o_lantern(t, 150, -280, 100)



# Draw the night sky
draw_sky(t, 30)

# Close the turtle graphics window when clicked
turtle.exitonclick()