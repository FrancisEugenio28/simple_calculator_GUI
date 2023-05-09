#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Simple Calculator w/ GUI

#create a GUI for our calculator
from tkinter import *

root = Tk()
root.title('Simple Calculator')
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')

#create a space where the calculation takes place or the screen of a calculator
input_digit = Label(root, text='', bg='black', fg='white')
input_digit.grid(row=0, column=0, pady=(50,25), columnspan=5, sticky='w')
input_digit.config(font=('verdana',30, 'bold'))
    # create a functioning button for 7
    # create a functioning button for 8 
    # create a functioning button for 9
    # create a functioning button for +
    # create a functioning button for 4
    # create a functioning button for 5
    # create a functioning button for 6
    # create a functioning button for -
    # create a functioning button for 1
    # create a functioning button for 2
    # create a functioning button for 3
    # create a functioning button for *
    # create a functioning button for clear
    # create a functioning button for 0
    # create a functioning button for =
    # create a functioning button for /
# give function for each number button
# gather all the input digits based on the pressed button in the GUI
# Give a function for the clear button
# Perform operation within the = button

root.mainloop()
