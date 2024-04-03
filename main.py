import turtle

import pandas
from turtle import Turtle,Screen

screen = Screen()

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

turtle = Turtle()
turtle.hideturtle()
data = pandas.read_csv("50_states.csv")

for _ in range(len(data)):
    user_state_name = screen.textinput("US States", "Enter the name of State:")
    if user_state_name in data.values:
        new_state = data[data.state == user_state_name]

        new_x = new_state.x.item()
        new_y = new_state.y.item()


        turtle.penup()

        turtle.goto(x=new_x,y=new_y)
        turtle.write(user_state_name,font=("Arial", 8, "bold"))
    else:
        continue
screen.mainloop()
screen.exitonclick()