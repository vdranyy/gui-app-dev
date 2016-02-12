from Tkinter import *


root = Tk()

PROGRAM_NAME = "Footprint Editor"

root.title(PROGRAM_NAME)

# Adding Menubar in the widget
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
# All file menu goes down here
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(
    label='New',
    accelerator='Ctrl+N',
    compound='left',
    underline=0,
    #command=new_file
)

file_menu.add_command(
    label='Open',
    accelerator='Ctrl+O',
    compound='left',
    underline=0,
    #command=open_file
)

file_menu.add_command(
    label='Save',
    accelerator='Ctrl+S',
    compound='left',
    underline=0,
    #command=save_file
)

file_menu.add_command(
    label='Save as',
    accelerator='Shift+Ctrl+S',
    compound='left',
    #command=save_file_as
)

file_menu.add_separator()

file_menu.add_command(
    label='Exit',
    accelerator='Alt+F4',
    compound='left',
    #command=exit_file
)

edit_menu = Menu(menu_bar, tearoff=0)
# All edit menu goes down here
menu_bar.add_cascade(label='Edit', menu=edit_menu)

edit_menu.add_command(
    label='Undo',
    accelerator='Ctrl+Z',
    compound='left',
    #command=undo
)

edit_menu.add_command(
    label='Redo',
    accelerator='Ctrl+Y',
    compound='left',
    #command=redo
)

edit_menu.add_separator()

edit_menu.add_command(
    label='Cut',
    accelerator='Ctrl+X',
    compound='left',
    #command=cut
)

edit_menu.add_command(
    label='Copy',
    accelerator='Ctrl+C',
    compound='left',
    #command=copy
)

edit_menu.add_command(
    label='Paste',
    accelerator='Ctrl+V',
    compound='left',
    #command=paste
)

edit_menu.add_separator()

edit_menu.add_command(
    label='Find',
    accelerator='Ctrl+F',
    compound='left',
    underline=0,
    #command=find
)

edit_menu.add_separator()

edit_menu.add_command(
    label='Select All',
    accelerator='Ctrl+A',
    compound='left',
    underline=7,
    #command=select_all
)

view_menu = Menu(menu_bar, tearoff=0)
# All view menu goes down here
menu_bar.add_cascade(label='Edit', menu=view_menu)

about_menu = Menu(menu_bar, tearoff=0)
# All about menu goes down here
menu_bar.add_cascade(label='About', menu=about_menu)

about_menu.add_command(
    label='About',
    compound='left',
    #command=about
)

about_menu.add_command(
    label='Help',
    compound='left',
    #command=help
)

root.config(menu=menu_bar)

root.mainloop()
