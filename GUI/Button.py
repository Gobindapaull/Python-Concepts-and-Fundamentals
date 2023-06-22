from tkinter import *
root = Tk()

def my_click():
    myLabel = Label(root, text='You clicked on the button')
    myLabel.pack()

myButton = Button(root, text='click me', padx=50, pady=20, command=my_click, fg="blue", bg="#579c69")
myButton.pack()

root.mainloop()
