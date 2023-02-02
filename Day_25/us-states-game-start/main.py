import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
answer_states = []

num_of_correct = 0


def among_50_states(guess):
    if guess in all_states:
        return True
    else:
        return False


def write_map(state_name):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    the_state = data[data.state == state_name]
    t.goto(int(the_state.x), int(the_state.y))
    t.write(state_name)


while num_of_correct < 50:
    answer_state = screen.textinput(title=f"{num_of_correct}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        print(answer_states)
        df = pandas.DataFrame(answer_states)
        print(df)
        df.to_csv("learn.csv")
        break
    if among_50_states(answer_state):
        answer_states.append(answer_state)
        write_map(answer_state)
        num_of_correct += 1


