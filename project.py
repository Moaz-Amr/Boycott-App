from tkinter import *



window = Tk()
window.geometry('800x400')


title_1 = Label(window, text='Enter Brand Name', fg='red',
                font=('times new roman', 25))
title_1.place(x=280, y=60)

title_2 = Label(window, text='Result:', fg='red',
                font=('times new roman', 25))
title_2.place(x=250, y=150)


user_entry = Entry(window, fg='black', bg='yellow',
                font=('times new roman', 25))
user_entry.place(x=250, y=100)

check_button = Button(window, text='Check', bg='yellow',
                font=('times new roman', 25))
check_button.place(x=280, y=250)

exit_button = Button(window, text='Exit', bg='green',
                font=('times new roman', 25))
exit_button.place(x=500, y=250)

nitemode_button = Button(window, text='Nite Or Light Mode', bg='black',fg='white',
                font=('times new roman', 25))
nitemode_button.place(x=290, y=325)

window.mainloop()