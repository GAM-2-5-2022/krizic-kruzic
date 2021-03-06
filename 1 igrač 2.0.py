import tkinter

# create the window
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(0, 0) # Use this secret command to make the window fits all needs, buttons and etc.

# create 9 buttons and grid them 3x3
b1 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b1)) # create button
b1.grid(row=1, column=1) # arrange the buttons in a 3x3 grid

b2 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b2))
b2.grid(row=1, column=2)

b3 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b3))
b3.grid(row=1, column=3)

b4 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b4))
b4.grid(row=2, column=1)

b5 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b5))
b5.grid(row=2, column=2)

b6 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b6))
b6.grid(row=2, column=3)

b7 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b7))
b7.grid(row=3, column=1)

b8 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b8))
b8.grid(row=3, column=2)

b9 = tkinter.Button(window, text=" ", font='Times 20 bold', bg='white', height=4, width=8, command=lambda: btn_click(b9))
b9.grid(row=3, column=3)

# store buttons in a list
buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

# create btn_click function
def btn_click(btn_clicked):
    btn_clicked['text'] = "X" # change the text of the button
    btn_clicked['state'] = 'disabled' # disable the button
    btn_clicked['bg'] = 'red' # change the background color of the button

    def checkforwinner():
        # if first row is X
        if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
            # make all buttons disabled
            for btn in buttons:
                btn['state'] = 'disabled'
            tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

        # if second row is X
        elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
            # make all buttons disabled
            for btn in buttons:
                btn['state'] = 'disabled'
            tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

        # if third row is X
        elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
            # make all buttons disabled
            for btn in buttons:
                btn['state'] = 'disabled'
            tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

        # if first column is X
        elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
            # make all buttons disabled
            for btn in buttons:
                btn['state'] = 'disabled'
            tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

        # if second column is X
        elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
            # make all buttons disabled
            for btn in buttons:
                btn['state'] = 'disabled'
            tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

        # if third column is X
        elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
            # make all buttons disabled
            for btn in buttons:
                btn['state'] = 'disabled'
            tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

        # if first diagonal is X
        elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
            # make all buttons disabled
            for btn in buttons:
                btn['state'] = 'disabled'
            tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

        # if second diagonal is X
        elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
            # make all buttons disabled
            for btn in buttons:
                btn['state'] = 'disabled'
            tkinter.Message(window, text='X wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

        else:
            emptybuttons = []
            if b1['text'] == " ":
                emptybuttons.append(b1)
            if b2['text'] == " ":
                emptybuttons.append(b2)
            if b3['text'] == " ":
                emptybuttons.append(b3)
            if ['text'] == " ":
                emptybuttons.append(b4)
            if b5 == " ":
                emptybuttons.append(b5)
            if b6['text'] == " ":
                emptybuttons.append(b6)
            if b7['text'] == " ":
                emptybuttons.append(b7)
            if b8['text'] == " ":
                emptybuttons.append(b8)
            if b9['text'] == " ":
                emptybuttons.append(b9)

            # randomly select a button from the list
            import random
            random_button = random.choice(emptybuttons)

            # change button text to O
            random_button.config(text="O")

            # make button disabled
            random_button.config(state=tkinter.DISABLED)

            # make O blue
            random_button.config(bg="blue")

            # clear the list
            emptybuttons.clear()

            # if first row is O
            if b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if second row is O
            elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if third row is O
            elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if first column is O
            elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if second column is O
            elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if third column is O
            elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if first diagonal is O
            elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)

            # if second diagonal is O
            elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
                # make all buttons disabled
                for btn in buttons:
                    btn['state'] = 'disabled'
                tkinter.Message(window, text='O wins!', width=100, bg='green', font='Times 20 bold').grid(row=4, column=1)
    checkforwinner()

if __name__ == "__main__":
    window.mainloop()
