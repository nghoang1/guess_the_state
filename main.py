from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)


correct = 0
while correct < 50:
    answer_state = screen.textinput(title=f"{correct}/50 States Correct", prompt="What is another state?").title()
    print(answer_state)
    states = pandas.read_csv("50_states.csv")
    all_states = states["state"].to_list()
    if answer_state in all_states:
        correct +=1
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()