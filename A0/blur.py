"""
File: blur.py
Name:Ethan HSU
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            pixel = new_img.get_pixel(x, y)
            total_red = 0
            total_blur = 0
            total_green = 0
            total_num = 0
            if x == 0:
                r_1 = x
            else:
                r_1 = x-1
            if y == 0:
                c_1 = y
            else:
                c_1 = y-1
            if x == (img.width-1):
                r_l = x
            else:
                r_l = x+1
            if y == (img.height-1):
                c_l = y
            else:
                c_l = y+1
            for r in range(r_1, r_l + 1):
                for c in range(c_1, c_l + 1):
                    total_red += img.get_pixel(r,c).red
                    total_blur += img.get_pixel(r,c).blue
                    total_green += img.get_pixel(r,c).green
                    total_num +=1

            pixel.red = total_red / total_num
            pixel.green = total_green / total_num
            pixel.blue = total_blur / total_num

    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
