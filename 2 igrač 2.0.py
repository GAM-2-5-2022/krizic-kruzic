from tkinter import *
import tkinter

# Create the window
window = Tk()
window.title("Tic Tac Toe - PC")
window.resizable(0, 0) # Use this secret command to make the window fits all needs, buttons and etc.

# Create the 9 buttons
button1 = Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: button_click(button1))
button1.grid(row=1, column=1)

button2 = Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: button_click(button2))
button2.grid(row=1, column=2)

button3 = Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: button_click(button3))
button3.grid(row=1, column=3)

button4 = Button(window, text=" ", font='Times 20 bold', bg='white',  height=4, width=8, command=lambda: button_click(button4))
button4.grid(row=2, column=1)

button5 = Button(window, text=" ", font='Times 20 bold', bg='white',  height=4, width=8, command=lambda: button_click(button5))
button5.grid(row=2, column=2)

button6 = Button(window, text=" ", font='Times 20 bold', bg='white',  height=4, width=8, command=lambda: button_click(button6))
button6.grid(row=2, column=3)

button7 = Button(window, text=" ", font='Times 20 bold', bg='white',  height=4, width=8, command=lambda: button_click(button7))
button7.grid(row=3, column=1)

button8 = Button(window, text=" ", font='Times 20 bold', bg='white',  height=4, width=8, command=lambda: button_click(button8))
button8.grid(row=3, column=2)

button9 = Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: button_click(button9))
button9.grid(row=3, column=3)

# Store buttons in a list
buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

# Create turn variable
turn = "X"

# Button_click function
def button_click(button_clicked):
    global turn
    # We won't need to check if button is empty, because we will make
    # it disabled when we click on it. So it cannot be clicked again.
    if turn == "X":
        # Button text is X and disabled
        button_clicked.config(text="X", state=DISABLED)
        # Button background color
        button_clicked.config(bg="red")
        turn = "O"

    elif turn == "O":
        # We will use elif here not if, or then, it won't work properly
        # Button text is O and disabled
        button_clicked.config(text="O", state=DISABLED)
        # Button background color
        button_clicked.config(bg="blue")
        turn = "X"

    # if first row is X
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if first row is O
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if second row is X
    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if second row is O
    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if third row is X
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if third row is O
    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if first column is X
    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if first column is O
    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if second column is X
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if second column is O
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if third column is X
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if third column is O
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if first diagonal is X
    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if first diagonal is O
    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if second diagonal is X
    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="X wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if second diagonal is O
    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="O wins!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

    # if all buttons are disabled
    elif button1["state"] == DISABLED and button2["state"] == DISABLED and button3["state"] == DISABLED and button4["state"] == DISABLED and button5["state"] == DISABLED and button6["state"] == DISABLED and button7["state"] == DISABLED and button8["state"] == DISABLED and button9["state"] == DISABLED:
        # Disable all buttons
        for button in buttons:
            button.config(state=DISABLED)
        tkinter.Message(window, text="Draw!", font='Times 20 bold').grid(row=4, column=1, columnspan=3)

if __name__ == "__main__":
    window.mainloop()
