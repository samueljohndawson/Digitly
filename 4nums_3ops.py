import tkinter
from tkinter import *
import random
import operator
import datetime as dt

# Generate the answer
ops = ['+', '-', 'x']
nums = [1, 2, 3, 4]

ops_dict = {
    '+': operator.add,
    '-': operator.sub,
    'x': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
}

# Shuffle the operators and numbers
random.shuffle(ops)
random.shuffle(nums)

ans = nums[0]
for i in range(len(nums)-1):
    ans = ops_dict[ops[i]](ans, nums[i+1])

# Create empty user number and ops list
user_nums = []
user_ops = []

disabled_colour = '#212121'
normal_colour = '#6aaa64'
num_op_font = "Helvetica 30 bold"
slot_font_colour = 'white'
slot_background = '#787c7e'
slot_width = 2
slot_border_width = 0
button_border_width = 0
button_curser = 'hand2'


# Functions
def check_ans():
    global user_nums, user_ops, user_answer_widget, result_widget


    # Reset buttons
    num1['state'] = tkinter.NORMAL
    num2['state'] = tkinter.NORMAL
    num3['state'] = tkinter.NORMAL
    num4['state'] = tkinter.NORMAL
    op1['state'] = tkinter.NORMAL
    op2['state'] = tkinter.NORMAL
    op3['state'] = tkinter.NORMAL

    if len(user_nums) == 4 and len(user_ops) == 3:
        user_ans = user_nums[0]
        for i in range(len(user_nums) - 1):
            user_ans = ops_dict[user_ops[i]](user_ans, user_nums[i+1])

        if user_ans == ans:
            result = 'You Win!'
            stop_timer()
        else:
            result = 'Guess again'

    else:
        result = "Invalid input"

    result_widget.destroy()
    result_widget = Label(frame, text=result, font="Helvetica 18 bold", bg='white')
    result_widget.grid(row=6, columnspan=7)

    user_nums = []
    user_ops = []

    reset_answer_board()
    reset_buttons()


def reset_answer_board():
    slot1['text'] = ''
    slot2['text'] = ''
    slot3['text'] = ''
    slot4['text'] = ''
    slot5['text'] = ''
    slot6['text'] = ''
    slot7['text'] = ''
    slot1['bg'] = slot_background
    slot2['bg'] = slot_background
    slot3['bg'] = slot_background
    slot4['bg'] = slot_background
    slot5['bg'] = slot_background
    slot6['bg'] = slot_background
    slot7['bg'] = slot_background
    slot1['disabledforeground'] = slot_font_colour
    slot2['disabledforeground'] = slot_font_colour
    slot3['disabledforeground'] = slot_font_colour
    slot4['disabledforeground'] = slot_font_colour
    slot5['disabledforeground'] = slot_font_colour
    slot6['disabledforeground'] = slot_font_colour
    slot7['disabledforeground'] = slot_font_colour


def reset_buttons():
    num1['state'] = NORMAL
    num1['bg'] = normal_colour

    num2['state'] = NORMAL
    num2['bg'] = normal_colour

    num3['state'] = NORMAL
    num3['bg'] = normal_colour

    num4['state'] = NORMAL
    num4['bg'] = normal_colour

    op1['state'] = DISABLED
    op1['bg'] = disabled_colour

    op2['state'] = DISABLED
    op2['bg'] = disabled_colour

    op3['state'] = DISABLED
    op3['bg'] = disabled_colour


def update_answer_board(num_op):
    if type(num_op) is int:
        if len(user_nums) == 1:
            slot1['text'] = num_op
        elif len(user_nums) == 2:
            slot3['text'] = num_op
        elif len(user_nums) == 3:
            slot5['text'] = num_op
        elif len(user_nums) == 4:
            slot7['text'] = num_op
    else:
        if len(user_ops) == 1:
            slot2['text'] = num_op
        elif len(user_nums) == 2:
            slot4['text'] = num_op
        elif len(user_nums) == 3:
            slot6['text'] = num_op


def switch_buttons():

    if num1['state'] == NORMAL:
        num1['state'] = DISABLED
        num1['bg'] = disabled_colour
    else:
        num1['state'] = NORMAL
        num1['bg'] = normal_colour

    if num2['state'] == NORMAL:
        num2['state'] = DISABLED
        num2['bg'] = disabled_colour
    else:
        num2['state'] = NORMAL
        num2['bg'] = normal_colour

    if num3['state'] == NORMAL:
        num3['state'] = DISABLED
        num3['bg'] = disabled_colour
    else:
        num3['state'] = NORMAL
        num3['bg'] = normal_colour

    if num4['state'] == NORMAL:
        num4['state'] = DISABLED
        num4['bg'] = disabled_colour
    else:
        num4['state'] = NORMAL
        num4['bg'] = normal_colour

    if op1['state'] == NORMAL:
        op1['state'] = DISABLED
        op1['bg'] = disabled_colour
    else:
        op1['state'] = NORMAL
        op1['bg'] = normal_colour


    if op2['state'] == NORMAL:
        op2['state'] = DISABLED
        op2['bg'] = disabled_colour
    else:
        op2['state'] = NORMAL
        op2['bg'] = normal_colour

    if op3['state'] == NORMAL:
        op3['state'] = DISABLED
        op3['bg'] = disabled_colour
    else:
        op3['state'] = NORMAL
        op3['bg'] = normal_colour

    # Check if buttons have already been clicked
    if 1 in user_nums:
        num1['state'] = DISABLED
        num1['bg'] = disabled_colour

    if 2 in user_nums:
        num2['state'] = DISABLED
        num2['bg'] = disabled_colour

    if 3 in user_nums:
        num3['state'] = DISABLED
        num3['bg'] = disabled_colour

    if 4 in user_nums:
        num4['state'] = DISABLED
        num4['bg'] = disabled_colour

    if '+' in user_ops:
        op1['state'] = DISABLED
        op1['bg'] = disabled_colour

    if '-' in user_ops:
        op2['state'] = DISABLED
        op2['bg'] = disabled_colour

    if 'x' in user_ops:
        op3['state'] = DISABLED
        op3['bg'] = disabled_colour



def click_one():
    user_nums.append(1)
    switch_buttons()
    update_answer_board(1)


def click_two():
    user_nums.append(2)
    switch_buttons()
    update_answer_board(2)


def click_three():
    user_nums.append(3)
    switch_buttons()
    update_answer_board(3)


def click_four():
    user_nums.append(4)
    switch_buttons()
    update_answer_board(4)


def click_add():
    user_ops.append('+')
    switch_buttons()
    update_answer_board('+')


def click_minus():
    user_ops.append('-')
    switch_buttons()
    update_answer_board('-')


def click_times():
    user_ops.append('x')
    switch_buttons()
    update_answer_board('x')


# TIMER FUNCTIONS

def start_timer():
    global start_time, end_time, running, target_widget
    if running:
        pass
    else:
        start_time = dt.datetime.now()
        running = True
        update_timer()
        target_widget.config(text="Target: " + str(ans) + "\n")


def stop_timer():
    global start_time, end_time, running
    end_time = dt.datetime.now()
    running = False
    stopwatch_label.config(text=str(end_time - start_time))


def update_timer():
    global start_time, end_time, running
    stopwatch_label.config(text=str((dt.datetime.now() - start_time) - total_time)[:-4])  # [-4] rounds the milliseconds
    if running:
        stopwatch_label.after(1, update_timer)

# TIMER VARIABLES
empty_dt = dt.timedelta()
running = False
is_reset = True
total_time = dt.timedelta()




# Create the title and rules
root = Tk()
root.title("Digitle")
root.configure(bg='white')
root.iconbitmap("favicon.ico")
frame = Frame(root, padx=20, pady=20, bg='white')

title = Label(frame, text="Digitle", font="Helvetica 37 bold", bg='white')
rules = Label(frame, text="Try to solve the Digitle as quickly as possible!\n\n"
              "Each number from 1-4 must be used once.\n\n"
              "Each Operator (+, -, x) must be used once.\n\n"
              "The target will be revealed when you click start!",
              font="Helvetica 12", padx=20, pady=20, bg='white'
              )

# Create the answer widget
target_widget = Label(frame, text="Target: ?\n", font="Helvetica 20 bold", bg='white')


# Create the input buttons
num1 = Button(frame, font=num_op_font, text=1, command=click_one, relief=GROOVE, borderwidth=button_border_width, cursor=button_curser)
op1 = Button(frame, font=num_op_font, text='+', command=click_add, relief=GROOVE, borderwidth=button_border_width, cursor=button_curser)
num2 = Button(frame, font=num_op_font, text=2, command=click_two, relief=GROOVE, borderwidth=button_border_width, cursor=button_curser)
op2 = Button(frame, font=num_op_font, text='-', command=click_minus, relief=GROOVE, borderwidth=button_border_width, cursor=button_curser)
num3 = Button(frame, font=num_op_font, text=3, command=click_three, relief=GROOVE, borderwidth=button_border_width, cursor=button_curser)
op3 = Button(frame, font=num_op_font, text='x', command=click_times, relief=GROOVE, borderwidth=button_border_width, cursor=button_curser)
num4 = Button(frame, font=num_op_font, text=4, command=click_four, relief=GROOVE, borderwidth=button_border_width, cursor=button_curser)

# Create the user answer area
slot1 = Button(frame, font=num_op_font, relief=GROOVE, state=DISABLED, width=slot_width, borderwidth=slot_border_width)
slot2 = Button(frame, font=num_op_font, relief=GROOVE, state=DISABLED, width=slot_width, borderwidth=slot_border_width)
slot3 = Button(frame, font=num_op_font, relief=GROOVE, state=DISABLED, width=slot_width, borderwidth=slot_border_width)
slot4 = Button(frame, font=num_op_font, relief=GROOVE, state=DISABLED, width=slot_width, borderwidth=slot_border_width)
slot5 = Button(frame, font=num_op_font, relief=GROOVE, state=DISABLED, width=slot_width, borderwidth=slot_border_width)
slot6 = Button(frame, font=num_op_font, relief=GROOVE, state=DISABLED, width=slot_width, borderwidth=slot_border_width)
slot7 = Button(frame, font=num_op_font, relief=GROOVE, state=DISABLED, width=slot_width, borderwidth=slot_border_width)


# Create the check button
check = Button(frame, text="Enter", command=check_ans, font="Helvetica 20 bold", )

result_widget = Label(frame, font="Helvetica 18 bold", bg='white')

user_answer_widget = Label(frame, text="Your Answer: ", font="Helvetica 20 bold", bg='white')



# Create enter button
enter_button_img = PhotoImage(file="enter-button.png")
enter_button = Button(frame, image=enter_button_img, command=check_ans, bg='white', borderwidth=0, cursor=button_curser)

# Create start button
start_button = Button(frame, text="Start", command=start_timer, bg="white", borderwidth=0, cursor=button_curser)


# Create the timer
stopwatch_label = Label(frame, text="0:00:00:00", font="Helvetica 24 bold", bg='white')


# Display the widgets

frame.pack(fill=BOTH, expand=True, padx= 10, pady=20)

title.grid(row=0, columnspan=7)
rules.grid(row=1, columnspan=7)

target_widget.grid(row=2, columnspan=7)

user_answer_widget.grid(row=3, columnspan=7)


slot1.grid(row=4, column=0, padx=5)
slot2.grid(row=4, column=1, padx=5)
slot3.grid(row=4, column=2, padx=5)
slot4.grid(row=4, column=3, padx=5)
slot5.grid(row=4, column=4, padx=5)
slot6.grid(row=4, column=5, padx=5)
slot7.grid(row=4, column=6, padx=5)

result_widget.grid(row=6, columnspan=7)

num1.grid(row=7, column=0, padx=5, pady=0)
op1.grid(row=7, column=1, padx=5, pady=0)
num2.grid(row=7, column=2, padx=5, pady=0)
op2.grid(row=7, column=3, padx=5, pady=0)
num3.grid(row=7, column=4, padx=5, pady=0)
op3.grid(row=7, column=5, padx=5, pady=0)
num4.grid(row=7, column=6, padx=5, pady=0)

enter_button.grid(row=8, columnspan=7, pady=20)

stopwatch_label.grid(row=9, columnspan=7)
start_button.grid(row=10, columnspan=7)



# Loads default button and board states
reset_buttons()
reset_answer_board()




frame.mainloop()