import ctypes
import os
import requests
import time

url = "https://www.dropbox.com/scl/fi/yqv9uxkovv53bemxssav9/bruh.jpg?rlkey=2u7ldyutirqq1z2j7x3fxh2oj&st=0dy4w0sr&dl=1"

# Path to the image you want to set as the background
folder = r"C:\Users\Public"

image_path = r"C:\Users\Public\bruh.png"

response = requests.get(url)

with open(image_path, 'wb') as f:
        f.write(response.content)

# Function to set the desktop background
def set_desktop_background(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

# Set the desktop background
set_desktop_background(image_path)

# Wait for 5 seconds before shutting down
time.sleep(2)

# Shut down the computer
os.system("shutdown /s /t 1")