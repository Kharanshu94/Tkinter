from tkinter import *

root = Tk()

List_l = Listbox(root, width=50, height=10,background="#92B4EC")
List_r = Listbox(root, width=50, height=10,background="#00FFAB")


for i in "KHARANSHU":
    List_l.insert(END," "+ i +" ")

def MoveTo(fromList,toList):
    index_list = fromList.curselection()
    if index_list:
        index = index_list[0] 
        val = fromList.get(index)
        fromList.delete(index)
        toList.insert(END,val)

frame = Frame(root)

b1 = Button(frame, text=">",command=lambda: MoveTo(List_l,List_r))
b2 = Button(frame, text="<",command=lambda: MoveTo(List_r,List_l))

b1.pack(side="top")
b2.pack(side="bottom")

List_l.pack(side = "left")
frame.pack(side = "left")
List_r.pack(side = "left")

root.mainloop()
