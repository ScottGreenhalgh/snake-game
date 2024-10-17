import york_graphics as g
from graphics import GraphicsError

def main():
    g.openWindow()
    pos1 = g.waitForMouseClick()
    pos2 = g.waitForMouseClick()
    pos3 = g.waitForMouseClick()
    drawTriangle(pos1, pos2, pos3)
    
def drawTriangle(pos1, pos2, pos3):
    g.moveTo(pos1[0], pos1[1])
    line2x = pos2[0]-pos1[0]
    line2y = pos2[1]-pos1[1]
    g.drawLine(line2x, line2y)
    line3x = pos3[0]-pos2[0]
    line3y = pos3[1]-pos2[1]
    g.drawLine(line3x, line3y)
    line4x = pos1[0]-pos3[0]
    line4y = pos1[1]-pos3[1]
    g.drawLine(line4x, line4y)
    g.updateCanvas()
    waitAndClose()

def waitAndClose():
    try:
        g.waitForMouseClick()
    except GraphicsError:
        pass
    g.closeWindow()

if __name__ == "__main__":
    main()