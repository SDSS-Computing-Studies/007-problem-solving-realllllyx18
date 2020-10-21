#! python3
import pyautogui as p

doLoop = True
count = 0

while doLoop:
    p.click(1100,478)
    count=count+1
    if count==50:
        count=0
        while p.pixelMatchesColor(1679,999,(255,255,255),tolerance=10):
            p.click(1679,999)
        while p.pixelMatchesColor(1676,935,(255,255,255),tolerance=10):
            p.click(1676,935)
        while p.pixelMatchesColor(1674,876,(255,255,255),tolerance=10):
            p.click(1674,876)
        while p.pixelMatchesColor(1678,805,(255,255,255),tolerance=10):
            p.click(1678,805)
        while p.pixelMatchesColor(1676,741,(255,255,255),tolerance=10):
            p.click(1676,741)
        while p.pixelMatchesColor(1674,682,(255,255,255),tolerance=10):
            p.click(1674,682)
        while p.pixelMatchesColor(1674,616,(255,255,255),tolerance=10):
            p.click(1674,616)
    
        
        

