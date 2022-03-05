# Import Module
from tkinter import *
from download import Wallpaper
from set_wallpaper import download_path

# create root window
root = Tk()

# root window title and dimension
root.title("Wallsy")

# Set geometry (widthxheight)
root.geometry('350x200')


# submit button function
def submit():
    keywords = keyword_var.get().split(',')
    Wallpaper(path=download_path, keyword=keywords[0]).download()


# all widgets will be here
# Execute Tkinter
keyword_var = StringVar()
keyword_widget = Entry(root, textvariable=keyword_var, font=('calibre', 10, 'normal'), width=50)
sub_btn = Button(root, text='Download', command=submit)

keyword_widget.grid(row=0, column=1)
sub_btn.grid(row=3, column=1)

root.mainloop()
