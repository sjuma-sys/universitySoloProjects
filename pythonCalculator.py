import _tkinter
import tkinter.font as font
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import messagebox
import _thread
import threading
import math
import time
import random
from time import sleep
#------------GUI-root-with-Frames-------------------------
#zain initialiser to create window
root = Tk()
#sets window background colour
root.configure(bg='grey')
#sets window size but is still resizable
root.geometry('300x400')
#makes window non resizable
root.resizable(width=False, height=False)

#this is a frame that stores the contents
contentFrame = Frame(root,
width=300,
height=400,
relief=RAISED)
contentFrame.pack()

#this is a frame that stores the buttons at the bottom
buttonsFrame = Frame(root,
width=280,
height=220,
relief=SUNKEN,
bg='white')
buttonsFrame.place(x=9, y=170)

#this is a frame that stores content at the top of the contentframe
topFrame = Frame(contentFrame)
topFrame.pack(side=TOP)


#--------------------global-variables---------------
final_value = 0
before_eq = ''
ans_recv = False
afk_count = 0
times_passed = 0
temp_val = 0
sqrt_used = False
before_eq_sq = False

#---------------------functions----------------------
def clear():
    global final_value, before_eq, ans_recv, times_passed, sqrt_used, before_eq_sq

    final_value = 0
    before_eq = ''
    viewansr.delete(0,END)
    ans_recv = False
    times_passed = 0
    sqrt_used = False
    before_eq_sq = False


def click(number):
    global final_value, ans_recv

    #if an answer has been recieved after using =, it will delete the entry and continue using it if user doesnt ppress clear
    if ans_recv == True:
        viewansr.delete(0,END)
        ans_recv = False
    value=viewansr.get()
    viewansr.delete(0,END)
    viewansr.insert(0,str(value) + str(number))


def add_():
    global final_value, before_eq, sqrt_used, before_eq_sq

    if viewansr.get() == '':
        return

    if before_eq_sq == True and '√' in viewansr.get():
        temp_val = 0
        #gets temporary value to store sqrt of answr
        temp_val = get_sqrt(viewansr)
        before_eq = '+'
        before_eq_sq = False
        #adds final_value and temp_val together
        final_value += temp_val
        viewansr.delete(0, END)
        #if its the user first input, assigns final value to input
        if times_passed == 0 and ans_recv == False:
            final_value = temp_val
            viewansr.delete(0, END)
            before_eq = '+'
            times_passed += 1
            return
        return
    else:
        value = float(viewansr.get())
        final_value += value
        viewansr.delete(0, END)
        before_eq = '+'


def subtract_():
    global final_value, before_eq, times_passed, sqrt_used, before_eq_sq

    if viewansr.get() == '':
        return

    if before_eq_sq == True and '√' in viewansr.get():
        temp_val = 0
        #gets temporary value to store sqrt of answr
        temp_val = get_sqrt(viewansr)
        before_eq = '-'
        before_eq_sq = False
        #subtracts final_value and temp_val together
        final_value -= temp_val
        viewansr.delete(0, END)
        #if its the user first input, assigns final value to input
        if times_passed == 0 and ans_recv == False:
            final_value = temp_val
            viewansr.delete(0, END)
            before_eq = '-'
            times_passed += 1
            return
        return

    else:
        value = float(viewansr.get())
        #if final value is 0 and an answer has been recieved, it will assign the value to
        #final value to be stored to be used for subtraction to continue the equation after equals function
        if final_value == 0 and ans_recv == True:
            final_value = value
            viewansr.delete(0, END)
            before_eq = '-'
            return
        #if the amount of times passing the functions is 0, it will assign the final value to value so it can be
        #operated on the number provided rather than zero which will output an incorrect answer
        elif times_passed == 0 and ans_recv == False:
            final_value = value
            viewansr.delete(0, END)
            before_eq = '-'
            times_passed += 1
            return
        final_value -= value
        viewansr.delete(0, END)
        before_eq = '-'
        return


def divide_():
    global final_value, before_eq, times_passed, sqrt_used, before_eq_sq

    if viewansr.get() == '':
        return

    if before_eq_sq == True and '√' in viewansr.get():
        temp_val = 0
        #gets temporary value to store sqrt of answr
        temp_val = get_sqrt(viewansr)
        #if its the user first input, assigns final value to input
        if times_passed == 0 and ans_recv == False:
            final_value = temp_val
            viewansr.delete(0, END)
            before_eq = '/'
            times_passed += 1
            return

        before_eq = '/'
        before_eq_sq = False
        #divides final_value and temp_val together
        final_value = final_value / temp_val
        viewansr.delete(0, END)
        return

    else:
        value = float(viewansr.get())
        #if final value is 0 and an answer has been recieved, it will assign the value to
        #final value to be stored to be used for division to continue the equation after equals function
        if final_value == 0 and ans_recv == True:
            final_value = value
            viewansr.delete(0, END)
            before_eq = '/'
            return
        #if the amount of times passing the functions is 0, it will assign the final value to value so it can be
        #operated on the number provided rather than zero which will output an incorrect answer
        elif times_passed == 0 and ans_recv == False:
            final_value = value
            viewansr.delete(0, END)
            before_eq = '/'
            times_passed += 1
            return
        final_value = final_value / value
        viewansr.delete(0, END)
        before_eq = '/'
        return


def multiply_():
    global final_value, before_eq, times_passed, temp_val, sqrt_used, before_eq_sq

    if viewansr.get() == '':
        return

    if before_eq_sq == True and '√' in viewansr.get():
        temp_val = 0
        #gets temporary value to store sqrt of answr
        temp_val = get_sqrt(viewansr)

        #if its the user first input, assigns final value to input
        if times_passed == 0 and ans_recv == False:
            final_value = temp_val
            viewansr.delete(0, END)
            before_eq = '*'
            times_passed += 1
            return
        #if final value is 0 and an answer has been recieved, it will assign the value to
        #final value to be stored to be used for division to continue the equation after equals function
        if final_value == 0 and ans_recv == True:
            final_value = value
            viewansr.delete(0, END)
            before_eq = '*'
            return

        before_eq = '*'
        before_eq_sq = False
        #multiplies final_value and temp_val together
        final_value = final_value * temp_val
        viewansr.delete(0, END)
        return

    else:
        value = float(viewansr.get())
        #if final value is 0 and an answer has been recieved, it will assign the value to
        #final value to be stored to be used for multiplication to continue the equation after equals function
        if final_value == 0 and ans_recv == True:
            final_value = value
            viewansr.delete(0, END)
            before_eq = '*'
            return
        #if the amount of times passing the functions is 0, it will assign the final value to value so it can be
        #operated on the number provided rather than zero which will output an incorrect answer
        elif times_passed == 0 and ans_recv == False:
            final_value = value
            viewansr.delete(0, END)
            before_eq = '*'
            times_passed += 1
            return
        final_value = final_value * value
        viewansr.delete(0, END)
        before_eq = '*'
        return


def sqrt_():
    global final_value, before_eq, times_passed, sqrt_used, before_eq_sq

    viewansr.insert(0,'√')

    sqrt_used = True
    before_eq_sq = True

def exp():
    global final_value, before_eq, times_passed, sqrt_used, before_eq_sq, exp_used
    if viewansr.get() == '':
        return

    if before_eq_sq == True and '√' in viewansr.get():
        temp_val = 0
        #gets temporary value to store sqrt of answr
        temp_val = get_sqrt(viewansr)
        if times_passed == 0 and ans_recv == False:
            final_value = temp_val
            viewansr.delete(0, END)
            before_eq = '**'
            times_passed += 1
            return
        #if final value is 0 and an answer has been recieved, it will assign the value to
        #final value to be stored to be used for division to continue the equation after equals function
        if final_value == 0 and ans_recv == True:
            final_value = value
            viewansr.delete(0, END)
            before_eq = '**'
            return

        before_eq = '**'
        before_eq_sq = False
        #multiplies final_value and temp_val together
        final_value = final_value ** temp_val
        viewansr.delete(0, END)
        return

    else:
        value = float(viewansr.get())
        #if final value is 0 and an answer has been recieved, it will assign the value to
        #final value to be stored to be used for multiplication to continue the equation after equals function
        if final_value == 0 and ans_recv == True:
            final_value = value
            viewansr.delete(0, END)
            before_eq = '**'
            return
        #if the amount of times passing the functions is 0, it will assign the final value to value so it can be
        #operated on the number provided rather than zero which will output an incorrect answer
        elif times_passed == 0 and ans_recv == False:
            final_value = value
            viewansr.delete(0, END)
            before_eq = '**'
            times_passed += 1
            return
        final_value = final_value ** value
        viewansr.delete(0, END)
        before_eq = '**'
        return

def equal():
    global final_value, before_eq, ans_recv, temp_val, sqrt_used, before_eq_sq

    #statements to get the last operation before equals
    if sqrt_used == True:
        if before_eq == '+' and before_eq_sq == True:
            fin_val = get_sqrt()
            final_value += fin_val
        elif before_eq == '+' and before_eq_sq == False:
            fin_val = float(viewansr.get())
            final_value = final_value + fin_val

        elif before_eq == '-' and before_eq_sq == True:
            fin_val = get_sqrt()
            final_value -= fin_val
        elif before_eq == '-' and before_eq_sq == False:
            fin_val = float(viewansr.get())
            final_value = final_value - fin_val

        elif before_eq == '/' and before_eq_sq == True:
            fin_val = get_sqrt()
            final_value = final_value / fin_val
        elif before_eq == '/' and before_eq_sq == False:
            fin_val = float(viewansr.get())
            final_value = final_value / fin_val

        elif before_eq == '*' and before_eq_sq == True:
            fin_val = get_sqrt()
            final_value = final_value * fin_val
        elif before_eq == '*' and before_eq_sq == False:
            fin_val = float(viewansr.get())
            final_value = final_value * fin_val
        if before_eq == '' and before_eq_sq == True:
            fin_val = get_sqrt()
            final_value = fin_val

    else:
        if before_eq == '+':
            fin_val = float(viewansr.get())
            final_value += fin_val
        elif before_eq == '-':
            fin_val = float(viewansr.get())
            final_value -= fin_val
        elif before_eq == '/':
            fin_val = float(viewansr.get())
            final_value = final_value / fin_val
        elif before_eq == '*':
            fin_val = float(viewansr.get())
            final_value = final_value * fin_val
        elif before_eq == '**':
            fin_val = float(viewansr.get())
            final_value = final_value ** fin_val


    viewansr.delete(0, END)
    viewansr.insert(0, float(final_value))

    #this is to clear the previous answer when they
    #begin to put in another calculation
    temp = final_value
    final_value = 0
    before_eq = ''
    ans_recv = True
    times_passed = 0


def get_sqrt(*args):
    #creation of empty list
    empty_list = []

    #goes through numbers in entry box
    for i in viewansr.get():
        #if the item at index i is a sqrt symbol, it will continue to the next position
        if i == '√':
            continue
            #else, it will append the item, in this case a number into the empty list
        else:
            empty_list.append(str(i))

    #this joins the items in the list as a float
    sqrt_val= float(''.join(empty_list))
    sqrt_val = math.sqrt(sqrt_val)
    return sqrt_val


def zain():
    #takes the global variable afk count
    global afk_count
    #starts new thread to count the seconds that the user if afk
    afk_thread = threading.Timer(1, zain)
    #starts thread
    afk_thread.start()

    in_box = str(viewansr.get())

    if in_box != '':
        afk_count = 0
        return
    #-----------------------------
    #fix this so that it doesnt repeatdidly output the message box
    if afk_count == 60:
        afk_count +=1
        messagebox.showwarning(title='Away', message='You have been away for: 1 minute.\nIf you are inactive for 2 minutes the app will close.')
    elif afk_count == 120:
        afk_count +=1
        #cancels thread
        afk_thread.cancel()
        messagebox.showinfo(title='Away', message='Closing application')
        #exits app
        root.quit()
    else:
        afk_count +=1
        return


def disco():
    #for loop to continue until it reaches 900
    for i in range(900):
        #nested loop to do the following commands everytime i increments in the loop before
        for i in (clear_button, zero,decimal,multiply, equals, one,two,three,divide,
        four,five,six,subtract, power,seven,eight,nine, add, sqrt, disco_activate):
            #this variable contains all the colours to be used for the bg
            colours = ('black', 'purple', 'orange', 'green')
            #this variable is the colour to be used for fg
            contrasts = ('white', 'yellow', 'pink')
            #this configures the button variable that i is at and assigns it a random colour and contrast
            i.configure(bg = random.choice(colours), fg = random.choice(contrasts))
            #this makes the thread sleep for 1 seconds
            time.sleep(0.2)

def seconddisco():
        while True:
            colours = ('black', 'purple', 'orange', 'green')
            contrasts = ('grey', 'brown', 'yellow', 'pink')
            for i in range(0,6):
                Button(buttonsFrame,width=4,height=1, font=('Times new roman', 10),padx=2, background = random.choice(contrasts)).grid(row=i,column=0)
                Button(buttonsFrame,width=4,height=1, font=('Times new roman', 10),padx=2, background=random.choice(colours)).grid(row=i,column=6)
            for i in range(0,7):
                Button(buttonsFrame,width=4,height=1, font=('Times new roman', 10),padx=2, background = random.choice(colours)).grid(row=0,column=i)
                Button(buttonsFrame,width=4,height=1, font=('Times new roman', 10),padx=2, background=random.choice(contrasts)).grid(row=5,column=i)

def wegoagain_start():
    wegoagain.start()

#----------------------wigits-------------------------

#title for calculator
calc_title = Label(topFrame,relief=RAISED,text='Calculator',fg = 'black',width=300,height=2,font=('Times new roman', 14))
calc_title.pack()

#an entry window for storing the answers and equations that user inputs to output it
viewansr = Entry(root,font=('Times new roman', 13),relief=SUNKEN,width=31)
viewansr.place(x=9,y=55, height=110)

#---------------buttons--------------------
#this was used to get the x values for each x position of a grid
#this was used to get the x values for each x position of a grid
for i in range(0,6):
    Button(buttonsFrame,width=4,height=1, font=('Times new roman', 10),padx=2).grid(row=i,column=0)
    Button(buttonsFrame,width=4,height=1, font=('Times new roman', 10),padx=2).grid(row=i,column=6)
for i in range(0,7):
    Button(buttonsFrame,width=4,height=1, font=('Times new roman', 10),padx=2).grid(row=0,column=i)
    Button(buttonsFrame,width=4,height=1, font=('Times new roman', 10),padx=2).grid(row=5,column=i)

#button for zero
zero = Button(buttonsFrame,text='0',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=lambda: click(0))
zero.grid(row=4,column=1)

#button for one
one = Button(buttonsFrame,text='1',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=lambda: click(1))
one.grid(row=3,column=1)

#button for two
two = Button(buttonsFrame,text='2',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=lambda: click(2))
two.grid(row=3,column=2)

#button for three
three = Button(buttonsFrame,text='3',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=lambda: click(3))
three.grid(row=3,column=3)

#button for four
four = Button(buttonsFrame,text='4',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=lambda: click(4))
four.grid(row=2,column=1)

#button for five
five = Button(buttonsFrame,text='5',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=lambda: click(5))
five.grid(row=2,column=2)

#button for six
six = Button(buttonsFrame,text='6',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=lambda: click(6))
six.grid(row=2,column=3)

#button for seven
seven = Button(buttonsFrame,text='7',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=lambda: click(7))
seven.grid(row=1,column=1)

#button for eight
eight = Button(buttonsFrame,text='8',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=lambda: click(8))
eight.grid(row=1,column=2)

#button for nine
nine = Button(buttonsFrame,text='9',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=lambda: click(9))
nine.grid(row=1,column=3)

#button for decimal
decimal = Button(buttonsFrame,text='.',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=lambda: click('.'))
decimal.grid(row=4,column=3)

#button for clear
clear_button = Button(buttonsFrame,text='CLR',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=clear)
clear_button.grid(row=4,column=2)

#button for add
add = Button(buttonsFrame,text='+',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=add_)
add.grid(row=1,column=4)

#button for subtract
subtract = Button(buttonsFrame,text='-',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=subtract_)
subtract.grid(row=2,column=4)

#button for divide
divide = Button(buttonsFrame,text='÷',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=divide_)
divide.grid(row=3,column=4)

#button for multiply
multiply = Button(buttonsFrame,text='x',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=multiply_)
multiply.grid(row=4,column=4)

#button for equals
equals = Button(buttonsFrame,text='=',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=equal)
equals.grid(row=3,column=5)


#button for power
power = Button(buttonsFrame,text='**',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2, command=exp)
power.grid(row=2,column=5)

#button for disco_activation
disco_activate = Button(buttonsFrame,text='$',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2, command=wegoagain_start)
disco_activate.grid(row=4,column=5)

#button for sqrt
sqrt = Button(buttonsFrame,text='√',font=('Times new roman', 10),width=4,height=1,activebackground='orange',padx=2,command=sqrt_)
sqrt.grid(row=1,column=5)

#this function changes colours of buttons
def disco():
    for i in range(900):
        for i in (one, two, three, four, five, six, seven, eight, nine):
            colours = ('black', 'purple', 'orange', 'green')
            contrasts = ('grey', 'brown', 'yellow', 'pink')
            i.configure(bg =random.choice(colours), fg=random.choice(contrasts))
            sleep(2.5)

wegoagain = threading.Thread(target=seconddisco, daemon=True)
partytime = threading.Thread(target=disco, daemon=True)
partytime.start()
root.mainloop()
