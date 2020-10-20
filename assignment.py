#! python3
import pyautogui as p
import time as t

doLoop = True
count = 0

while doLoop:
    p.click(1100,478)
    count=count+1
    if count==50:
        count==0
        while p.pixelMatchesColor(1739,760,(100,249,100),tolerance=10):
            p.click(1739,760)
        while p.pixelMatchesColor(1737,701,(100,249,100),tolerance=10):
            p.click(1737,701)
        while p.pixelMatchesColor(1730,647,(100,249,100),tolerance=10):
            p.click(1730,647)
        while p.pixelMatchesColor(1730,578,(100,249,100),tolerance=10):
            p.click(1730,578)
        while p.pixelMatchesColor(1721,515,(100,249,100),tolerance=10):
            p.click(1721,515)
        while p.pixelMatchesColor(1735,447,(100,249,100),tolerance=10):
            p.click(1735,447)
        while p.pixelMatchesColor(1745,391,(100,249,100),tolerance=10):
            p.click(1745,391)
        doLoop = False
        

