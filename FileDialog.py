from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("My Name is Kharnashu")


def open():
    global my_image
    filename = filedialog.askopenfilename(parent=root,initialdir='/kinter/images',title="select a file",
                                                filetypes=(("PNG files","*.png"),("All files","*")))

    my_label = Label(root,text= filename)
    my_label.pack()

    my_image = ImageTk.PhotoImage(Image.open(filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="open file",command=open).pack()

root.mainloop()