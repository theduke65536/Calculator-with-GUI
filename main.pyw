from tkinter import *

number_bar_text = ''


def number_bar_append(text):
    global number_bar_text

    number_bar_text = str(number_bar_text)
    number_bar_text += text

    return number_bar_text


def type_one():
    text = number_bar_append('1')
    number_bar.config(text=text)


def type_two():
    text = number_bar_append('2')
    number_bar.config(text=text)


def type_three():
    text = number_bar_append('3')
    number_bar.config(text=text)


def type_four():
    text = number_bar_append('4')
    number_bar.config(text=text)


def type_five():
    text = number_bar_append('5')
    number_bar.config(text=text)


def type_six():
    text = number_bar_append('6')
    number_bar.config(text=text)


def type_seven():
    text = number_bar_append('7')
    number_bar.config(text=text)


def type_eight():
    text = number_bar_append('8')
    number_bar.config(text=text)


def type_nine():
    text = number_bar_append('9')
    number_bar.config(text=text)


def type_zero():
    text = number_bar_append('0')
    number_bar.config(text=text)


def type_add():
    text = number_bar_append(' + ')
    number_bar.config(text=text)



def type_sub():
    text = number_bar_append(' - ')
    number_bar.config(text=text)


def type_div():
    text = number_bar_append(' ÷ ')
    number_bar.config(text=text)


def type_mult():
    text = number_bar_append(' x ')
    number_bar.config(text=text)


def add(num1,num2):
    global number_bar_text

    num3 = num1 + num2
    number_bar.config(text=num3)
    number_bar_text = num3

    return num3


def sub(num1,num2):

    num3 = num1 - num2

    global number_bar_text
    number_bar.config(text=num3)
    number_bar_text = num3

    return num3


def div(num1,num2):
    num3 = num1 / num2

    global number_bar_text
    number_bar.config(text=num3)
    number_bar_text = num3

    return num3


def mult(num1,num2):
    num3 = num1 * num2

    global number_bar_text
    number_bar.config(text=num3)
    number_bar_text = num3

    return num3


def delete():
    global number_bar_text

    number_bar.config(text='')
    number_bar_text = ''


def decimal():
    text = number_bar_append('.')
    number_bar.config(text=text)


def negative():
    text = number_bar_append('-')
    number_bar.config(text=text)


def equals():
    expression = number_bar.cget('text')
    for i in expression:
        if i == '+':

            num1 = float(expression[:expression.index('+')])
            num2 = float(expression[expression.index('+')+1:])
            _sum = add(num1,num2)
            number_bar.config(text=str(_sum))

        if i == '-':

            if expression[expression.index(i)+1] == ' ':
                num1 = float(expression[:expression.index('-')])
                num2 = float(expression[expression.index('-')+1:])
                dif = sub(num1,num2)
                number_bar.config(text=str(dif))

        if i == '÷':

            num1 = float(expression[:expression.index('÷')])
            num2 = float(expression[expression.index('÷')+1:])
            quo = div(num1,num2)
            number_bar.config(text=str(quo))

        if i == 'x':

            num1 = float(expression[:expression.index('x')])
            num2 = float(expression[expression.index('x')+1:])
            prod = mult(num1,num2)
            number_bar.config(text=str(prod))




window = Tk()
window.title('Calculator')
window.config(background='black')
window.geometry('770x450')

frame = Frame(window)
frame.pack()
frame.config(background='black')


number_bar = Label(window, text='', font=('Arial', 50), bg='silver', width=20, background='grey')

button1 = Button(frame, command=type_one, text='1', font=('Arial', 10), height=4, width=9, bg='grey')
button2 = Button(frame, command=type_two, text='2', font=('Arial', 10), height=4, width=9, bg='grey')
button3 = Button(frame, command=type_three, text='3', font=('Arial', 10), height=4, width=9, bg='grey')
button4 = Button(frame, command=type_four, text='4', font=('Arial', 10), height=4, width=9, bg='grey')
button5 = Button(frame, command=type_five, text='5', font=('Arial', 10), height=4, width=9, bg='grey')
button6 = Button(frame, command=type_six, text='6', font=('Arial', 10), height=4, width=9, bg='grey')
button7 = Button(frame, command=type_seven, text='7', font=('Arial', 10), height=4, width=9, bg='grey')
button8 = Button(frame, command=type_eight, text='8', font=('Arial', 10), height=4, width=9, bg='grey')
button9 = Button(frame, command=type_nine, text='9', font=('Arial', 10), height=4, width=9, bg='grey')
button0 = Button(frame, command=type_zero, text='0', font=('Arial', 10), height=4, width=9, bg='grey')
button_add = Button(frame, command=type_add, text='+',font=('Arial', 10), height=4, width=9, bg='grey')
button_subtract = Button(frame, command=type_sub, text='-',font=('Arial', 10), height=4, width=9, bg='grey')
button_divide = Button(frame, command=type_div, text='÷',font=('Arial', 10), height=4, width=9, bg='grey')
button_multiply = Button(frame, command=type_mult, text='x',font=('Arial', 10), height=4, width=9, bg='grey')

button_delete = Button(frame, command=delete, text='⌫', font=('Arial', 10), height=4, width=9, bg='grey')
button_equals = Button(frame, command=equals, text='=',font=('Arial', 10), height=4, width=9, bg='grey')
button_decimal = Button(frame, command=decimal, text='.',font=('Arial', 10), height=4, width=9, bg='grey')
button_negative = Button(frame, command=negative, text='+/-',font=('Arial', 10), height=4, width=9, bg='grey')

number_bar.pack(side=TOP)

button1.grid(row=3,column=1)
button2.grid(row=3,column=2)
button3.grid(row=3,column=3)
button4.grid(row=2,column=1)
button5.grid(row=2,column=2)
button6.grid(row=2,column=3)
button7.grid(row=1,column=1)
button8.grid(row=1,column=2)
button9.grid(row=1,column=3)
button0.grid(row=4,column=1)

button_add.grid(row=4,column=3)
button_subtract.grid(row=3,column=4)
button_multiply.grid(row=2,column=4)
button_divide.grid(row=1,column=4)

button_equals.grid(row=4,column=4)
button_delete.grid(row=0, column=1)
button_decimal.grid(row=4,column=2)
button_negative.grid(row=0,column=2)

window.mainloop()
