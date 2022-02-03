import pygame
import requests

FPS = 60
REQ = s = 'https://static-maps.yandex.ru/1.x/?ll=133.282109%2C-26.327176&spn=25,25&l=sat'
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
    pygame.display.set_caption('Высадка десанта')

    response = requests.get(REQ)
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