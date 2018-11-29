import pygame
from pygame import *
from player import Player
from blocks import *
from player1 import Player1
# from start_main import *
# Объявляем переменные
WIN_WIDTH = 1920  # Ширина создаваемого окна
WIN_HEIGHT = 1080  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
st_x=1830
st_y=995
st_x1=64
st_y1=40
x_m=50
y_m=50
def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY,FULLSCREEN)  # Создаем окошко
    pygame.display.set_caption("The Adventures Of Eclips")  # Пишем в шапку

    # pygame.mixer.pre_init(44100, -16, 1, 512)
    # pygame.mixer.init()
    # pygame.mixer.music.load('music/fon.mp3')
    # pygame.mixer.music.play(-1)
    bg_image=pygame.image.load("image/moon_day.png").convert()
    bg_image1 = pygame.image.load("image/sun_day.png").convert()
    # bg_image=pygame.transform.scale(bg_image,(1920,1080))


    hero = Player(st_x, st_y)  # соwздаем героя по (x,y) координатам
    left = right = False  # по умолчанию - стоим
    up = down = False
    hero1 = Player1(st_x1, st_y1)  # создаем героя по (x1,y1) координатам
    left1 = right1 = False  # по умолчанию - стоим
    up1 = down1 = False
    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    gems_moon = pygame.sprite.Group()
    gems_sun = pygame.sprite.Group()
    drab=[]
    doors=[]
    heroes1 = pygame.sprite.Group()
    heroes = pygame.sprite.Group()
    heroes.add(hero)
    heroes1.add(hero1)
    entities.add(hero)


    level = [
        "------------------------------------------------------------",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/                                                          /",
        "/----------------------------------------------------------/"]

    timer = pygame.time.Clock()
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform_gorizontal(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "/":
                pf = Platform_vertical(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "^":
                pf = Platform_up(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "$":
                pf = Platform_down(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "!":
                pf = Platform_right(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "+":
                rb = Gems(x, y)
                entities.add(rb)
                gems_moon.add(rb)
            if col == "*":
                rb = Gems1(x, y)
                entities.add(rb)
                gems_sun.add(rb)
            if col == "#":
                dr = Drab(x, y)
                entities.add(dr)
                drab.append(dr)
            if col == "0":
                door = Door(x, y)
                entities.add(door)
                doors.append(door)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    gems_count = 0
    gems_count1 = 0
    while 1:  # Основной цикл программы
        timer.tick(100)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    raise SystemExit
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False


            if e.type == KEYDOWN and e.key == K_w:
                up1 = True
            if e.type == KEYDOWN and e.key == K_a:
                left1 = True
            if e.type == KEYDOWN and e.key == K_d:
                right1 = True
            if e.type == KEYDOWN and e.key == K_s:
                down1 = True

            if e.type == KEYUP and e.key == K_w:
                up1 = False
            if e.type == KEYUP and e.key == K_d:
                right1 = False

            if e.type == KEYUP and e.key == K_a:
                left1 = False
            if e.type == KEYUP and e.key == K_s:
                down1 = False

        screen.blit(bg_image1, (-300, 0))  # Каждую итерацию необходимо всё перерисовывать
        screen.blit(bg_image, (960, 0))
        entities.draw(screen)  # отображение
        heroes.draw(screen)

        heroes1.draw(screen)
        if pygame.sprite.groupcollide(heroes,gems_moon,False,True):
            gems_count+=1
            pygame.mixer.pre_init(44100, -16, 1, 512)
            pygame.mixer.init()
            pygame.mixer.music.load('music/gems.mp3')
            pygame.mixer.music.play(1)
        if pygame.sprite.groupcollide(heroes1,gems_sun,False,True):
            gems_count1+=1
            pygame.mixer.pre_init(44100, -16, 1, 512)
            pygame.mixer.init()
            pygame.mixer.music.load('music/gems.mp3')
            pygame.mixer.music.play(1)


        hero.update(left, right, up, down, platforms, doors)  # передвижение
        hero1.update(left1, right1, up1, down1, platforms, doors)
        # if gems_count==
        hero.update(left, right, up, down, platforms,doors)  # передвижение
        hero1.update(left1, right1, up1, down1, platforms,doors)

        pygame.display.update()  # обновление и вывод всех изменений на экран

        # print(gems_count)ad
main()