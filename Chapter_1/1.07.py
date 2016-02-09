from Tkinter import *

parent = Tk()
parent.title('Find & Replace')

Label(parent, text="Find:").grid(row=0, column=0, sticky=E)
Entry(parent, width=60).grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=9)

Label(parent, text="Replace:").grid(row=1, column=0, sticky=E)
Entry(parent).grid(row=1, column=1, padx=2, pady=2, sticky='we', columnspan=9)

Button(parent, text="Find").grid(
    row=0, column=10, sticky=EW, padx=2, pady=22
)
Button(parent, text="Find All").grid(
    row=1, column=10, sticky=EW, padx=2
)
Button(parent, text="Replace").grid(
    row=2, column=10, sticky=EW, padx=2
)
Button(parent, text="Replace All").grid(
    row=3, column=10, sticky=EW, padx=2
)
Checkbutton(parent, text="Match whole word only").grid(
    row=2, column=1, columnspan=4, sticky=W
)
Checkbutton(parent, text="Match Case").grid(
    row=3, column=1, columnspan=4, sticky=W
)
Checkbutton(parent, text="Wrap Around").grid(
    row=4, column=1, columnspan=4, sticky=W
)
Label(parent, text="Direction:").grid(
    row=2, column=6, sticky=W
)
Radiobutton(parent, text="Up", value=1).grid(
    row=3, column=6, columnspan=6, sticky=W
)
Radiobutton(parent, text="Down", value=2).grid(
    row=3, column=7, columnspan=2, sticky=E
)
parent.mainloop()
