#! python3
import pyautogui as p
import time as t

doLoop = True
count = 0

while doLoop:
    p.click(1100,478)
    count=count+1
    if count == 50:
        p.Moveto(1745,391)
        p.Moveto(1735,447)
        p.Moveto(1721,515)
        p.Moveto(1730,578)
        p.Moveto()
            doLoop = False
        

