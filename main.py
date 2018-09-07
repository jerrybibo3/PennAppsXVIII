import pygame as p
import sys
import math
from pygame.locals import *

WHITE = (255,) * 3
BLACK = (0,) * 3

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# TODO Declare constants here

p.init()
wS = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)


def main():
    while 1:
        # TODO Put your code here
        wS.fill(BLACK)
        for event in p.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    p.quit()
                    sys.exit(0)
            if event.type == QUIT:
                p.quit()
                sys.exit(0)
        p.display.update()


main()
