import york_graphics as g
from graphics import GraphicsError

def square(x, y, size):
    rectangle(x, y, size, size)
   
def rectangle(x, y, height, width):
    g.moveTo(x, y)
    g.drawLine(0, height)
    g.drawLine(width, 0)
    g.drawLine(0, -height)
    g.drawLine(-width, 0)

def isoscelesTriangle(x, y, height, width):
    g.moveTo(x, y)
    g.drawLine(height, -height)
    g.drawLine(height, height)
    g.drawLine(-width, 0)

def cross(x, y, size):
    g.moveTo(x + (size/2), y)
    g.drawLine(0, size)
    g.moveTo(x, y + (size/2))
    g.drawLine(size, 0)

def window(x, y, size):
    square(x, y, size)
    cross(x, y, size)

def drawHouse():
    g.openWindow()
    square(200, 200, 300)
    isoscelesTriangle(200, 200, 150, 300)
    window(250, 250, 75)
    window(375, 250, 75)
    window(250, 375, 75)
    rectangle(375, 375, 125, 75)
    g.updateCanvas()
    waitAndClose()

def waitAndClose():
    try:
        g.waitForMouseClick()
    except GraphicsError:
        pass
    g.closeWindow()

if __name__ == "__main__":
    drawHouse()
