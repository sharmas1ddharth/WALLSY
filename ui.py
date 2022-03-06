# Import Module
from tkinter import *
from download import Wallpaper
from set_wallpaper import download_path, set
from tkinter import ttk
import random
import time
import threading

# create root window
root = Tk()
root.resizable(width=False, height=False)
# root window title and dimension
root.title("Wallsy")

# Set geometry (widthxheight)
root.geometry('350x200')


# submit button function

# def download():
#     keywords = keyword_var.get().split(',')
#     keyword_arg = "background"
#     if len(keywords) > 1:
#         keyword_arg = keywords[0]
#
#     json_result = Wallpaper(path=download_path, keyword=keyword_arg).get_json()
#     # print(json_result)
#     page_n = random.randint(0, json_result['total_results'] + 1)
#     Wallpaper(path=download_path, keyword=keyword_arg, page_num=page_n).download()
#     return download


def progress_():
    progress = ""
    while True:
        status = download()
        if status == "":
            progress = "Downloading..."
            continue

        else:
            progress = "Download Complete"
            break

    return progress


def submit():
    keywords = keyword_var.get().split(',')
    keyword_arg = "background"
    if len(keywords) > 1:
        keyword_arg = keywords[0]

    json_result = Wallpaper(path=download_path, keyword=keyword_arg).get_json()
    page_n = random.randint(0, json_result['total_results'] + 1)
    Wallpaper(path=download_path, keyword=keyword_arg, page_num=page_n).download()
    set()


# all widgets will be here
# Execute Tkinter
keyword_var = StringVar()
# lbl = Label(root, text=progress_())
keyword_widget = Entry(root, textvariable=keyword_var, font=('calibre', 10, 'normal'), width=47)
sub_btn = Button(root, text='Download', command=threading.Thread(target=submit).start())

# lbl.place(x=170, y=40)
keyword_widget.place(x=10, y=10)
sub_btn.place(x=140, y=40)

root.mainloop()
