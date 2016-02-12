from Tkinter import *

def cut():
    content_text.event_generate('<<Cut>>')


def copy():
    content_text.event_generate('<<Copy>>')


def paste():
    content_text.event_generate('<<Paste>>')


def undo():
    content_text.event_generate('<<Undo>>')


def redo(event=None):
    content_text.event_generate('<<Redo>>')
    return 'break'


def select_all(event=None):
    content_text.tag_add('sel', '1.0', 'end')
    return 'break'


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
    command=undo
)

edit_menu.add_command(
    label='Redo',
    accelerator='Ctrl+Y',
    compound='left',
    command=redo
)

edit_menu.add_separator()

edit_menu.add_command(
    label='Cut',
    accelerator='Ctrl+X',
    compound='left',
    command=cut
)

edit_menu.add_command(
    label='Copy',
    accelerator='Ctrl+C',
    compound='left',
    command=copy
)

edit_menu.add_command(
    label='Paste',
    accelerator='Ctrl+V',
    compound='left',
    command=paste
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
    command=select_all
)

view_menu = Menu(menu_bar, tearoff=0)
# All view menu goes down here
menu_bar.add_cascade(label='View', menu=view_menu)

view_menu.add_checkbutton(
    label='Show Line Number',
    #variable=show_line_no
)

view_menu.add_checkbutton(
    label='Show Cursor Location at Bottom',
    #variable=cursor_bottom
)

view_menu.add_checkbutton(
    label='Highlight Current Line',
    #variable=highlight_line
)

themes_menu = Menu(view_menu, tearoff=0)
view_menu.add_cascade(label='Themes', menu=themes_menu)

themes_menu.add_radiobutton(
    label='Aquamarine',
    #variable=theme_name
)

themes_menu.add_radiobutton(
    label='Bold Beige',
    #variable=theme_name
)

themes_menu.add_radiobutton(
    label='Cobalt Blue',
    #variable=theme_name
)

themes_menu.add_radiobutton(
    label='Default',
    #variable=theme_name
)

themes_menu.add_radiobutton(
    label='Greygarious',
    #variable=theme_name
)

themes_menu.add_radiobutton(
    label='Night Mode',
    #variable=theme_name
)

themes_menu.add_radiobutton(
    label='Olive Green',
    #variable=theme_name
)

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

# Frame widget to hold the shortcut icons
shortcut_bar = Frame(root, height=25, background='light sea green')
shortcut_bar.pack(expand='no', fill=X)

# Text widget to hold line numbers
line_number_bar = Text(
    root,
    width=4,
    padx=3,
    takefocus=0,
    border=0,
    background='khaki',
    state='disabled',
    wrap='none'
)
line_number_bar.pack(side='left', fill=Y)

# Main Text widget and Scrollbar
content_text = Text(root, wrap='word', undo=True)
content_text.bind('<Control-y>', redo) # handling Ctrl + smallcase y
content_text.bind('<Control-Y>', redo) # handling Ctrl + uppercase y
content_text.bind('<Control-a>', select_all)
content_text.bind('<Control-A>', select_all)
content_text.pack(expand='yes', fill='both')

scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill=Y)

root.mainloop()
