"""
File: draw line
Name:Ethan HSU
-------------------------
TODO:Make a program that when odd timemyou click the butttom it locate and draw a circle,and when it is even,click the buttom will connect the dot .
"""


"""
   This program creates lines on an instance of GWindow class.
   There is a circle indicating the user’s first click. A line appears
   at the condition where the circle disappears as the user clicks
   on the canvas for the second time.
"""
from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title='draw_line')
SIZE = 30
num = 0
circle = GOval(SIZE, SIZE)


def main():
    onmouseclicked(mix)


def mix(mouse):
    global num
    global circle
    num += 1
    print(str(num))
    if num % 2 == 0:
        window.remove(circle)
        line = GLine(circle.x+SIZE/2, circle.y+SIZE/2, mouse.x, mouse.y)
        window.add(line)
    else:
        circle = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        window.add(circle)


if __name__ == "__main__":
    main()
