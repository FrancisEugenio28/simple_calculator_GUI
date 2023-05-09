#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Simple Calculator w/ GUI

#create a GUI for our calculator
from tkinter import *

root = Tk()
root.title('Simple Calculator')
root.geometry('300x380')
root.resizable(0,0)
root.configure(background='black')

try:    
    # give function for each number button
    def get_digit(digit):
        current = input_digit['text']
        new = current + str(digit)
        input_digit.config(text=new)

except ZeroDivisionError:
    print("Syntax Error")

except TypeError:
    print("Syntax Error")

finally: 
    print("Thank You For Using This Small And Simple Calculator ^__^")

#create a space where the calculation takes place or the screen of a calculator
input_digit = Label(root, text='', bg='black', fg='white')
input_digit.grid(row=0, column=0, pady=(50,25), columnspan=5, sticky='w')
input_digit.config(font=('verdana',30, 'bold'))

# create a functioning button for 7
button7 = Button(root, text='7', bg='white', fg='grey', width=5, height=2, command=lambda :get_digit(7))
button7.grid(row=1, column=0)
button7.config(font=('verdana', 14, 'bold'))
    
# create a functioning button for 8 
button8 = Button(root, text='8', bg='white', fg='grey', width=5, height=2, command=lambda :get_digit(8))
button8.grid(row=1, column=1)
button8.config(font=('verdana', 14, 'bold'))

# create a functioning button for 9
button9 = Button(root, text='9', bg='white', fg='grey', width=5, height=2, command=lambda :get_digit(9))
button9.grid(row=1, column=2)
button9.config(font=('verdana', 14, 'bold'))

# create a functioning button for +
button_add = Button(root, text='+', bg='white', fg='grey', width=5, height=2)
button_add.grid(row=1, column=3)
button_add.config(font=('verdana', 14, 'bold'))
    
# create a functioning button for 4
button4 = Button(root, text='4', bg='white', fg='grey', width=5, height=2, command=lambda :get_digit(4))
button4.grid(row=2, column=0)
button4.config(font=('verdana', 14, 'bold'))

# create a functioning button for 5
button5 = Button(root, text='5', bg='white', fg='grey', width=5, height=2, command=lambda :get_digit(5))
button5.grid(row=2, column=1)
button5.config(font=('verdana', 14, 'bold'))
    
# create a functioning button for 6
button6 = Button(root, text='6', bg='white', fg='grey', width=5, height=2, command=lambda :get_digit(6))
button6.grid(row=2, column=2)
button6.config(font=('verdana', 14, 'bold'))

# create a functioning button for -
button_minus = Button(root, text='-', bg='white', fg='grey', width=5, height=2)
button_minus.grid(row=2, column=3)
button_minus.config(font=('verdana', 14, 'bold'))
    
# create a functioning button for 1
button1 = Button(root, text='1', bg='white', fg='grey', width=5, height=2, command=lambda :get_digit(1))
button1.grid(row=3, column=0)
button1.config(font=('verdana', 14, 'bold'))

# create a functioning button for 2
button2 = Button(root, text='2', bg='white', fg='grey', width=5, height=2, command=lambda :get_digit(2))
button2.grid(row=3, column=1)
button2.config(font=('verdana', 14, 'bold'))
    
# create a functioning button for 3
button3 = Button(root, text='3', bg='white', fg='grey', width=5, height=2, command=lambda :get_digit(3))
button3.grid(row=3, column=2)
button3.config(font=('verdana', 14, 'bold'))

# create a functioning button for *
button_multiply = Button(root, text='*', bg='white', fg='grey', width=5, height=2)
button_multiply.grid(row=3, column=3)
button_multiply.config(font=('verdana', 14, 'bold'))

# create a functioning button for clear
button_clear = Button(root, text='AC', bg='white', fg='grey', width=5, height=2)
button_clear.grid(row=4, column=0)
button_clear.config(font=('verdana', 14, 'bold'))
    
# create a functioning button for 0
button0 = Button(root, text='0', bg='white', fg='grey', width=5, height=2, command=lambda :get_digit(0))
button0.grid(row=4, column=1)
button0.config(font=('verdana', 14, 'bold'))

# create a functioning button for =
button_equals = Button(root, text='=', bg='white', fg='grey', width=5, height=2)
button_equals.grid(row=4, column=2)
button_equals.config(font=('verdana', 14, 'bold'))
    
# create a functioning button for /
button_divide = Button(root, text='/', bg='white', fg='grey', width=5, height=2)
button_divide.grid(row=4, column=3)
button_divide.config(font=('verdana', 14, 'bold'))

# gather all the input digits based on the pressed button in the GUI
# Give a function for the clear button
# Perform operation within the = button

root.mainloop()
