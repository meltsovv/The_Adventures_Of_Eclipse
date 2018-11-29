import pygame

# from level2 import *

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

pygame.display.set_caption("Our first game")



window=True
zmina = False
start_main = pygame.image.load("image/1.jpg").convert()
start_main = pygame.transform.scale(start_main, (1920, 1080))
while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if pygame.mouse.get_pos()[0] in range(0, 900) and pygame.mouse.get_pos()[1] in range(300, 1080):
                window = False
                from level1 import *
            elif pygame.mouse.get_pos()[0] in range(900, 1920) and pygame.mouse.get_pos()[1] in range(300, 1080):
                window = False
                from level2 import *
            elif pygame.mouse.get_pos()[0] in range(900, 1920) and pygame.mouse.get_pos()[1] in range(300, 1080):
                window = False
                from level3 import *
    screen.blit(start_main, (0, 0))
    pygame.display.flip()
pygame.display.update()