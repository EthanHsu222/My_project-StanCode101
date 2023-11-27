"""
File: 
Name:Ethan HSU
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gobjects import GLabel

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
switch = True
n = 0
k = 0
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
window.add(ball)
label = GLabel('Times : ' + str(n))
label.font = "SansSerif-30"
label.color = 'black'
x = (window.width - 100)
y = (window.height + 100)
window.add(label, x, y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    if n <= 2:
        window.remove(label)
        onmouseclicked(drop)



def drop(mouse):
    global Switch
    global ball
    global n
    global GRAVITY
    global REDUCE
    gravity = 0
    if n < 3:
        Switch = False
        n += 1
        while ball.x <= window.width:
            if ball.y <= window.height:
                gravity += GRAVITY
                ball.move(VX, gravity)
                pause(DELAY)
            elif ball.y >= window.height:
                gravity = -gravity*REDUCE
                ball.move(VX, gravity)
                pause(DELAY)
        ball.x = START_X
        ball.y = START_Y
    Switch = True


if __name__ == "__main__":
    main()
