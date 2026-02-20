'''Nicole Lin
CS151
2/12/26
lab2.py'''

import turtle as t
import random as r


def goto(x,y):
    print("goto(): going to", x,y)
    print("goto(): before move, turtle at", t.position())
    
    t.setheading(90)

    t.up()
    t.goto(x,y)
    t.down()
 
    print("goto(): after move, turtle now at", t.position())


def block(x, y, width, height):
    '''Draws a block at (x,y) of the given width and height'''
    goto(x,y)
    t.speed(0)

    t.forward(width)  # tell the turtle to go forward by width
    t.left(90)        # tell the turtle to turn left by 90 degrees
    t.forward(height) # tell the turtle to go forward by height
    t.left(90)
    t.forward(width)  # repeat the above 4 commands

    t.left(90)
    t.forward(height)

    print('block(): drawing block of size', width, height)

#block(10,100,2,10)


def bunchOfBlocks(x,y,scale):
    print('bunchOfBlocks(): drawing blocks at location',x,y)

    # put several calls to the block function here
    block(x,y,10*scale,10*scale)
    block(x-10*scale,y+10*scale,10*scale,10*scale)
    block(x,y+10*scale,10*scale,10*scale)
    block(x+10*scale,y+10*scale,10*scale,10*scale)

#bunchOfBlocks(0,0,9)
    

for i in range (10):
    bunchOfBlocks(r.random()*600 - 300,
                  r.random()* 600 - 300,
                  r.random()*2 + 0.5)





t.exitonclick()