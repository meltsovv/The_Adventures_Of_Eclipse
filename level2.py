import pygame
from pygame import *
from player_level2 import Player
from blocks_level2 import *
from player1_level2 import Player1

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



start=1
if start==1:
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY,FULLSCREEN)  # Создаем окошко
    pygame.display.set_caption("The Adventures Of Eclips")  # Пишем в шапку

    # pygame.mixer.pre_init(44100, -16, 1, 512)
    # pygame.mixer.init()
    # pygame.mixer.music.load('music/fon.mp3')
    # pygame.mixer.music.play(-1)
    bg_image=pygame.image.load("image/space.jpg").convert()

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
    button_sun= pygame.sprite.Group()
    button_moon = pygame.sprite.Group()
    drab=[]
    doors_sun=[]
    doors_moon=[]
    heroes1 = pygame.sprite.Group()
    heroes = pygame.sprite.Group()
    heroes.add(hero)
    heroes1.add(hero1)
    entities.add(hero)

    level = [
        "------------------------------------------------------------",
        "/                  /          /    /                       /",
        "/          *       /* + * +   /  * /  + * +    * + * + *   /",
        "/----##-##----##/##/--------##/##--/##-----/##/----------##/",
        "/    ##/##   /##/##         ##/##  /##     /##/         /##/",
        "/   *##/##*  /##/## *     + ##/##  /##* + */##/*  +  *  /##/",
        "/##----/---##/##/-----/##--------##/##-----/##/-------##/##/",
        "/##    /   ##/##/     /##        ##/##     /##/       ##/##/",
        "/##*   / * ##/##/ *   /## +   *  ##/##+    /##/    * +##/##/",
        "/------/-----/##/---##/-----##---##/----/##/##/##-------/##/",
        "/            /##    ##/     ##  /##     /##/##/##////////##/",
        "/            /##*  +##/* + *##  /##  *  /##/##/##        ##/",
        "/##/##-/##/##/--------/-------##/##/--##/##/##/##+ * +   ##/",
        "/##/##-/##/##/               /##/##/  ##/##/##/------------/",
        "/##/##-/##/##/   * + * + *   /##/##/+*##/##/##             /",
        "/##/##-/##/##/##/---------/##/##/##/----/##/## *    +      /",
        "/##/##-/##/##/##/         /## ##/##     /##/-----/----##/##/",
        "/##/##-/##/##/##/   +  =  /## ##/##* +  /##/     /    ##/##/",
        "/##/##-/##/##/##/##-------/##------00-##/##/     /  + ##/##/",
        "/##/##-/##/##/##/##       !##/       /##/##/##/##/##----/##/",
        "/##/##-/##/##/##/## +     !##/ *     /##/##/##/##/##  ##/##/",
        "/##/##-/##/##/##/---------/##/-----##/##/##/##/##/##* ##/##/",
        "/##/##-/##/##/##          /##/     ##/##/##/##/##/----##/##/",
        "/##/##-/##/##/##  +    *  /##/ *   ##/##/##/##/##     ##/##/",
        "/##/##-/##/##/-------------##/-------/##/##/---##   + ##/##/",
        "/##/##  ##/##    /        /##/        ## ##    ###------/##/",
        "/##/## +##/##+   /   * + */##/    *   ## ##  + ###/##/##/##/",
        "/##-----------/##/##------/##/##----------------##/##/##/##/",
        "/##/          /##/##      /##/##  /            /##/## ## ##/",
        "/##/ *   +    /##/##  +   /##/##  /   *   +    /##/## ## ##/",
        "/##/--------##/##/------##/##/--##/----------##/##----##/##/",
        "/##         ##/##       ## ##/  ##           ## ##    ##/##/",
        "/##  +   *  ##/##   +   ## ##/  ##  +     *  ## ##  _ ##/##/",
        "/----------------------------------------------------------/"]

    timer = pygame.time.Clock()
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform_gorizontal_level2(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "/":
                pf = Platform_vertical_level2(x, y)
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
                door_sun = Door_sun(x, y)
                entities.add(door_sun)
                doors_sun.append(door_sun)
            if col == "!":
                door_moon = Door_moon(x, y)
                entities.add(door_moon)
                doors_moon.append(door_moon)
            # if col == "1":
            #     door_sun = Door_sun(x, y)
            #     entities.add(door_sun)
            #     doors_sun.append(door_sun)
            # if col == "2":
            #     door_moon = Door_moon(x, y)
            #     entities.add(door_moon)
            #     doors_moon.append(door_moon)
            if col == "_":
                button_s = Button_sun(x, y)
                entities.add(button_s)
                button_sun.add(button_s)
            if col == "=":
                button_m = Button_moon(x, y)
                entities.add(button_m)
                button_moon.add(button_m)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    gems_count = 0
    gems_count1 = 0
    while 1:  # Основной цикл программы
        timer.tick(60)
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

         # Каждую итерацию необходимо всё перерисовывать
        screen.blit(bg_image, (0, 0))
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

        if pygame.sprite.groupcollide(heroes1, button_sun, False, False):
            entities.remove(doors_moon)
            doors_moon = []
        if pygame.sprite.groupcollide(heroes, button_moon, False, False):
            entities.remove(doors_sun)
            doors_sun = []
        if gems_count==36 and gems_count1==42:
            if pygame.sprite.groupcollide(heroes, heroes1, True, True):
                print("the end")
                start = 2
                from The_end import*
        hero.update(left, right, up, down, platforms, doors_moon)  # передвижение
        hero1.update(left1, right1, up1, down1, platforms, doors_sun)
        # if gems_count==
        hero.update(left, right, up, down, platforms, doors_moon)  # передвижение
        hero1.update(left1, right1, up1, down1, platforms, doors_sun)
        # if gems_count==
        print(gems_count1)
        print(gems_count)
        pygame.display.flip()
        pygame.display.update()  # обновление и вывод всех изменений на экран

        # print(gems_count)ad

