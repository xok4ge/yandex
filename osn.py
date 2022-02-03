#там где будет, но пока не работает


import pygame
import requests

FPS = 60

toponym_to_find = '?ll37.769597%2C55.723277&spn=25,25&l=sat'
geocoder_api_server = "https://static-maps.yandex.ru/1.x/"
geocoder_params = {
     "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
     "geocode": toponym_to_find,
     "format": "json"}

FULLSCREEN = False
WIDTH = 600
HEIGHT = 400


def main(fps, width, height, fullscreen=False):
    pygame.init()
    if not fullscreen:
        screen = pygame.display.set_mode((width, height))
    else:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((width, height))

    response = requests.get(geocoder_api_server, params=geocoder_params)
    if response:
        with open('Australia.png', 'wb') as f:
            f.write(response.content)

    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        img = pygame.image.load('Australia.png')
        screen.blit(img, (0, 0))
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main(FPS, WIDTH, HEIGHT, FULLSCREEN)
