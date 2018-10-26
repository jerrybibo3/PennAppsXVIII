from vpython import *
import math

canvas_width = 600
canvas_height = 600
fps = 30
frame = 0

userzoom = False
userspin = False
userpan = False
autoscale = False

scene = canvas(title='VPython', width=canvas_width, height=canvas_height, range=300, fov=40)

player = box(pos=vec(0, 0, 0), size=vec(60, 60, 30))

wall1 = box(pos=vec(295, 0, 0), size=vec(20, 590, 800))
wall2 = box(pos=vec(0, 295, 0), size=vec(590, 20, 800))
wall3 = box(pos=vec(-295, 0, 0), size=vec(20, 590, 800))
wall4 = box(pos=vec(0, -295, 0), size=vec(590, 20, 800))

info = label(yoffset=-265,
             text=str(fps) + 'fps, frame 0')

r = vec(0, 0, 0)

scale_factor = 20

obs = [box(pos=vec(10, 0, -2000), size=vec(20, 590, 30))]


def collideplayer(listofobs):
    for i in listofobs:
        if player.pos.z - 30 <= i.pos.z <= player.pos.z:
            if player.pos.x + player.length / 2 + i.length / 2 > i.pos.x and \
               i.pos.x + i.length / 2 + player.length / 2 > player.pos.x and \
               player.pos.y + player.height / 2 + i.height / 2 > i.pos.y and \
               i.pos.y + i.height / 2 + player.height / 2 > player.pos.y:
                print("Hit")

# def key_input(evt):
#     event_key = evt.key
#     r = player.pos
#     if event_key == 'up':
#         r.y += scale_factor * 1
#     if event_key == 'left':
#         r.x -= scale_factor * 1
#     if event_key == 'down':
#         r.y -= scale_factor * 1
#     if event_key == 'right':
#         r.x += scale_factor * 1
#     player.pos = r
#
#
# scene.bind('keydown', key_input)


def move():
   player.pos = scene.mouse.pos


scene.bind("mousemove", move)

while 1:
    rate(fps)
    frame += 1
    info.text = str(fps) + 'fps, frame ' + str(frame)
    r.z += 0.5
    for i in obs:
        i.pos += r
    collideplayer(obs)