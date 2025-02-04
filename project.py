from tkinter import *



window = Tk()
window.geometry('800x400')


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
                font=('times new roman', 25))
nitemode_button.place(x=290, y=325)

window.mainloop()