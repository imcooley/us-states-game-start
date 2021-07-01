import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

state_file = pandas.read_csv("50_states.csv")
all_states = state_file.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = state_file[state_file.state == answer_state]
        writer.goto(int(state_data.x), int(state_data.y))
        # Another way to write the state
        #writer.write(state_data.state.item())
        writer.write(answer_state)

