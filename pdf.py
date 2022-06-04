# Import module
from tkinter import *
# from PIL import ImageTk, Image
from tkinter import filedialog
import os
from PyPDF2 import PdfFileMerger
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile


# Create object
root = Tk()

# Adjust size
root.geometry("604x400+300+100")
root.iconbitmap(".\WelPDF.ico")
root.title(" Welspun PDF COMPILER")
root. resizable(width=False, height=False)
# root.configure(bg='')


#--------------------------Save Files----------------------------

def save_file():
    global f
    f = asksaveasfile(initialfile = 'Merged',
        defaultextension=".pdf",filetypes=[("PDF Documents","*.PDF"),("All Files","*.*")])
    

#--------------------------Open Dialogbox Files----------------------------
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

#--------------------------MoveTo Functions----------------------------
def MoveTo(fromList,toList):
    index_list = fromList.curselection()
    if index_list:
        index = index_list[0] 
        val = fromList.get(index)
        fromList.delete(index)
        toList.insert(END,val)

#--------------------------Select Functions----------------------------
def select():
    my_label.config(text=List_l.get(ANCHOR))
    
#--------------------------Delete Functions----------------------------   
def delete():
    List_l.delete(ANCHOR)
    my_label.config(text="")

#--------------------------Clear Functions----------------------------  
def clear1():
    List_l.delete(0,END)

#--------------------------Merge Functions----------------------------
def merge_pdf():
    global to_be_merge
    global merger
    global new_list

    to_be_merge =list(List_r.get(0,END))


    if len(to_be_merge)>=2:
        new_list=[]
        for list1 in to_be_merge:
            new_list.append(dict12[list1])

        # print(new_list)

        save_file()
        # print(f)

        merger = PdfFileMerger()

        for pdf in new_list:
            merger.append(pdf)

        merger.write(f.name)
        merger.close()
        messagebox.showinfo("Done", "PDFs Compiled")
        # List_l.delete(0,END)
        List_r.delete(0,END)
    else:
        messagebox.showinfo("Select More than 2 PDF Files", "Error")


# Add image file
bg = PhotoImage(file = ".\Main_Frame.png")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

#----------------------Creating CLEAR Button-----------------------
clear_btn = PhotoImage(file=".\CLEAR.png")
CLEAR1 = Button(root,image=clear_btn,borderwidth=0,bg="#555454",
                height=35,width=80,anchor="center",activebackground='#01D1FF',
                command=clear1)
CLEAR1.place(relx = 0.162, rely = 0.81,anchor="center")

#----------------------Creating DELETE Button-----------------------
delete_btn = PhotoImage(file=".\DELETE.png")
DELETE1 = Button(root,image=delete_btn,borderwidth=0,bg="#555454",
                height=35,width=80,anchor="center",activebackground='#01D1FF',
                command=delete)
DELETE1.place(relx = 0.34, rely = 0.81,anchor="center")

#----------------------Creating S2D Button-----------------------
s2d_btn = PhotoImage(file=".\S2D.png")
S2D1 = Button(root,image=s2d_btn,borderwidth=0,bg="#555454",
                height=40,width=40,anchor="center",activebackground='#01D1FF',
                command=lambda: MoveTo(List_l,List_r))
S2D1.place(relx = 0.5, rely = 0.5,anchor="center")

#----------------------Creating D2S Button-----------------------
d2s_btn = PhotoImage(file=".\D2S.png")
D2S1 = Button(root,image=d2s_btn,borderwidth=0,bg="#555454",
                height=40,width=40,anchor="center",activebackground='#01D1FF',
                command=lambda: MoveTo(List_r,List_l))
D2S1.place(relx = 0.5, rely = 0.6,anchor="center")

#----------------------Creating IMPORT Button-----------------------
import_btn = PhotoImage(file=".\IMPORT.png")
IMPORT1 = Button(root,image=import_btn,borderwidth=0,bg="#555454",
                height=22,width=465,anchor="center",activebackground='#01D1FF',
                command=open)
IMPORT1.place(relx = 0.49, rely = 0.18,anchor="center")

#----------------------Creating MERGED Button-----------------------
merge_btn = PhotoImage(file=".\MERGE.png")
MERGE1 = Button(root,image=merge_btn,borderwidth=0,bg="#555454",
                height=35,width=80,anchor="center",activebackground='#01D1FF',
                command=merge_pdf)
MERGE1.place(relx = 0.762, rely = 0.81,anchor="center")

# try_btn = Button(root, text="CLEAR",borderwidth=0,height=3,width=7)
# try_btn.place(relx = 0.5, rely = 0.525, anchor="center")

List_l = Listbox(root, width=35, height=11,background="#827E7E",borderwidth=0,fg="#FFFFFF")
List_r = Listbox(root, width=35, height=11,background="#827E7E",borderwidth=0,fg="#EBF000")
# List_l.config(font=bolded)
# List_r.config(font=bolded)

List_l.place(relx = 0.25, rely = 0.525, anchor="center")
List_r.place(relx = 0.75, rely = 0.525, anchor="center")

global my_label

my_label = Label(root,text='',background="#555454")
# my_label.pack(pady=5)
my_label.place(relx = 0.5, rely = 0.725)

root.mainloop()
