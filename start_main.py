import pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Our first game")
window=True
zmina = False
start_main = pygame.image.load("image/start_main.png").convert()
start_main = pygame.transform.scale(start_main, (1920, 1080))
while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] in range(0, 900) and pygame.mouse.get_pos()[1] in range(300, 1080):
                window = False
                from levels import *
            if pygame.mouse.get_pos()[0] in range(1700, 1920) and pygame.mouse.get_pos()[1] in range(0, 300):
                window= False
                from info import*
            elif pygame.mouse.get_pos()[0] in range(900, 1920) and pygame.mouse.get_pos()[1] in range(300, 1080):
                window = False
    screen.blit(start_main, (0, 0))
    pygame.display.flip()
pygame.display.update()