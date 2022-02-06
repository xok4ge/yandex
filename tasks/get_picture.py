import pygame
import os
import requests

_width = 650
_height = 450


def y_up(y, z):
    step = 400 / 2 ** z
    y2 = y + step
    if y2 <= 85:
        return y2
    return 85


def y_down(y, z):
    step = 400 / 2 ** z
    y2 = y - step
    if y2 >= -85:
        return y2
    return -85


def x_right(x, z):
    step = 880 / 2 ** z
    x2 = x + step
    if x2 > 180:
        x2 -= 360
    # print(x2)
    return x2


def x_left(x, z):
    step = 880 / 2 ** z
    x2 = x - step
    if x2 < -180:
        x2 += 360
    # print(x2)
    return x2


def get_map(x, y, z, type):
    if z > 17:
        z = 17
    if z < 1:
        z = 1
    map_request = f'https://static-maps.yandex.ru/1.x/?ll={x}%2C{y}&size={_width},{_height}&z={z}&l={type}'
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file
    os.remove(map_file)


def get_picture(x, y, z, type):
    map_file = get_map(x, y, z, type)
    pygame.init()
    screen = pygame.display.set_mode((_width, _height))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.set_caption('Задачи')
    pygame.display.flip()

    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if keys[pygame.K_PAGEUP]:
                if z > 0:
                    z -= 1
                screen.blit(pygame.image.load(get_map(x, y, z, type)), (0, 0))
            if keys[pygame.K_PAGEDOWN]:
                if z < 17:
                    z += 1
                screen.blit(pygame.image.load(get_map(x, y, z, type)), (0, 0))

            if keys[pygame.K_UP]:
                y = y_up(y, z)
                screen.blit(pygame.image.load(get_map(x, y, z, type)), (0, 0))
            if keys[pygame.K_DOWN]:
                y = y_down(y, z)
                screen.blit(pygame.image.load(get_map(x, y, z, type)), (0, 0))
            if keys[pygame.K_RIGHT]:
                x = x_right(x, z)
                screen.blit(pygame.image.load(get_map(x, y, z, type)), (0, 0))
            if keys[pygame.K_LEFT]:
                x = x_left(x, z)
                screen.blit(pygame.image.load(get_map(x, y, z, type)), (0, 0))

        img = pygame.image.load('Map.png')
        screen.blit(img, (0, 0))
        pygame.display.flip()

    pygame.quit()
    os.remove(map_file)


if __name__ == '__main__':
    get_picture(45, 30, 5, "sat,skl")
