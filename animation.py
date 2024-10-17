#######################################
#                                     #
#    Introduction to Programming      #
#                Lab 4                #
#                                     #
#              Animation              #
#                                     #
#        Author: Samuel Bourke        #
#   Email: samuel.bourke@york.ac.uk   #
#                                     #
#  This program animated a square     #
#  moving across a screen, bouncing   #
#  each edge.                         #
#                                     #
#######################################

# Import relevant packages. york_graphics handles the
# graphics functions, time is used to delay the update of
# the canvas.
from york_graphics import *
from time import *

openWindow()

# Set initial positions and velocities.
xPos=20
yPos=200
xVelocity = 10
yVelocity = 5

# Set the properties of the box
setLineThickness(50)
setLineColour("red")

# While(1) is a loop that will continue forever.
while(1):
    
    clearCanvas()

    # Update the position of the box based on it's x and y velocities.
    xPos+=xVelocity
    yPos+=yVelocity

    # Move to the new position and redraw the box
    moveTo(xPos,yPos)
    drawLine(100,0)

    # Update the canvas and wait for 2 milliseconds.
    updateCanvas()
    sleep(0.002)

    # If the box hits a wall, reverse the velocity in the appropriate direction.
    if xPos > 700 or xPos<0:
        xVelocity *= -1
    if yPos > 575 or yPos<25:
        yVelocity *= -1
