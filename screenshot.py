import time
import tkinter as tk
import pyautogui as pag
import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab

def screenshot():
    name= int(round(time.time())*1000) #get the time and round it up
    name = 'D:/Python Projectss/ScreenShot-App/Screenshots Images/{}.png'.format(name) #get the random number we generate it and pass it in the {}
    time.sleep(3) #wait for a while before taking a screenshot
    img = pag.screenshot(name) #built-in function to take screenshots
    img.show()
SCREEN_SIZE= tuple(pyautogui.size())
def screenRecorder():
    fourcc = cv2.VideoWriter_fourcc(*'XVID') #create a video writer object
    out=cv2.VideoWriter('output.avi', fourcc,5.0,(SCREEN_SIZE) )
    while True:
        img = pyautogui.screenshot()
        img_np = np.array(img)
        frame =cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow("screen recorder",frame)
        out.write(img_np)

        if cv2.waitKey(1)==ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()


#creates a screen

r = tk.Tk()
button1= tk.Button(r, text="Take Screenshot", command=screenshot)
button1.pack(side= tk.LEFT)
button2= tk.Button(r, text="Quit",command=quit)
button2.pack(side= tk.RIGHT)
button3 = tk.Button(r,text="Screen Recorder", command=screenRecorder)
button3.pack()

r.mainloop()
