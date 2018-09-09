"""
Hack the Mainframe
Jerrybibo
September 8th - PennApps XVIII
"""

import pygame as p
import random as r
import math
from os import system, popen, chdir
from ast import literal_eval
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

SCALEVALUE = 5
f = open("./forgereeee.txt")
x = f.read()
x = literal_eval(x)
FPS = 60

clock = p.time.Clock()

wS = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULL_SCREEN_MOD[FULL_SCREEN], 32)
movement = []
p.display.set_caption(SCREEN_CAPTION)

# Image load
prestates = (p.image.load("./resources/prestate_angel.png").convert(),
             p.image.load("./resources/prestate_devil.png").convert())
viruses = (p.image.load("./resources/envy.png").convert_alpha(),
           p.image.load("./resources/pride.png").convert_alpha(),
           p.image.load("./resources/wrath.png").convert_alpha(),
           p.image.load("./resources/glutton.png").convert_alpha())
mainframes = (p.image.load("./resources/hackthemainframe1.png").convert_alpha(),
              p.image.load("./resources/hackthemainframe2.png").convert_alpha(),
              p.image.load("./resources/hackthemainframe3.png").convert_alpha())
win = p.image.load("./resources/win.png").convert()
lose = p.image.load("./resources/lose.png").convert()
sign_in = p.image.load("./resources/signin.png").convert_alpha()
user_icon = p.image.load("./resources/usricon.png").convert()
fb_screen = p.image.load("./resources/fb_screen.png").convert()
fb_login = p.image.load("./resources/fb_login.png").convert()
fb_login_c = p.image.load("./resources/fb_login_corrupt.png").convert()
cursor = p.image.load("./resources/cursor.png").convert_alpha()
scenes = [(fb_screen, [p.Rect(144, 198, 162, 206)]),
          (fb_login, [p.Rect(482, 352, 307, 44)]),
          ('cuck'),
          (fb_login, [p.Rect(482, 352, 307, 44)]),
          (fb_login_c, [p.Rect(482, 352, 307, 44)])]
intro_loop = p.mixer.Sound("resources/intro.wav")
main_loop = p.mixer.Sound("resources/loop.wav")

class Particle:
    x = 0
    y = 0
    dx = 0
    dy = 0
    health = 0
    sprite = None

    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.health = 30 + r.randint(0, 70)
        self.dx = -3 + r.randint(0, 7)
        self.dy = -3 + r.randint(0, 7)

    def draw(self):
        wS.blit(self.sprite, (self.x - 3, self.y - 3))

    def drawInv(self):
        inv = inverted(self.sprite)
        wS.blit(inv, (self.x - 3, self.y - 3))

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += .01
        self.health -= 1


def create_part_sys(x, y, sprite):
    parts = []
    for i in range(r.randint(2, 6)):
        parts.append(Particle(x, y, sprite))
    return parts


def inverted(img):
   inv = p.Surface(img.get_rect().size, p.SRCALPHA)
   inv.fill((255,255,255,255))
   inv.blit(img, (0,0), None, BLEND_RGB_SUB)
   return inv


def create_text(window_surface, x, y, size, phrase, foreground_color, background_color=(), align="c", font="font.ttc"):
    font_obj = p.font.Font("./resources/" + font, size)
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


def direction(point1, point2):
    p1 = point1[:2]
    if p1 == (-1,-1) or point2[:2] == (-1,-1) or p1 == (0,0) or point2[:2] == (0,0):
        return 'f'
    dt = point2[2] - point1[2]
    dxdt = (point2[0] - point1[0]) / dt
    dydt = (point2[1] - point1[1]) / dt
    return [dxdt, dydt, p1]


def createVectorsList(lstofpoints):
    vectors = []
    for i in range(len(lstofpoints) - 1):
        if (direction(lstofpoints[i], lstofpoints[i+1]) != 'f'):
            vectors.append(direction(lstofpoints[i], lstofpoints[i+1]))
    return vectors


def draw(vectors):
    while True:
        #i[2] is point 1
        pt2 = [0,0]
        for i in vectors:
            pt2[0] = int(i[2][0] + i[0] * SCALEVALUE)
            pt2[1] = int(i[2][1] + i[1] * SCALEVALUE)
            p.draw.line(wS, BLACK, i[2], pt2, 2)
            p.draw.circle(wS, BLACK, pt2, 3, 0)
            p.image.save(wS, "./vfak1.jpg")
            p.quit()
            f.close()

            system('mv vfak1.jpg /Users/jerrybibo/Downloads/tensorflow-for-poets-2/')
            output = popen('cd /Users/jerrybibo/Downloads/tensorflow-for-poets-2; ./outsideRunner.sh').read()
            print(output)
                # print(vectors)
            exit(0)
        p.display.update()
        clock.tick(FPS)


def losing_screen():
    while 1:
        for event in p.event.get():
            if event.type == KEYDOWN:
                p.quit()
                exit(0)
        wS.fill(BLACK)
        wS.blit(lose, (490, 550))
        wS.blit(mainframes[1], (320, 0))
        p.display.update()


def main():
    global wS, FULL_SCREEN
    # todo define main-scope variables here
    intro()
    scene_index = 0
    current_alpha = 0
    progression_overlay = p.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    progression_color_v = 15
    progression_rects = [p.Rect(144, 198, 162, 206)]
    progressing = False
    parties = []
    thres = 25
    count = 0
    takeover = False
    flip = False
    main_loop.play(-1)

    while 1:
        wS.fill(BLACK)
        mouse_xy = p.mouse.get_pos()
        if scene_index == 2:
            FULL_SCREEN = False
            wS = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULL_SCREEN_MOD[FULL_SCREEN], 32)
            system('python3 ./docu\ 2.py')
            scene_index += 1
        if scene_index == 3:
            FULL_SCREEN = True
            wS = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULL_SCREEN_MOD[FULL_SCREEN], 32)
            wS.blit(scenes[scene_index][0], (0, 0))
            #draw(createVectorsList(x))
            current_alpha = 255
            progression_color_v = -15
            scene_index += 1
            takeover = True
            progressing = True
        else:
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
                if not progressing:
                    losing_screen()

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

        if takeover:
            if count >= thres > 5:
                count = 0
                if thres > 5:
                    thres -= 1
                parts = create_part_sys(r.randint(0, SCREEN_WIDTH), r.randint(0, SCREEN_HEIGHT), r.choice(viruses))
                parties.append(parts)
                flip = True
            count += 1
            if flip != True:
                for x in parties:
                    for y in x:
                        y.update()
                        y.draw()
            else:
                wS.fill(BLACK)
                for x in parties:
                    for y in x:
                        y.update()
                        y.drawInv()
                if thres > 5:
                    flip = False
            for q in parties:
                for i in range(len(q[:]) - 1, 0, -1):
                    if q[i].health <= 0:
                        parts = create_part_sys(q[i].x, q[i].y, r.choice(viruses))
                        parties.append(parts)
                        q.remove(q[i])

        if len(parties) > 300:
            takeover = False


        wS.blit(progression_overlay, (0, 0))
        wS.blit(cursor, (mouse_xy[0], mouse_xy[1]))
        # create_text(wS, 5, SCREEN_HEIGHT - 20, 24, str(mouse_xy[0]) + ' ' + str(mouse_xy[1]), BLACK, WHITE, "l")
        p.display.update()
        clock.tick(60)


def intro():
    greetings()
    current_alpha = 255
    progression_overlay = p.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    progression_color_v = -5
    progressing = True
    track = False
    first = True
    count = 0
    prestate_index = 0
    movement = []
    parties = []
    thres = 25
    count = 0
    takeover = False
    flip = False


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
                intro_loop.fadeout(100)

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
            takeover = True

        wS.blit(sign_in, (0, 80))
        wS.blit(progression_overlay, (0, 0))
        if takeover:
            intro_loop.stop()
            if count >= thres > 5:
                count = 0
                if thres > 5:
                    thres -= 1
                parts = create_part_sys(r.randint(0, SCREEN_WIDTH), r.randint(0, SCREEN_HEIGHT), r.choice(viruses))
                parties.append(parts)
                flip = True
            count += 1
            if flip != True:
                for x in parties:
                    for y in x:
                        y.update()
                        y.draw()
            else:
                wS.fill(BLACK)
                for x in parties:
                    for y in x:
                        y.update()
                        y.drawInv()
                if thres > 5:
                    flip = False
            for q in parties:
                for i in range(len(q[:]) - 1, 0, -1):
                    if q[i].health <= 0:
                        parts = create_part_sys(q[i].x, q[i].y, r.choice(viruses))
                        parties.append(parts)
                        q.remove(q[i])
        wS.blit(cursor, (prev[0], prev[1]))
        wS.blit(user_icon, (0, SCREEN_HEIGHT - 50))
        # create_text(wS, 5, SCREEN_HEIGHT - 20, 24, str(prev[0]) + ' ' + str(prev[1]), BLACK, WHITE, "l")
        p.display.update()
        clock.tick(60)


def greetings():
    # edited 10:41 - removed p.Rect(760, 0, 1160, 200)
    progression_rects = [p.Rect(760, 200, 1160, 400)]
    current_alpha = 0
    progression_overlay = p.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    progression_color_v = 5
    progressing = False
    ticker = 0
    index = 0
    greeting_text = '''    Welcome to the mainframe, hacker.
        Your mission, if you choose to accept it, is
        to break in and retrieve vital information from
        the core of this machine. Tread carefully, as one
        false click and the system will automatically
        shutdown, and the authorities will be instantly
        alerted. The owner of this machine is some
        kind of mad scientist and has left a path they
        believe no one will be able to follow to the
        vital information. Good luck.'''
    greeting = greeting_text.split('\n')

    count = 0
    ind = 0
    y = SCREEN_HEIGHT // 1.5 - 70
    intro_loop.play(-1)

    while 1:
        wS.fill(BLACK)
        mousexy = p.mouse.get_pos()
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
                # if progression_rects[0].collidepoint(mousexy[0], mousexy[1]):
                #     print("u won kek")
                #     exit(0)
                if progression_rects[0].collidepoint(mousexy[0], mousexy[1]):
                    progressing = True

        if progressing:
            current_alpha += progression_color_v
            if current_alpha > 255:
                return
            if current_alpha < 0:
                current_alpha = 0
                progression_color_v *= -1
                progressing = False

        ticker += 1
        if ticker > 30:
            ticker = 0
            index = -(index - 1) + 1

        if count < len(greeting[ind]):
            count += 1
        elif ind + 1 < len(greeting):
            count = 0
            ind += 1
        for x in range(ind + 1):
            if x < ind:
                text = greeting[x]
            else:
                text = greeting[x][:count]
            create_text(wS, SCREEN_WIDTH // 1.5, y + 20 * x, 20, text, WHITE, (), "c", "facy.ttc")

        wS.blit(mainframes[index], (0, 80))
        wS.blit(win, (810, -50))
        wS.blit(lose, (810, 150))
        # create_text(wS, 690, 450, 32, "")
        wS.blit(progression_overlay, (0, 0))
        wS.blit(cursor, (mousexy[0], mousexy[1]))
        p.display.update()
        clock.tick(60)

#
# def forgery():
#     track = False
#     first = True
#     count = 0
#     prevCount = 0
#     movement = []
#
#     while True:
#
#         prev = p.mouse.get_pos()
#
#         for event in p.event.get():
#             if event.type == QUIT:
#                 p.quit()
#                 exit(0)
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     x = len(movement) - 1
#                     while movement[x][0] == -1 and movement[x][1] == -1:
#                         movement.remove(movement[x])
#                         x -= 1
#                     return movement
#                     p.quit()
#                     sys.exit(0)
#             if event.type == MOUSEBUTTONUP:
#                 track = False
#             if event.type == MOUSEBUTTONDOWN:
#                 track = True
#                 prev = p.mouse.get_pos()
#                 start = prev[0]
#
#         if track:
#
#             if first:
#                 first = False
#                 count = 0
#
#             p.draw.line(wS, BLACK, prev, p.mouse.get_pos(), 2)
#             p.draw.line(wS, RED, (count-1, SCREEN_HEIGHT - prev[0]//2), (count, SCREEN_HEIGHT - p.mouse.get_pos()[0]//2), 2)
#             p.draw.line(wS, GREEN, (count-1, prev[1]//2 - start//4), (count, p.mouse.get_pos()[1]//2 - start//4), 2)
#             #movement.extend([(0,0,0)] * (count - prevCount))
#             movement.append((((0, 0), (0, 0)), ((0, 0), (0, 0))))
#
#         else:
#             if not first:
#                 movement.append((((0, 0), (0, 0)), ((0, 0), (0, 0))))
#
#         p.display.update()
#         count += 1
#         clock.tick(FPS)

main()
# forgery()