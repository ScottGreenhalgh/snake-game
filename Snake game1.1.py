from york_graphics import*
from time import*

openWindow(500,500)
x = 10
y = 10
speed = 1

Array =[[0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]


moveTo(50,50)
setLineThickness(10)

for y in range(len(Array)):
        
    for x in range(len(Array[y])):
        moveTo(50*y+10*x,50)
        print(Array[y][x])
        if Array[y][x]==1:
            setLineColour("BLACK")
            drawLine(10,0)
            updateCanvas()
##while(1):       
##    def_Right(x,y):
##        self.x = self.x + self.speed
##        drawLine(20,0)
##        updateCanvas()
##    def_Left(x,y):
##        self.x = self.x - self.speed
##        drawLine()20,0)
##        updateCanvas()
##     
##    def_Up(x,y):
##        self.y = self.y - self.speed
##        drawLine(20,0)
##        updateCanvas()
##    def_Down(x,y):
##        self.y = self.y + self.speed
    #drawLine(20,0)
    #updateCanvas()
 
##class App:
## 
##    windowWidth = 50
##    windowHeight = 50
##    player = 0
##    print player
##    
 
