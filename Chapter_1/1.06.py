from Tkinter import *

root = Tk()
Label(root, text="Username").grid(row=0, sticky=W)
Label(root, text="Password").grid(row=1, sticky=W)
Entry(root).grid(row=0, column=1, sticky=E, padx=2, pady=2)
Entry(root).grid(row=1, column=1, sticky=E, padx=2, pady=2)
Button(root, text="Login").grid(row=2, column=1, sticky=E)
root.mainloop()
