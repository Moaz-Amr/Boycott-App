from tkinter import *
import tkinter as tk



window = tk.Tk()
window.geometry('800x400')
background_image = tk.PhotoImage(file="D:\\mrmaz\\Documents\\SWE Orange\\final project\\5-41.png")  # استبدل هذا بمسار الصورة الخاصة بك
label = tk.Label(window, image=background_image)
label.place(x=0, y=0, relwidth=1, relheight=1)
current_image = background_image

def swich_mode():
    global current_image
    if current_image == background_image:
        current_image = tk.PhotoImage(file="D:\\mrmaz\\Documents\\SWE Orange\\final project\\jerusalem-4296503_960_720.png")
    else:
        current_image = background_image
    
    label.configure(image=current_image)
def end():
    window.destroy()
    
def check():
    user_input = user_entry.get().strip()  
    
    with open('D:\\mrmaz\\Documents\\SWE Orange\\day3\\Boycott Brands.txt') as file:
        content = file.readlines()  
        content = [line.strip() for line in content] 
        
        
        for brand in content:
            if user_input.lower() == brand.lower():  
                title_2['text'] = 'Result: dont  buy from this brand!'
                title_2['fg'] = 'red'
                return
                
        title_2['text'] = 'Result: buy from this brand!'
        title_2['fg'] = 'green'

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
                font=('times new roman', 25), command=check)
check_button.place(x=280, y=250)

exit_button = Button(window, text='Exit', bg='green',
                font=('times new roman', 25), command=end)
exit_button.place(x=500, y=250)

nitemode_button = Button(window, text='Nite Or Light Mode', bg='black',fg='white',
                font=('times new roman', 25), command=swich_mode)
nitemode_button.place(x=290, y=325)


window.mainloop()