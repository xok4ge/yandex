import pygame
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import task_1.map_dialog as dialog
import requests

#---------------------------------
pygame.init()
FPS = 60
FULLSCREEN = False
WIDTH = 600
HEIGHT = 400
polz = []
scale = ''
start, always = [30, 50], []  # max y = 80, min y = -81     max x = 180, min x = -180
#----------------------------------


def render(api):
    response = requests.get(api)
    with open('l.png', 'wb') as f:
        f.write(response.content)
    img = pygame.image.load('l.png')
    return img


def get_picture(x, y, scale=2):
    # view min\max scale
    if -180 < x <= 180 and -81 < y <= 80 and 2 <= scale <= 20:
        return f'?ll={x}%2C{y}&z={scale}&l=map'

def main(fps, width, height, fullscreen=False):
    global always
    if not fullscreen:
        screen = pygame.display.set_mode((width, height))
    else:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((0, 0, 0))
    dialog.open_dialog()
    try:
        coords = get_picture(*polz)
        if not coords:
            raise ValueError
        always = polz
    except ValueError:
        coords = get_picture(*start)
        always = start
    geocoder_api_serve = "https://static-maps.yandex.ru/1.x/" + coords + scale
    img = render(geocoder_api_serve)
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