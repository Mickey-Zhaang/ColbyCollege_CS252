'''Nicole Lin
CS151
2/13/26
shapelib.py'''

import turtle as t
import random as r
import math as m

def goto(x,y):
    print("goto(): going to", x,y)
    #print("goto(): before move, turtle at", t.position())
    
    t.setheading(0)

    t.up()
    t.goto(x,y)
    t.down()
 
    print("goto(): after move, turtle now at", t.position())


def block(x, y, width, height):
    '''Draws a block at (x,y) of the given width and height'''
    goto(x,y)
    t.speed(0)

    t.forward((1/2)*width)  # tell the turtle to go forward by width
    t.left(90)        # tell the turtle to turn left by 90 degrees
    t.forward(height) # tell the turtle to go forward by height
    t.left(90)
    t.forward(width)  # repeat the above 4 commands
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward((1/2)*width)

    print('block(): drawing block of size', width, height)


def tiltedBlock(x, y, width, height, angle):
    t.speed(0)
    t.up()
    t.goto(x,y)
    t.down()
    t.left(angle)
    t.setheading(angle)
    t.forward((1/2)*width)  
    t.left(90)        
    t.forward(height) 
    t.left(90)
    t.forward(width)  
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward((1/2)*width)


def bunchOfBlocks(x,y,scale):
    print('bunchOfBlocks(): drawing blocks at location',x,y)

    # put several calls to the block function here
    block(x,y,10*scale,10*scale)
    block(x-10*scale,y+10*scale,10*scale,10*scale)
    block(x,y+10*scale,10*scale,10*scale)
    block(x+10*scale,y+10*scale,10*scale,10*scale)


# bunchOfBlocks(0,0,10)

def triangle (x,y,sideLength):
    # Creates an isoceles triangle: side lengths are "n", "n", and "n(sqrt(2))"
    goto(x,y)
    t.speed(0)
    t.forward((1/2)*sideLength*m.sqrt(2))
    t.left(135)
    t.forward(sideLength)
    t.left(90)
    t.forward(sideLength)
    t.left(135)
    t.forward((1/2)*sideLength*m.sqrt(2))
  

def circle (x,y,radius):
    t.speed(0)
    goto(x,y)
    t.circle(radius)


def semicircle (radius):
    t.speed(0)
    t.left(90)
    t.circle(radius,180)


def horizon(y):
    t.speed(0)
    goto(-800,y)
    t.forward(1600)


# Creates an evergreen tree with isoceles triangles
def tree (x, y, sideLength):
    goto(x,y)

    # Creates trunk of tree
    block(x,y, 0.5*sideLength, 0.25*sideLength)
    
    # Creates 1st triangle of tree
    triangle(x, 
             y+(0.25*sideLength), 
             sideLength)
    
    # Creates 2nd triangle of tree
    triangle(x, 
             y+(0.25*sideLength) + (m.sqrt((sideLength**2) - ((sideLength*m.sqrt(2))**2)/4)),
             sideLength*(5/8))
    
    # Creates 3rd triangle of tree
    triangle(x, 
             y+(0.25*sideLength) + ((13/8)*(m.sqrt((sideLength**2) - ((sideLength*m.sqrt(2))**2)/4))),
             sideLength*(7/16))
    
    # Creates 4th triangle of tree
    triangle(x, 
             y+(0.25*sideLength) + ((33/16)*(m.sqrt((sideLength**2) - ((sideLength*m.sqrt(2))**2)/4))),
             sideLength*(7/16))

    
# Creates a cloud with semicircles
def cloud (x,y,scale):
    goto(x,y)
    print("goto(): before cloud move, turtle at", t.position())
    t.forward(100*scale)
    t.right(20)
    semicircle(20*scale)
    t.left(90)
    semicircle(45*scale)
    t.left(100)
    semicircle(60*scale)
    t.left(120)
    semicircle(40*scale)
    t.left(120)
    semicircle(20*scale)
    t.left(120)
    semicircle(3.71*scale)
    t.left(10)    
    t.forward(250*scale)
    print("goto(): after cloud move, turtle at", t.position())
    

# Creates rocks from blocks
def rocks (x,y,scale):
    block(x,y,10*scale,10*scale)
    block(x-11*scale,y,12*scale,4*scale)
    block(x+10*scale,y,10*scale,10*scale)
    block(x+10*scale,y+10*scale,10*scale,10*scale)
    block(x+20*scale,y,10*scale,15*scale)
    block(x+30*scale,y,10*scale,8*scale)


# Creates a sun with circles and blocks 
def sun (x,y,scale):
    t.up()
    t.goto(x,y)
    t.down()
    t.speed(0)
    circle(x,y,1*scale)
    block(x, y-2.25*scale, 1*scale, 2*scale)
    block(x, y+2.25*scale, 1*scale, 2*scale)
    block(x+2.25*scale,y+0.5*scale,  2*scale, 1*scale)
    block(x-2.25*scale,y+0.5*scale,  2*scale, 1*scale)
    tiltedBlock(x-1.25*scale,y-.75*scale, 1.5*scale, .75*scale, 45)
    tiltedBlock(x+1.75*scale,y+2.2*scale, 1.5*scale, .75*scale, 45)
    tiltedBlock(x+1.75*scale,y-.2*scale, 1.5*scale, .75*scale, 135)
    tiltedBlock(x-1.3*scale,y+2.75*scale, 1.5*scale, .75*scale, 135)


# sun(-500,300,50)
# horizon(0)
# rocks(-200,-200,5)
# tree(0,0,100)
# cloud(200,250, 1.5)
# cloud(0,250,.75)
# cloud(-150,200, 1)
# cloud(450,200,.5)

    


t.exitonclick()