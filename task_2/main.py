import task_2.map_dialog as dialog
from task_2.map_inf import info as inf

import pygame
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import requests


#---------------------------------
pygame.init()
FPS = 60
FULLSCREEN = False
WIDTH = 600
HEIGHT = 400
polz = []
scale=''
start, always, Z = [30, 50], [], 2  # max y = 80, min y = -81     max x = 180, min x = -180
#----------------------------------

def render(api):
    response = requests.get(api)
    with open('l.png', 'wb') as f:
        f.write(response.content)
    img = pygame.image.load('l.png')
    return img


def get_picture(x, y, z=2):
    if -180 < x <= 180 and -81 < y <= 80:
        return f'?ll={x}%2C{y}&z={z}&l=map'


def zoom(z, *args):
    global Z
    Z += z
    if Z > 20:
        Z = 20
    elif Z < 2:
        Z = 2
    cords = f'?ll={args[0][0]}%2C{args[0][1]}&z={Z}&l=map'
    geocoder_api_serv = "https://static-maps.yandex.ru/1.x/" + cords
    img = render(geocoder_api_serv)
    return img


def main(fps, width, height, fullscreen=False):
    global always
    if not fullscreen:
        screen = pygame.display.set_mode((width, height))
    else:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((0, 0, 0))
    dialog.open_dialog()
    polz = inf.polz_i
    scale = inf.scale_i

    try:
        coords = get_picture(*polz, scale)
        if coords is None:
            raise ValueError
        always = polz
    except ValueError:
        coords = get_picture(*start, scale)
        always = start
    geocoder_api_serve = "https://static-maps.yandex.ru/1.x/" + coords
    img = render(geocoder_api_serve)
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if keys[pygame.K_PAGEUP]:
                img = zoom(1, always)
            if keys[pygame.K_PAGEDOWN]:
                img = zoom(-1, always)
        screen.blit(img, (0, 0))
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main(FPS, WIDTH, HEIGHT, FULLSCREEN)