from tkinter import *
root = Tk()

e = Entry(root, width=75, bg="#854ebf", fg="white", borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ")

def my_click():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text='click me', padx=50, pady=20, command=my_click, fg="blue", bg="#579c69")
myButton.pack()

root.mainloop()
