from download import Wallpaper
import ctypes
import os
import random

user = os.getlogin()
root = f"C:\\Users\\{user}\\Documents\\"
path = "wallpaper"
os.chdir(root)
if os.path.isdir(path):
    pass
else:
    os.mkdir(path)

Wallpaper().download()

backgrounds = []
for root, directories, files in os.walk(os.path.join(path)):
    backgrounds = [file.lower() for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]

# ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{path}/{random.choice(backgrounds)}", 0)
