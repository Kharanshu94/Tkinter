# from cgitb import text
# from glob import glob
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

from setuptools import Command

root = Tk()
root.title("Kharanshu")
root.geometry("400x400")

List_l = Listbox(root, width=50, height=10,background="#92B4EC")
List_r = Listbox(root, width=50, height=10,background="#00FFAB")


my_listbox = Listbox(root)
my_listbox.pack(pady=25)

def open():
    global my_listbox
    global original_Name
    global fileN
    global filename

    # clear1
    my_listbox.delete(0,END)

    filename = filedialog.askopenfilenames(initialdir='/kinter/images',title="select a file",
                                                filetypes=(("PNG files","*.png"),("All files","*")))

    # my_label = Label(root,text= filename)
    # my_label.pack()

    fileN = list(filename) 
    original_Name=[]

    for i in fileN:
        original_Name.append(os.path.basename(i))
    
    dict12 = dict(zip(original_Name,fileN))

    for i in original_Name:
        my_listbox.insert(END,i)

def MoveTo(fromList,toList):
    index_list = fromList.curselection()
    if index_list:
        index = index_list[0] 
        val = fromList.get(index)
        fromList.delete(index)
        toList.insert(END,val)

def scale_up(self):
    l = self.my_listbox
    posList = l.curselection()

    # exit if the list is empty
    if not posList:
        return

    for pos in posList:

        # skip if item is at the top
        if pos == 0:
            continue

        text = l.get(pos)
        l.delete(pos)
        l.insert(pos-1, text)

def select():
    my_label.config(text=my_listbox.get(ANCHOR))
    
    
def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text="")

def clear1():
    my_listbox.delete(0,END)

frame = Frame(root)

b1 = Button(frame, text=">",command=lambda: MoveTo(List_l,List_r))
b2 = Button(frame, text="<",command=lambda: MoveTo(List_r,List_l))

b1.pack(side="top")
b2.pack(side="bottom")

List_l.pack(side = "left")
frame.pack(side = "left")
List_r.pack(side = "left")
    
my_btn = Button(root, text="open file",command=open).pack()

my_button  = Button(root, text="Delete",command=delete)
my_button.pack(pady=10)

b_arrange  = Button(root, text="^",command=clear1)
b_arrange.pack(pady=10)


global my_label

my_label = Label(root,text='')
my_label.pack(pady=5)


root.mainloop()