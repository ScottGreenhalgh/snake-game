import york_graphics as g
from graphics import GraphicsError, Text
from random import randint
from time import sleep
from math import floor

size = (600, 600)
thickness = 20
snake = [(1, 1)]
shouldDraw = True

directions = ["Up", "Right", "Down", "Left"]

def randPos(size):
  """Generate random position inside our grid
  """
  return (
    floor(randint(0, size[0])/thickness),
    floor(randint(0, size[1])/thickness)
  )

def drawWhiteCanvas(size):
  """Draw line the size of the entire canvas, white.
  """
  thickness = max(size)
  g.setLineThickness(thickness*2)
  print(thickness)
  drawBox(0, 0, 0, thickness)

def setupCanvas():
  """Open the window
  Set the background to white
  Set the line thickness
  """
  g.openWindow(size[0], size[1], "Snake")
  drawWhiteCanvas(size)
  g.setLineThickness(thickness)

def drawBox(xPos, yPos, colour, thickness=thickness, length=0):
  """Set colour
  Move to position, with offset on Y axis because thickness applies from center
  Draw Line
  """
  if colour == 0:
    g.setLineColour("white")
  elif colour == 1:
    g.setLineColour("black")
  elif colour == 2:
    g.setLineColour("red")
  g.moveTo(
    (xPos*thickness),
    (yPos*thickness)+(thickness/2)
  )
  g.drawLine(thickness, length)

def waitAndClose():
  """Wait for mouse click
  If window is already closed, ignore exception and try close window.
  """
  try:
      g.waitForMouseClick()
  except GraphicsError:
      pass
  shouldDraw = False
  g.closeWindow()

def drawFood(food):
  """Draw box for food then updates canvas
  """
  print(food)
  drawBox(food[0], food[1], 2)

def drawFullSnake(snake):
  """Enumate over the snake and draw each piece then update canvas
  """
  for index, pos in enumerate(snake):
    drawBox(pos[0], pos[1], 1)
  g.updateCanvas()

def getInverseDirection(direction):
  if direction == "Up":
    return "Down"
  elif direction == "Right":
    return "Left"
  elif direction == "Down":
    return "Up"
  elif direction == "Left":
    return "Right"

def waitForDirection(direction):
  """If direction isn't set, wait for the keypress.
  If keypress is a direction then return key.
  Else wait for the keypress again.
  If direction is set, get most recent keypress.
  If keypress is a direction then return key.
  Else return previous direction
  """
  if not direction:
    key = g.waitForKeyPress()
    if key in directions:
      if key == getInverseDirection(direction):
        return direction
      else:
        return key
    else:
      return waitForDirection(direction)
  else:
    key = g.getKeyPress()
    if key in directions:
      if key == getInverseDirection(direction):
        return direction
      else:
        return key
    else:
      return direction

def getNewPos(direction, position, speed=1):
  """Return modified position relative to the direction of the snake.
  """
  x, y = position
  if direction == "Up":
    return (x, y - speed)
  elif direction == "Right":
    return (x + speed, y)
  elif direction == "Down":
    return (x, y + speed)
  elif direction == "Left":
    return (x - speed, y)
  else:
    return position

def moveSnake(snake, direction, grow):
  """Get tail index of the snake and the head (x, y).
  If snake isn't growing then remove the tail.
  Get new head position based on direction.
  Insert new head to the start of the snake.
  Draw new head.
  Return snake.
  """
  tailIndex = len(snake) - 1
  head = snake[0]
  if not grow:
    removed = snake.pop(tailIndex)
    drawBox(removed[0], removed[1], 0)
  newHead = getNewPos(direction, head)
  global shouldDraw
  if isColliding(newHead, snake):
    shouldDraw = False
  newHeadX, newHeadY = newHead
  if (
    newHeadX < 0 or newHeadY < 0
  ) or (
    newHeadX > (size[0]/thickness-1) or
    newHeadY > (size[1]/thickness-1)
  ):
    shouldDraw = False
  snake.insert(0, newHead)
  drawBox(newHead[0], newHead[1], 1)
  return snake

def isEating(snake, food):
  """Get snake head (x, y).
  If head (x, y) equals food (x, y)
  Return true
  Else return false
  """
  return isColliding(food, snake)

def isColliding(position, boundaries):
  """If position is in any boundary
  Return True
  Else return false
  """
  return position in boundaries

def makeFood(snake):
  """Generate random food.
  Check if food is inside snake
  Returns food (x, y)
  """
  food = randPos(size)
  if isColliding(food, snake):
    return makeFood(snake)
  else:
    return food

def drawDeathMessage():
  """Moves to the centre of the screen
  Death text placed at location
  """
  g.moveTo(size[0]/2, size[1]/2)
  g.setTextProperties(None, 36)
  g.setLineColour("blue")
  g.drawText("You died")
  g.updateCanvas()

def undrawOldScore(score):
  try:
    for i in range(0, len(g._objects)):
      if isinstance(g._objects[i], Text):
        if not g._objects[i].getText() == score:
          g._objects[i].undraw()
          del g._objects[i]
  except IndexError:
    pass

def drawScore(snake):
  score = len(snake)
  undrawOldScore(score)
  g.moveTo(size[0]-100, 100)
  g.setTextProperties(None, 36)
  g.setLineColour("blue")
  g.drawText(score)
  g.updateCanvas()

def gameLoop(snake):
  """Get food position
  draw the initial snake before starting loop
  draw the initial food before starting loop
  inside loop wait for a direction to move in
  move snake in above direction
  drawFood
  sleep for 1/20th of a second
  """
  snakePos = snake
  direction = None
  food = makeFood(snakePos)
  drawFullSnake(snakePos)
  drawFood(food)
  g.updateCanvas()
  while shouldDraw == True:
    direction = waitForDirection(direction)
    grow = isEating(snake, food)
    if grow:
      food = makeFood(snakePos)
    drawFood(food)
    snakePos = moveSnake(snakePos, direction, grow)
    drawScore(snakePos)
    sleep(1/20)
  drawDeathMessage()

def menu():
  g.moveTo(size[0]/2, size[1]/2)
  g.setTextProperties(None, 36)
  g.setLineColour("blue")
  g.drawText("Welcome to Snake")
  g.updateCanvas()

def main():
  setupCanvas()
  menu()
  gameLoop(snake)
  waitAndClose()

if __name__ == "__main__":
  main()
