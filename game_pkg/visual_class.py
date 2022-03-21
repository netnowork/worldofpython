import time
import sys
from os import system
import shutil
import timeit
import math

from game_pkg.func import *
columns = shutil.get_terminal_size().columns
lines = shutil.get_terminal_size().lines
borderchar = val_border
border = borderchar.ljust(columns, val_border)
borderl = [border, border]


class Visual:
    def __init__(self, image):
        self.imglist = open('images/img_{}'.format(image), "r")
        self.img = (self.imglist.readlines())
        self.img = [self.img.replace("\n", "") for self.img in self.img]
        self.imglist.close()
        self.imgheight = len(self.img)
        self.imgwidth = len(self.img[0])
        self.imgl = self.img
        self.imgp = horz_placement(self.imgl, "center", None)
        self.imgpl = horz_placement(self.imgl, "left", None)
        self.imgpr = horz_placement(self.imgl, "right", None)

    def show_image(self, placement):
        dimensions()
        system('clear')
        if placement == "midcenter":
            spacing(self.imgheight, "u", 0)
        for img in self.imgp:
            print(img)

    def expandmid(self, sec):
        dimensions()
        system('clear')
        for x in range(1, int((self.imgwidth / 2 + 1))):
            spacing(self.imgheight, "u", borderh)
            for y in range(0, self.imgheight):
                printimg = (self.imgl[y][0:x] + self.imgl[y][-x:])
                print(printimg.center(columns))
            time.sleep(sec)
            system('clear')
        spacing(self.imgheight, "u", borderh)
        for x in self.imgl:
            print(x.center(columns))

    def expandmidborder(self, sec_expand, sec_transition, sec_border, text):
        dimensions()
        self.expandmid(sec_expand)
        time.sleep(sec_transition)
        dimensions()
        borderchar = val_border
        border = borderchar.ljust(columns, val_border)
        borderl = [border, border]
        if text:
            text = text.center(columns)
            borderl.append(text)
        for x in range(math.ceil(columns / 10) + 2):
            exp = 10 * x
            if exp > columns:
                system('clear')
                spacing(self.imgheight, "u", borderh)
                for image in self.imgp:
                    print(image)
                spacing(self.imgheight, "l", borderh)
                for border in borderl:
                    print(border)
            else:
                system('clear')
                spacing(self.imgheight, "u", borderh)
                for image in self.imgp:
                    print(image)
                spacing(self.imgheight, "l", borderh)
                for y in range(len(borderl)):
                    print(borderl[y][0:exp])
                time.sleep(sec_border)

    def show_image_border(self):
        dimensions()
        system('clear')
        spacing(self.imgheight, "u", borderh)
        for img in self.imgp:
            print(img)
        spacing(self.imgheight, "l", borderh)
        pborder()

    def image_enter_border(self, sec, direction, mult=None):
        dimensions()
        system('clear')
        if mult == None:
            multi = 1
        else:
            multi = mult
        z = 0
        for x in range(self.imgwidth):
            if x == 0:
                z = 1
            else:
                z += x * multi
            if z > self.imgwidth:
                break
            spacing(self.imgheight, "u", borderh)
            for y in range(self.imgheight):
                if direction.lower() == "right":
                    printimg = self.imgl[y][-z:self.imgwidth]
                    print(printimg.center(columns))
                if direction.lower() == "left":
                    printimg = self.imgl[y][0:z]
                    print(printimg.center(columns))
            spacing(self.imgheight, "l", borderh)
            pborder()
            time.sleep(sec)
            system('clear')
        spacing(self.imgheight, "u", borderh)
        for x in self.imgl:
            print(x.center(columns))
        spacing(self.imgheight, "l", borderh)
        pborder()

    def image_exit_border(self, sec, direction, mult=None):
        dimensions()
        system('clear')
        if mult == None:
            multi = 1
        else:
            multi = mult
        z = 0
        for x in range(self.imgwidth):
            if x == 0:
                z = 1
            else:
                z += x * multi
            if z > self.imgwidth:
                break
            spacing(self.imgheight, "u", borderh)
            for y in range(self.imgheight):
                if direction.lower() == "right":
                    printimg = self.imgl[y][0:-z]
                    print(printimg.center(columns))
                if direction.lower() == "left":
                    printimg = self.imgl[y][z:self.imgwidth]
                    print(printimg.center(columns))
            spacing(self.imgheight, "l", borderh)
            pborder()
            time.sleep(sec)
            system('clear')
        showborder()
