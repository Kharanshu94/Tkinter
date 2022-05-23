from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from PyPDF2 import PdfFileMerger,PdfFileReader


root = Tk()
root.title("Kharanshu")
root.geometry("400x400")

def open():
    # global my_listbox
    global original_Name
    global fileN
    global List_l
    global dict12

    # clear1
    List_l.delete(0,END)

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

def merge_pdf():
    global to_be_merge
    global merger
    global new_list

    to_be_merge =list(List_l.get(0,END))

    if len(to_be_merge)>=2:
        new_list=[]
        for list1 in to_be_merge:
            new_list.append(dict12[list1])

        print(new_list)

        merger = PdfFileMerger()

        for pdf in new_list:
            merger.append(pdf)

        merger.write("./result.pdf")
        merger.close()


List_l = Listbox(root, width=50, height=10,background="#92B4EC")
List_l.pack()

my_btn = Button(root, text="open file",command=open).pack()
b3 = Button(root, text="Merge",command=merge_pdf).pack()


root.mainloop()
