"""
File: 
Name:Ethan HSU
----------------------
TODO:Draw a spongebob
"""

from campy.graphics.gobjects import GOval, GRect ,GLine ,GLabel
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GPolygon
import random


def main():
    window = GWindow(400, 550)
    back =GRect(400,700)
    back.color = "aqua"
    back.filled = True
    back.fill_color = "aqua"
    window.add(back, x=0, y=0)

    body = GRect(width=200, height=285)
    body.color = "black"
    body.filled = True
    body.fill_color = "yellow"
    window.add(body, x=100, y=65)

    hole1 = GOval(width=25, height=25)
    hole1.color = "goldenrod"
    hole1.filled = True
    hole1.fill_color = "goldenrod"
    window.add(hole1, x=140, y=75)

    hole2 = GOval(width=30, height=30)
    hole2.color = "goldenrod"
    hole2.filled = True
    hole2.fill_color = "goldenrod"
    window.add(hole2, x=110, y=110)

    hole3 = GOval(width=35, height=35)
    hole3.color = "goldenrod"
    hole3.filled = True
    hole3.fill_color = "goldenrod"
    window.add(hole3, x=265, y=245)

    hole4 = GOval(width=15, height=25)
    hole4.color = "goldenrod"
    hole4.filled = True
    hole4.fill_color = "goldenrod"
    window.add(hole4, x=100, y=225)

    hole5 = GOval(width=30, height=30)
    hole5.color = "goldenrod"
    hole5.filled = True
    hole5.fill_color = "goldenrod"
    window.add(hole5, x=265, y=100)

    hole6 = GOval(width=35, height=15)
    hole6.color = "goldenrod"
    hole6.filled = True
    hole6.fill_color = "goldenrod"
    window.add(hole5, x=188, y=260)

    hole7 = GOval(width=35, height=15)
    hole7.color = "goldenrod"
    hole7.filled = True
    hole7.fill_color = "goldenrod"
    window.add(hole7, x=250, y=75)
    # Draw SpongeBob's eyes (ovals)
    eye1 = GOval(width=45, height=65)
    eye1.color = "black"
    eye1.filled = True
    eye1.fill_color = "white"
    window.add(eye1, x=150, y=120)
    eyeball1 = GOval(width=25, height=25)
    eyeball1.color = "black"
    eyeball1.filled = True
    eyeball1.fill_color = "skyblue"
    window.add(eyeball1, x=160, y=140)

    pupil1 = GOval(width=12, height=12)
    pupil1.color = "black"
    pupil1.filled = True
    pupil1.fill_color = "black"
    window.add(pupil1, x=166, y=148)

    eye2 = GOval(width=45, height=65)
    eye2.color = "black"
    eye2.filled = True
    eye2.fill_color = "white"
    window.add(eye2, x=215, y=120)
    eyeball1 = GOval(width=25, height=25)
    eyeball1.color = "black"
    eyeball1.filled = True
    eyeball1.fill_color = "skyblue"
    window.add(eyeball1, x=225, y=140)

    pupil2 = GOval(width=12, height=12)
    pupil2.color = "black"
    pupil2.filled = True
    pupil2.fill_color = "black"
    window.add(pupil2, x=232, y=148)

    # Draw SpongeBob's nose
    nose = GOval(width=20, height=20)

    nose.color = "black"
    nose.filled = True
    nose.fill_color = "orange"
    window.add(nose,x=190,y=180)

    # Draw SpongeBob's mouth (line)
    mouth = GLine(160, 220, 240, 220)
    mouth.color = "black"
    window.add(mouth)

    teeth = GRect(width=15, height=20)
    teeth.color = "black"
    teeth.filled = True
    teeth.fill_color = "white"
    window.add(teeth, x=185, y=220)
    teeth2 = GRect(width=15, height=20)
    teeth2.color = "black"
    teeth2.filled = True
    teeth2.fill_color = "white"
    window.add(teeth2, x=215, y=220)

    # Draw SpongeBob's pants (rectangle)
    pants = GRect(width=200, height=80)
    pants.color = "black"
    pants.filled = True
    pants.fill_color = "chocolate"
    window.add(pants, x=100, y=270)

    pants2 = GRect(width=200, height=30)
    pants2.color = "black"
    pants2.filled = True
    pants2.fill_color = "white"
    window.add(pants2, x=100, y=270)

    # Draw hands
    hand1 = GRect(width=75,height=15)
    hand1.color = 'black'
    hand1.filled = True
    hand1.fill_color = 'yellow'
    window.add(hand1, x=25, y=200)
    pawn1 = GOval(width=25, height=25)
    pawn1.color = 'black'
    pawn1.filled = True
    pawn1.fill_color = 'yellow'
    window.add(pawn1, x=15, y=195)

    hand2 = GRect(width=75, height=15)
    hand2.color = "black"
    hand2.filled = True
    hand2.fill_color = "yellow"
    window.add(hand2, x=300, y=200)
    pawn2 = GOval(width=25, height=25)
    pawn2.color = "black"
    pawn2.filled = True
    pawn2.fill_color = "yellow"
    window.add(pawn2, x=360, y=195)

    # draw shirt
    shirt1 = GRect(width=25, height=25)
    shirt1.color = "black"
    shirt1.filled = True
    shirt1.fill_color = "white"
    window.add(shirt1, x=75, y=195)

    shirt2 = GRect(width=25, height=25)
    shirt2.color = "black"
    shirt2.filled = True
    shirt2.fill_color = "white"
    window.add(shirt2, x=300, y=195)

    # draw tie
    tie = GRect(width=30, height=65)
    tie.color = "black"
    tie.filled = True
    tie.fill_color = "red"
    window.add(tie, x=185, y=270)

    # Draw SpongeBob's leg (rectangles)
    leg1 = GRect(width=12, height=80)
    leg1.color = "black"
    leg1.filled = True
    leg1.fill_color = "yellow"
    window.add(leg1, x=165, y=350)

    leg2 = GRect(width=12, height=80)
    leg2.color = "black"
    leg2.filled = True
    leg2.fill_color = "yellow"
    window.add(leg2, x=223, y=350)
    # Draw SpongeBob's shoes (rectangles)
    shoe1 = GRect(width=30, height=20)
    shoe1.color = "black"
    shoe1.filled = True
    shoe1.fill_color = "black"
    window.add(shoe1, x=147, y=430)

    shoe2 = GRect(width=30, height=20)
    shoe2.color = "black"
    shoe2.filled = True
    shoe2.fill_color = "black"
    window.add(shoe2, x=223, y=430)

    # Draw SpongeBob's socks (rectangles)
    socks1 = GRect(width=12, height=30)
    socks1.color = "black"
    socks1.filled = True
    socks1.fill_color = "white"
    window.add(socks1, x=165, y=400)

    socks2 = GRect(width=12, height=30)
    socks2.color = "black"
    socks2.filled = True
    socks2.fill_color = "white"
    window.add(socks2, x=223, y=400)

    # Land
    land =GRect(400,400)
    land.color = "gray"
    land.filled = True
    land.fill_color = "gray"
    window.add(land, x=0, y=450)

if __name__ == '__main__':
    main()
