import time
import sys
from os import system
import shutil
import timeit
import math
columns = shutil.get_terminal_size().columns
lines = shutil.get_terminal_size().lines


# Border settings
val_border = "*"
borderh = 10
bordert = 2

# Terminal settings
term_w = 200
term_h = 50
term_tries = 0
uspacing = lines - borderh
imgstart = uspacing // 2


def termcheck():
    while True:
        global term_tries
        system('clear')
        dimensions()
        #columns = shutil.get_terminal_size().columns
        #lines = shutil.get_terminal_size().lines
        str_term_w = str(term_w)
        str_term_h = str(term_h)
        neededw = 200 - columns
        neededh = 50 - lines
        neededw = str(neededw)
        neededh = str(neededh)
        str_columns = str(columns)
        str_lines = str(lines)
        spacing(9, "u", 0)
        if columns >= term_w and lines >= term_h:
            for x in range(1, 4):
                system('clear')
                if term_tries > 0:
                    spacing(2, "u", 0)
                    print("The Terminal is now the appropriate size. Game will exit and you will need to rerun it with the same terminal size.".center(
                        columns))
                    print(f"Exiting Game in {4 - x}".center(columns))
                    time.sleep(1)
                else:
                    spacing(1, "u", 0)
                    print(
                        f"Starting Game in {4 - x}".center(columns))
                    time.sleep(1)
            if term_tries > 0:
                exit()
            else:
                break
        elif columns < term_w and lines < term_h:
            term_tries += 1
            print("Terminal size is too small.".center(columns))
            print(
                f"Minimum size is {str_term_h} height and {str_term_w} width.\n".center(columns))
            print("Size is currently".center(columns))
            print(f"Width: {str_columns}".center(columns))
            print(f"Lines: {str_lines}\n".center(columns))
            print(f"Please expand the height by {neededh} and the width by {neededw}.".center(
                columns))
            print(
                "Press enter once done. To exit, press any key and then enter.".center(columns))
            sizeorquit = input()
            if sizeorquit.lower() == "":
                continue
            else:
                exit()
        elif columns < term_w:
            term_tries += 1
            neededw = 200 - columns
            print("Terminal size is too small.".center(columns))
            print(
                f"Minimum size is {str_term_h} height and {str_term_w} width.\n".center(columns))
            print("Size is currently".center(columns))
            print(f"Width: {str_columns}".center(columns))
            print(f"Lines: {str_lines}\n".center(columns))
            print(f"Please expand the width by {neededw}.".center(
                columns))
            print(
                "Press enter once done. To exit, press any key and then enter.".center(columns))
            sizeorquit = input()
            if sizeorquit.lower() == "":
                continue
            else:
                exit()
        elif lines < term_h:
            term_tries += 1
            neededh = 50 - lines
            print("Terminal size is too small.".center(columns))
            print(
                f"Minimum size is {str_term_h} height and {str_term_w} width.\n".center(columns))
            print("Size is currently".center(columns))
            print(f"Width: {str_columns}".center(columns))
            print(f"Lines: {str_lines}\n".center(columns))
            print(f"Please expand the height by {neededh}.".center(
                columns))
            print(
                "Press enter once done. To exit, press any key and then enter.".center(columns))
            sizeorquit = input()
            if sizeorquit.lower() == "":
                continue
            else:
                exit()


def spacing(imgheight, uln, borderh, offset=None):
    dimensions()
    bh = borderh
    us = lines - bh
    imgfit = us - imgheight

    if imgfit < 2:
        print("Image is too big for upper window size")
    if uln.lower() == "u":
        if offset:
            for x in range(offset):
                print("")
        for x in range(imgfit // 2):
            print("")
    elif uln.lower() == "l":
        if imgfit % 2 == 0:
            for x in range(imgfit // 2):
                print("")
        else:
            for x in range((imgfit // 2) + 1):
                print("")


def upperspacing():
    us = lines - borderh
    if lines % 2 == 0:
        for x in range(us):
            print("")
    else:
        for x in range(us):
            print("")


def pborder():
    borderchar = val_border
    border = borderchar.ljust(columns, val_border)
    borderl = [border, border]
    for border in borderl:
        print(border)


def showborder():
    system('clear')
    upperspacing()
    pborder()


def dimensions():
    global columns
    global lines
    global uspacing
    global imgstart
    global borderl
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines
    uspacing = lines - borderh
    imgstart = uspacing // 2
    borderchar = val_border
    border = borderchar.ljust(columns, val_border)
    borderl = [border, border]


def horz_placement(img, placement, num):
    ncolumns = columns
    newimg = []
    if num:
        ncolumns = num
    else:
        pass
    if placement.lower() == "center" or None:
        for x in range(len(img)):
            varimg = img[x]
            varimg = varimg.center(ncolumns)
            newimg.append(varimg)
        return newimg
    elif placement.lower() == "left":
        for x in range(len(img)):
            varimg = img[x]
            varimg = varimg.ljust(ncolumns)
            newimg.append(varimg)
        return newimg
    elif placement.lower() == "right":
        for x in range(len(img)):
            varimg = img[x]
            varimg = varimg.rjust(ncolumns)
            newimg.append(varimg)
        return newimg


def scrolltext(text, sec):
    text = text.center(columns)
    for char in text:
        if char == " ":
            print(char, end="", flush=True)
        else:
            time.sleep(sec)
            print(char, end="", flush=True)
