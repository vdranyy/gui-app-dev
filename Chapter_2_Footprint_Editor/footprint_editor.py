from Tkinter import *
from tkFileDialog import *
import os

file_name = None


def new_file(event=None):
    root.title('Untitled')
    global file_name
    file_name = None
    content_text.delete(1.0, END)


def open_file(event=None):
    input_file_name = askopenfilename(
        defaultextension='.txt',
        filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')]
    )
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
        content_text.delete(1.0, END)
        with open(file_name) as _file:
            content_text.insert(1.0, _file.read())


def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return 'break'


def save_as(event=None):
    input_file_name = asksaveasfilename(
        defaultextension='*.txt',
        filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')]
    )
    if input_file_name:
        global file_name
        file_name = input_file_name
        write_to_file(file_name)
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
    return 'break'


def write_to_file(file_name):
    try:
        content = content_text.get(1.0, END)
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass # pass for now but we show some warnings - we do this in next iteration


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


def find_text(event=None):
    search_toplevel = Toplevel(root)
    search_toplevel.title('Find Text')
    search_toplevel.transient(root)
    search_toplevel.resizable(False, False)
    Label(search_toplevel, text='Find All:',).grid(row=0, column=0, sticky=E)
    search_entry_widget = Entry(search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(search_toplevel, text='Ignore Case', variable=ignore_case_value).grid(
        row=1, column=1, sticky=E, padx=2, pady=2
    )
    Button(
        search_toplevel,
        text='Find All',
        underline=0,
        command=lambda: search_output(
            search_entry_widget.get(),
            ignore_case_value.get(),
            content_text, search_toplevel,
            search_entry_widget
        )
    ).grid(row=0, column=2, sticky='ew', padx=2, pady=2)
    
    def close_search_window():
        content_text.tag_remove('match', '1.0', END)
        search_toplevel.destroy()
    search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
    return 'break'


def search_output(needle, if_ignore_case, content_text, search_toplevel, search_box):
    content_text.tag_remove('match', '1.0', END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle, start_pos, nocase=if_ignore_case, stopindex=END)
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
        content_text.tag_config(
            'match',
            foreground='red',
            background='yellow'
        )
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))


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
    command=new_file
)

file_menu.add_command(
    label='Open',
    accelerator='Ctrl+O',
    compound='left',
    underline=0,
    command=open_file
)

file_menu.add_command(
    label='Save',
    accelerator='Ctrl+S',
    compound='left',
    underline=0,
    command=save
)

file_menu.add_command(
    label='Save as',
    accelerator='Shift+Ctrl+S',
    compound='left',
    command=save_as
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
    command=find_text
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
content_text.bind('<Control-f>', find_text)
content_text.bind('<Control-F>', find_text)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-s>', save)
content_text.bind('<Control-S>', save)
content_text.bind('<Shift-Control-s>', save_as)
content_text.bind('<Shift-Control-S>', save_as)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-N>', new_file)
content_text.pack(expand='yes', fill='both')

scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill=Y)

root.mainloop()
