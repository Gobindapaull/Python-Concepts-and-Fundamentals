from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Image")

img = ImageTk.PhotoImage(Image.open("eth.png"))
my_label = Label(image=img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
