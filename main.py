import time

import keyboard
import mouse
import pyautogui
from PIL import Image


image = Image.open("img.png")
image.rotate(angle=90)
img = image.load()
w, h =image.size
keyboard.wait("w")

xB, yB = 1717, 178

for k in range(0, 25):
    #loc = pyautogui.locateOnScreen('button.png')

    #point = pyautogui.center(loc)
    #pX, pY = point
    mouse.move(xB, yB)
    mouse.click()

    time.sleep(0.01)
    '''
    for l in range(0, 12):
        keyboard.press("tab")
        time.sleep(0.01)
        keyboard.release("tab")
        time.sleep(0.01)
    time.sleep(0.01)
    #keyboard.press("shift+tab")
    time.sleep(0.01)
    #keyboard.release("shift+tab")
    time.sleep(0.01)
    '''


    #mouse.move(1716, 180)
    #mouse.click()
    time.sleep(0.01)
    for l in range(0, 6):
        keyboard.press("tab")
        time.sleep(0.01)
        keyboard.release("tab")
        time.sleep(0.01)

    for l in range(0, 3):
        time.sleep(0.01)
        keyboard.press('Ctrl+a')
        time.sleep(0.01)
        keyboard.release('Ctrl+a')
        time.sleep(0.01)
        s = str(k*10)
        keyboard.write(s)

        time.sleep(0.1)

        keyboard.press("tab")
        time.sleep(0.01)
        keyboard.release("tab")
        time.sleep(0.01)

    for l in range(0, 3):
        keyboard.press("tab")
        time.sleep(0.01)
        keyboard.release("tab")
        time.sleep(0.01)

    keyboard.press("enter")
    keyboard.release("enter")
    for j in range(0, h):

        for i in range(0, w):
            r, g, b = img[i, j]
            d = (r + g + b) / 3
            if abs(d - k * 10) <= 5:
                mouse.move(i+400, j+400)
                #time.sleep(0.001)
                mouse.click()
                time.sleep(0.001)


        if(keyboard.is_pressed('q')):
            exit()


    #keyboard.wait('f')


