import pygame
import requests

FPS = 60

coords = f'?ll=63.570251%2C12.809027&z=2&spn=10,10l=sat'

geocoder_api_serve = "https://static-maps.yandex.ru/1.x/" + coords

# geocoder_params = {
#      "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
#      "geocode": toponym_to_find,
#      "format": "json"}

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

    response = requests.get(geocoder_api_serve)
    if response:
        with open('Australia.jpg', 'wb+') as f:
            f.write(response.content)

    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        img = pygame.image.load('Australia.jpg')
        screen.blit(img, (0, 0))
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main(FPS, WIDTH, HEIGHT, FULLSCREEN)
