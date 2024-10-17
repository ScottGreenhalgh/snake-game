import york_graphics as g
from graphics import GraphicsError
board = [
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
size = 40
minimum = 2

def main():
    setupCanvas()
    drawPixelImage(board)
    food(board, minimum)
    waitAndClose()

def setupCanvas():
    g.openWindow()
    g.setLineThickness(size)

def waitAndClose():
    try:
        g.waitForMouseClick()
    except GraphicsError:
        pass
    g.closeWindow()
 
def drawPixelImage(image):
    for y, row in enumerate(image):
        for x, val in enumerate(row):
            drawBox(x, y, val)
    g.updateCanvas()

def drawBox(xPos, yPos, colour):
    print "Coordinate ({}, {}) contains value {}".format(xPos, yPos, colour)
    if colour == 0:
        g.setLineColour("white")
    elif colour == 2:
        g.setLineColour("red")
    else:
        g.setLineColour("black")
    g.moveTo(xPos*size, yPos*size)
    g.drawLine(size, 0)

def food(board, minimum):
    print(min(board))
    if min(board) >= minimum:
        print "All values are equal or above", minimum
    else:
        print "Not all values are equal or above", minimum
    
if __name__ == "__main__":
    main()
