import pygame
import os
import requests


def get_map(x, y, z, type="map"):
    if z > 18:
        z = 18
    if z < 1:
        z = 1
    map_request = f'https://static-maps.yandex.ru/1.x/?ll={x}%2C{y}&size=450,450&z={z}&l={type}'
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file
    os.remove(map_file)


def get_picture(x, y, z=10, type="map"):
    width = 450
    height = 350

    map_file = get_map(x, y, z, type)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
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
                z -= 1
                screen.blit(pygame.image.load(get_map(x, y, z)), (0, 0))
            if keys[pygame.K_PAGEDOWN]:
                z += 1
                screen.blit(pygame.image.load(get_map(x, y, z)), (0, 0))
        img = pygame.image.load('Map.png')
        screen.blit(img, (0, 0))
        pygame.display.flip()

    pygame.quit()
    os.remove(map_file)


if __name__ == '__main__':
    get_picture(57, 57, 10, "map")
