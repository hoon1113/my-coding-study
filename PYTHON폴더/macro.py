import pyautogui
import keyboard
import time

while True:
    pyautogui.click(button='left', clicks=120)
    if keyboard.is_pressed('f3'):
        break