from Tkinter import *

root = Tk()
root.configure(background="#4D4D4D") # top level styling

# connection to external styling optionDB.txt
root.option_readfile('optionDB.txt')

# widget specific styling
mytext = Text(root, background="#101010", foreground="#D6D6D6", borderwidth=18, relief="sunken", width=17, height=5)
mytext.insert(END, "Style is knowing who you are, what you want to say, and not giving a damn.")
mytext.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

# all the below widgets derive their styling from optionDB.txt file
Button(root, text='*').grid(row=1, column=1)
Button(root, text='^').grid(row=1, column=2)
Button(root, text='#').grid(row=1, column=3)
Button(root, text='<').grid(row=2, column=1)
Button(root, text='OK', cursor='target').grid(row=2, column=2) #changing cursor style
Button(root, text='>').grid(row=2,column=3)
Button(root, text='+').grid(row=3, column=1)
Button(root, text='v').grid(row=3, column=2)
Button(root, text='-').grid(row=3, column=3)
for i in range(9):
    Button(root, text=str(i+1)).grid(row=4+i//3, column=1+i%3)

root.mainloop()
