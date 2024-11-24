import turtle

drawing_board = turtle.Screen()
drawing_board.title("Drawing Board")
drawing_board.bgcolor("light blue")
turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def turtle_right():
    turtle_instance.setheading(turtle_instance.heading() -10)

def turtle_left():
    turtle_instance.setheading(turtle_instance.heading() +10)

def turtle_penup():
    turtle_instance.penup()

def turtle_pendown():
    turtle_instance.pendown()

def turtle_return_home():
    turtle_penup()
    turtle_instance.home()
    turtle_pendown()

def board_clean():
    turtle_instance.clear()

drawing_board.listen()
drawing_board.onkey(turtle_forward, "space")
drawing_board.onkey(turtle_left, "Up")
drawing_board.onkey(turtle_right, "Down")
drawing_board.onkey(turtle_return_home, "h")
drawing_board.onkey(board_clean, "c")
drawing_board.onkey(turtle_pendown, "w")
drawing_board.onkey(turtle_penup, "q")


turtle.done()