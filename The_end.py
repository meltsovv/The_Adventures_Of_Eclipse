import pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Our first game")
window=True
zmina = False
start_main = pygame.image.load("image/game_over.png").convert()
start_main = pygame.transform.scale(start_main, (1920, 1080))
while window:
    for e in pygame.event.get():  # Обрабатываем события
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                raise SystemExit
        if e.type == pygame.MOUSEBUTTONDOWN:

            if pygame.mouse.get_pos()[0] in range(0, 1920) and pygame.mouse.get_pos()[1] in range(500, 1080):

                raise SystemExit
    screen.blit(start_main, (0, 0))
    pygame.display.flip()
pygame.display.update()