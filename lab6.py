import york_graphics as g
from graphics import GraphicsError
myImage = [
  [0,0,0,0,0,0,0,0],
  [0,1,1,0,0,1,1,0],
  [0,1,1,0,0,1,1,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,1,0,0,0,0,1,0],
  [0,1,1,1,1,1,1,0],
  [0,0,0,0,0,0,0,0]
]
size = 75

def main():
    setupCanvas()
    drawPixelImage(myImage)
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
            drawSquare(x, y, val)
    g.updateCanvas()

def drawSquare(xPos, yPos, colour):
    print "Coordinate ({}, {}) contains value {}".format(xPos, yPos, colour)
    if colour == 0:
        g.setLineColour("white")
    else:
        g.setLineColour("black")
    g.moveTo(xPos*size, yPos*size)
    g.drawLine(size, 0)

if __name__ == "__main__":
    main()