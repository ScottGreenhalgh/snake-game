from york_graphics import *
openWindow()
def triangle(t1,t2,t3,t4,t5,t6):
   moveTo(t1,t2)
   drawLine(t3,t4)
   drawLine(t5,t6)
triangle(100, 100, 200, 200, 0, 300)
x, y = waitForMouseClick()
updateCanvas()
waitForMouseClick()
closeWindow()
