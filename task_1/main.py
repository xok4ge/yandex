import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import task_1.map_dialog as dialog
from task_1.map_inf import info as inf

import requests
import pygame
#---------------------------------
pygame.init()
FPS = 60
FULLSCREEN = False
WIDTH = 600
HEIGHT = 400
polz = [111]
scale = ''
start, always = [30, 50], []  # max y = 80, min y = -81     max x = 180, min x = -180
#----------------------------------


def render(api):
    response = requests.get(api)
    if response:
        with open('picture.png', 'wb') as f:
            f.write(response.content)
        img = pygame.image.load('picture.png')
        return img
    return None

def get_picture(x, y, z=2):
    if -180 < x <= 180 and -81 < y <= 80 and 0 <= int(z) <= 17:
        return f'?ll={x},{y}&z={z}&l=map'

def main(fps, width, height, fullscreen=False):
    global always, scale
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
        if not coords:
            raise ValueError
        always = polz
    except ValueError:
        coords = get_picture(*start)
        always = start
    print(coords)
    geocoder_api_serve = "https://static-maps.yandex.ru/1.x/" + coords
    print(geocoder_api_serve, 'djn')
    flag = render(geocoder_api_serve)
    if flag:
        img = render(geocoder_api_serve)
    else:
        print('aaa')
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(img, (0, 0))
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main(FPS, WIDTH, HEIGHT, FULLSCREEN)