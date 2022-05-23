import tkinter as tk
from PIL import ImageTk, Image
import tkinter.filedialog as fd

root = tk.Tk()
# filez = fd.askopenfilenames(parent=root, title='Choose a file')


def open():
    global my_image
    filename = fd.askopenfilenames(initialdir='/kinter/images',title="select a file",
                                                filetypes=(("PNG files","*.png"),("All files","*")))

    my_label = tk.Label(root,text= filename)
    my_label.pack()

    my_image = ImageTk.PhotoImage(Image.open(filename))
    my_image_label = tk.Label(image=my_image).pack()



my_btn = tk.Button(root, text="open file",command=open).pack()

# print(filez)
root.mainloop()