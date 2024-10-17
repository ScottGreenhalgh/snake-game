import york_graphics as g
from graphics import GraphicsError

def safeGetMousePos():
  try:
    return g.waitForMouseClick()
  except:
    quit()

def relativePos(start, end):
  startX, startY = start
  endX, endY = end
  return (endX - startX, endY - startY)

def drawLine(line):
  lineX, lineY = line
  g.drawLine(lineX, lineY)

def drawTriangle(triangle):
  startX, startY = triangle[0]
  g.moveTo(startX, startY)
  drawLine(relativePos(triangle[0], triangle[1]))
  drawLine(relativePos(triangle[1], triangle[2]))
  drawLine(relativePos(triangle[2], triangle[0]))

def waitAndClose():
  try:
      g.waitForMouseClick()
  except GraphicsError:
      pass
  g.closeWindow()

def getUserInputPoints(num):
  points = []
  for i in range(num):
    points.append(safeGetMousePos())
  return tuple(points)

def main():
  g.openWindow()
  triangle = getUserInputPoints(3)
  drawTriangle(triangle)
  g.updateCanvas()
  waitAndClose()

if __name__ == "__main__":
  main()