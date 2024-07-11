import turtle
import random

def draw_star(turtle, size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

def draw_circle_pattern(turtle, radius):
    for _ in range(36):
        turtle.circle(radius)
        turtle.right(10)

def draw_spiral(turtle):
    colors = ["red", "yellow", "blue", "green", "purple", "orange", "pink", "cyan"]
    turtle.speed(0)
    turtle.width(2)
    for i in range(50):
        turtle.color(random.choice(colors))
        turtle.forward(i * 10)
        turtle.right(144)

def draw_combined_pattern():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(100000)  # Fastest drawing speed

    colors = ["red", "yellow", "blue", "green", "purple", "orange", "pink", "cyan"]
    
    # Draw multiple stars with different sizes and colors
    for _ in range(12):
        t.color(random.choice(colors))
        t.penup()
        t.goto(random.randint(-300, 300), random.randint(-300, 300))
        t.pendown()
        draw_star(t, random.randint(20, 100))

    # Draw multiple circle patterns
    for _ in range(6):
        t.color(random.choice(colors))
        t.penup()
        t.goto(random.randint(-300, 300), random.randint(-300, 300))
        t.pendown()
        draw_circle_pattern(t, random.randint(30, 60))

    # Draw a spiral in the center
    t.penup()
    t.goto(0, 0)
    t.pendown()
    draw_spiral(t)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_combined_pattern()
