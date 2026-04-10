import turtle

# 1. Setup the Screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color
screen.title("Python Turtle Polygons")

# 2. Setup the Turtle
t = turtle.Turtle()
t.speed(3)
t.width(3)

# Function to draw any regular polygon
def draw_polygon(sides, length, border_color, fill_color):
    t.color(border_color, fill_color)
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()

# --- Draw Equilateral Triangle ---
t.penup()
t.goto(-200, 0)
t.pendown()
draw_polygon(3, 100, "white", "red")

# --- Draw Rectangle ---
t.penup()
t.goto(-50, 0)
t.pendown()
t.color("white", "blue")
t.begin_fill()
for _ in range(2):
    t.forward(150) # Length
    t.left(90)
    t.forward(80)  # Height
    t.left(90)
t.end_fill()

# --- Draw Hexagon ---
t.penup()
t.goto(150, -50)
t.pendown()
draw_polygon(6, 70, "white", "green")

# Keep the window open
t.hideturtle()
turtle.done()
