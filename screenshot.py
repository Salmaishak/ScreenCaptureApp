import time
import tkinter as tk

import pyautogui as pag



def screenshot():
    name= int(round(time.time())*1000) #get the time and round it up
    name = 'D:/Python Projectss/ScreenShot-App/Screenshots Images/{}.png'.format(name) #get the random number we generate it and pass it in the {}
    time.sleep(3) #wait for a while before taking a screenshot
    img = pag.screenshot(name) #built-in function to take screenshots
    img.show()




#creates a screen

r = tk.Tk()
button1= tk.Button(r, text="Take Screenshot", command=screenshot)
button1.pack(side= tk.LEFT)
button2= tk.Button(r, text="Quit",command=quit)
button2.pack(side= tk.RIGHT)

r.mainloop()
