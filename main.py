"""
Hack the Mainframe
Jerrybibo
September 8th - PennApps XVIII
"""

import pygame as p
import random as r
import math
from sys import exit
from pygame.locals import *

FULL_SCREEN_MOD = [0, FULLSCREEN]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 10)
GREEN = (10, 255, 10)
BLUE = (10, 10, 255)
RED = (255, 10, 10)
GRAY = (140, 140, 140)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_CAPTION = "Hack the Mainframe"
FULL_SCREEN = True
p.init()
p.mouse.set_visible(False)

clock = p.time.Clock()

wS = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULL_SCREEN_MOD[FULL_SCREEN], 32)
p.display.set_caption(SCREEN_CAPTION)

# Image load
prestates = (p.image.load("./resources/prestate_angel.png").convert(),
             p.image.load("./resources/prestate_devil.png").convert())
viruses = (p.image.load("./resources/envy.png").convert_alpha(),
           p.image.load("./resources/pride.png").convert_alpha(),
           p.image.load("./resources/wrath.png").convert_alpha(),
           p.image.load("./resources/glutton.png").convert_alpha())
user_icon = p.image.load("./resources/usricon.png").convert()
fb_screen = p.image.load("./resources/fb_screen.png").convert()
fb_login = p.image.load("./resources/fb_login.png").convert()
cursor = p.image.load("./resources/cursor.png").convert_alpha()
scenes = [(fb_screen, [p.Rect(144, 198, 162, 206)]),
          (fb_login, [p.Rect(482, 352, 307, 44)])]


def create_text(window_surface, x, y, size, phrase, foreground_color, background_color=(), align="c"):
    font_obj = p.font.Font("./resources/font.ttc", size)
    text_surface_obj = font_obj.render(phrase, True, foreground_color, background_color)
    text_rect_obj = text_surface_obj.get_rect()
    if align == "c":
        text_rect_obj.center = (x, y)
    elif align == "r":
        text_rect_obj.centery = y
        text_rect_obj.right = x
    elif align == "l":
        text_rect_obj.centery = y
        text_rect_obj.left = x
    window_surface.blit(text_surface_obj, text_rect_obj)


def main():
    # todo define main-scope variables here
    intro()
    scene_index = 0
    current_alpha = 0
    progression_overlay = p.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    progression_color_v = 15
    progression_rects = [p.Rect(144, 198, 162, 206)]
    progressing = False

    while 1:
        wS.fill(BLACK)
        mouse_xy = p.mouse.get_pos()
        wS.blit(scenes[scene_index][0], (0, 0))
        progression_overlay.set_alpha(current_alpha)
        for event in p.event.get():
            if event.type == QUIT:
                p.quit()
                exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    p.quit()
                    exit(0)
            elif event.type == MOUSEBUTTONDOWN:
                for rect in progression_rects:
                    if rect.collidepoint(mouse_xy[0], mouse_xy[1]):
                        progressing = True

        if progressing:
            current_alpha += progression_color_v
            if current_alpha >= 255:
                current_alpha = 255
                scene_index += 1
                progression_color_v *= -1
            if current_alpha <= 0:
                current_alpha = 0
                progression_color_v *= -1
                progression_rects = scenes[scene_index][1]
                progressing = False

        wS.blit(progression_overlay, (0, 0))
        wS.blit(cursor, (mouse_xy[0], mouse_xy[1]))
        # create_text(wS, 5, SCREEN_HEIGHT - 20, 24, str(mouse_xy[0]) + ' ' + str(mouse_xy[1]), BLACK, WHITE, "l")
        p.display.update()
        clock.tick(60)


def intro():
    current_alpha = 255
    progression_overlay = p.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    progression_color_v = -5
    progressing = True
    track = False
    first = True
    count = 0
    prestate_index = 0
    movement = []

    while 1:
        wS.fill(BLACK)
        prev = p.mouse.get_pos()
        progression_overlay.set_alpha(current_alpha)
        for event in p.event.get():
            if event.type == QUIT:
                p.quit()
                exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    p.quit()
                    exit(0)
                if event.key == K_RETURN:
                    progressing = True
            elif event.type == MOUSEBUTTONDOWN:
                track = True
                prev = p.mouse.get_pos()
                start = prev[0]
            elif event.type == MOUSEBUTTONUP:
                track = False
        p.draw.rect(wS, WHITE, (SCREEN_WIDTH // 2, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        p.draw.line(wS, BLACK, prev, p.mouse.get_pos(), 2)
        wS.blit(prestates[prestate_index], (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 16 * 9))

        for i in movement:
            print(i)
            p.draw.line(wS, BLUE, i[0][0], i[0][1], 3)
            p.draw.line(wS, GREEN, i[1][0], i[1][1], 3)

        if track and prev[0] >= 640 and prev[1] <= 400:
            if first:
                first = False
                count = 0
            # if p.mouse.get_pos(),
            # This is the x-value (blue)
            movement.append((((SCREEN_WIDTH // 2 + count - 1,
                               round((prev[0] - SCREEN_WIDTH / 4 * 3) / 4.8 + SCREEN_HEIGHT / 8)),
                              (SCREEN_WIDTH // 2 + count,
                               round((p.mouse.get_pos()[0] - SCREEN_WIDTH / 4 * 3) / 4.8 + SCREEN_HEIGHT / 8))),
                             ((SCREEN_WIDTH // 2 + count - 1,
                               round((prev[1] - SCREEN_HEIGHT / 4 * 3) / 3 + SCREEN_HEIGHT / 8 * 3)),
                              (SCREEN_WIDTH // 2 + count,
                               round((p.mouse.get_pos()[1] - SCREEN_HEIGHT / 4 * 3) / 3 + SCREEN_HEIGHT / 8 * 3)))))
            if round((p.mouse.get_pos()[0] - SCREEN_WIDTH / 4 * 3) / 4.8 + SCREEN_HEIGHT / 8) > \
                    round((p.mouse.get_pos()[1] - SCREEN_HEIGHT / 4 * 3) / 3 + SCREEN_HEIGHT / 8 * 3):
                progressing = True

        else:
            if not first:
                movement.append((((0, 0), (0, 0)), ((0, 0), (0, 0))))
        if progressing:
            current_alpha += progression_color_v
            if current_alpha > 255:
                return
            if current_alpha <= 0:
                current_alpha = 0
                progression_color_v *= -1
                progressing = False

        if not first:
            count += 1
        if count > 640:
            prestate_index = 1

        wS.blit(progression_overlay, (0, 0))
        wS.blit(cursor, (prev[0], prev[1]))
        wS.blit(user_icon, (0, SCREEN_HEIGHT - 50))
        # create_text(wS, 5, SCREEN_HEIGHT - 20, 24, str(prev[0]) + ' ' + str(prev[1]), BLACK, WHITE, "l")
        p.display.update()
        clock.tick(60)


main()
