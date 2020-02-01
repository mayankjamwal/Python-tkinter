from tkinter import *

root = Tk()
root.title("Calculator 1.0")

def button_play(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_delete():
    e.delete(0,END)

def button_ad():
    add_num = e.get()
    global first_num
    global math 
    math = 'addition'
    first_num = int(add_num)
    e.delete(0,END)

def button_su():
    add_num = e.get()
    global first_num
    global math
    math = 'subtraction'
    first_num = int(add_num)
    e.delete(0,END)

def button_multi():    
    add_num = e.get()
    global first_num
    global math
    math = 'multiplication'
    first_num = int(add_num)
    e.delete(0,END)

def button_div():    
    add_num = e.get()
    global first_num
    global math
    math = 'division'
    first_num = int(add_num)
    e.delete(0,END)

def button_eq():
    
    second_number = e.get()
    e.delete(0,END)
    if  math == 'addition':
        e.insert(0,first_num + int(second_number))
    elif math == 'subtraction':
        e.insert(0,first_num - int(second_number))
    elif math == 'multiplication':
        e.insert(0,first_num * int(second_number))
    elif math == 'division':
        e.insert(0,first_num / int(second_number))              
#Enter value
e = Entry(root,width=35, borderwidth=5)

e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#make button 
button_1 = Button(root,text='1',padx=40,pady=22,bg='orange',fg='white',command=lambda: button_play(1))
button_2 = Button(root,text='2',padx=40,pady=22,bg='orange',fg='white',command=lambda: button_play(2))
button_3 = Button(root,text='3',padx=40,pady=22,bg='orange',fg='white',command=lambda: button_play(3))
button_4 = Button(root,text='4',padx=40,pady=22,bg='orange',fg='white',command=lambda: button_play(4))
button_5 = Button(root,text='5',padx=40,pady=22,bg='orange',fg='white',command=lambda: button_play(5))
button_6 = Button(root,text='6',padx=40,pady=22,bg='orange',fg='white',command=lambda: button_play(6))
button_7 = Button(root,text='7',padx=40,pady=22,bg='orange',fg='white',command=lambda: button_play(7))
button_8 = Button(root,text='8',padx=40,pady=22,bg='orange',fg='white',command=lambda: button_play(8))
button_9 = Button(root,text='9',padx=40,pady=22,bg='orange',fg='white',command=lambda: button_play(9))
button_0 = Button(root,text='0',padx=40,pady=29,bg='orange',fg='white',command=lambda: button_play(0))
button_add = Button(root,text='+',padx=39,pady=29,bg='lightblue',fg='black',command=lambda: button_ad())
button_subtract = Button(root,text='-',padx=41,pady=29,bg='lightblue',fg='black',command=lambda: button_su())
button_multiple = Button(root,text='*',padx=41,pady=29,bg='lightblue',fg='black',command=lambda: button_multi())
button_divide = Button(root,text='/',padx=41,pady=29,bg='lightblue',fg='black',command=lambda: button_div())
button_clear = Button(root,text='Clear',padx=30,pady=29,bg='blue',fg='white',command=lambda: button_delete())
button_equal = Button(root,text='=',padx=40,pady=111,bg='darkgreen',fg='white',command=lambda: button_eq())

#set button on the window
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5,column=0)
button_divide.grid(row=6,column=0)
button_multiple.grid(row=6,column=1)
button_subtract.grid(row=5,column=1)
button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2,rowspan=3)


root.mainloop()