from Tkinter import *
root = Tk()

frame = Frame(root)

# demo of side and fill options
Label(frame, text="Pack Demo of side and fill").pack()
Button(frame, text="A").pack(side=LEFT, fill=Y)
Button(frame, text="B").pack(side=TOP, fill=X)
Button(frame, text="C").pack(side=RIGHT, fill=NONE)
Button(frame, text="D").pack(side=TOP, fill=BOTH)
frame.pack()
# the top frame doesn't expand nor does it fill in

# X or Y directions

Label(root, text="Pack Demo of expand").pack()
Button(root, text="I do not expand").pack()
Button(root, text="I do not fill X but I expand").pack(expand=1, fill=NONE)
Button(root, text="I fill X and expand").pack(expand=1, fill=X)
root.mainloop()
