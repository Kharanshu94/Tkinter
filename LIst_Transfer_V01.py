# from cgitb import text
# from glob import glob
from heapq import merge
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from PyPDF2 import PdfFileMerger



from setuptools import Command

root = Tk()
root.title("Kharanshu")
root.geometry("400x400")

List_l = Listbox(root, width=50, height=10,background="#92B4EC")
List_r = Listbox(root, width=50, height=10,background="#00FFAB")


# my_listbox = Listbox(root)
# my_listbox.pack(pady=25)

def open():
    # global my_listbox
    global original_Name
    global fileN
    global List_l
    global dict12

    # clear1
    List_l.delete(0,END)
    List_r.delete(0,END)

    filename = filedialog.askopenfilenames(initialdir='/kinter/images',title="select a file",
                                                filetypes=(("PDF files","*.PDF"),("All files","*")))

    # my_label = Label(root,text= filename)
    # my_label.pack()

    fileN = list(filename) 
    original_Name=[]

    for i in fileN:
        original_Name.append(os.path.basename(i))
    
    dict12 = dict(zip(original_Name,fileN))

    for i in original_Name:
        List_l.insert(END,i)

def MoveTo(fromList,toList):
    index_list = fromList.curselection()
    if index_list:
        index = index_list[0] 
        val = fromList.get(index)
        fromList.delete(index)
        toList.insert(END,val)


def select():
    my_label.config(text=List_l.get(ANCHOR))
    
    
def delete():
    List_l.delete(ANCHOR)
    my_label.config(text="")

def clear1():
    List_l.delete(0,END)

def merge_pdf():
    global to_be_merge
    global merger
    global new_list

    to_be_merge =list(List_r.get(0,END))

    if len(to_be_merge)>=2:
        new_list=[]
        for list1 in to_be_merge:
            new_list.append(dict12[list1])

        print(new_list)

        merger = PdfFileMerger()

        for pdf in new_list:
            merger.append(pdf)

        merger.write("result.pdf")
        merger.close()



frame = Frame(root)

b1 = Button(frame, text=">",command=lambda: MoveTo(List_l,List_r))
b2 = Button(frame, text="<",command=lambda: MoveTo(List_r,List_l))
b3 = Button(frame, text="Merge",command=merge_pdf).pack()

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