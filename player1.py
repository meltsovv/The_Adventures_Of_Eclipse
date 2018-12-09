import pygame
from pygame import *
MOVE_SPEED = 7
WIDTH = 50
HEIGHT = 50
COLOR = "#888888"
animCount = 0
animCount1 = 0
walkDown1 =[pygame.image.load("image/Solnce ruh verh.png"),pygame.image.load("image/Solnce ruh verh1.png"),pygame.image.load("image/Solnce ruh verh2.png")]
walkUp1 = [pygame.image.load("image/Solnce ruh verh.png"),pygame.image.load("image/Solnce ruh verh1.png"),pygame.image.load("image/Solnce ruh verh2.png")]
walkLeft1 = [pygame.image.load("image/run_left1.png"),pygame.image.load("image/run_left2.png"),pygame.image.load("image/run_left3.png")]
walkRight1 = [pygame.image.load("image/run_right1.png"),pygame.image.load("image/run_right2.png"),pygame.image.load("image/run_right3.png")]
class Player1(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = pygame.image.load("image/run_right2.png")
        # self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

    def update(self, left1, right1, up1, down1, platforms, doors):
        global animCount1
        print(up1, down1, left1, right1)

        if animCount1 + 1 >= 9:
            animCount1 = 0
        if up1 :
            self.xvel = 0
            self.yvel = -MOVE_SPEED
            self.image = walkUp1[animCount1 // 3]
            animCount1 += 1

        if down1 :
            self.xvel = 0
            self.yvel = MOVE_SPEED
            self.image = walkDown1[animCount1 // 3]
            animCount1 += 1

        if left1 :
            self.yvel = 0
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image = walkLeft1[animCount1 // 3]
            animCount1 += 1

        if right1 :
            self.yvel = 0
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image = walkRight1[animCount1 // 3]
            animCount1 += 1

        if not (left1 or right1) and not (up1 or down1):  # стоим, когда нет указаний идти
            self.xvel = 0
            self.yvel = 0

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms,doors)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms,doors)

    def collide(self, xvel, yvel, platforms,doors):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает
        for d in doors:
            if sprite.collide_rect(self, d):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = d.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = d.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = d.rect.top  # то не падает вниз

                if yvel < 0:  # если движется вверх
                    self.rect.top = d.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает





