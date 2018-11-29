import pygame
from pygame import *

MOVE_SPEED = 7

WIDTH = 50
HEIGHT = 50
COLOR = "#888888"

animCount = 0
walkDown =[pygame.image.load("image/run_up (1).png"),pygame.image.load("image/run_up (2).png"),pygame.image.load("image/run_up (3).png")]
walkUp = [pygame.image.load("image/run_up (1).png"),pygame.image.load("image/run_up (2).png"),pygame.image.load("image/run_up (3).png")]
walkLeft = [pygame.image.load("image/run_left11.png"),pygame.image.load("image/run_left12.png"),pygame.image.load("image/run_left13.png")]
walkRight = [pygame.image.load("image/run_right11.png"),pygame.image.load("image/run_right12.png"),pygame.image.load("image/run_right13.png")]




class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = Surface((WIDTH, HEIGHT))
        # self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

    def update(self, left, right, up, down, platforms,doors):
        global animCount

        if animCount + 1 >= 9:
            animCount = 0
        if up:
            self.xvel = 0
            self.yvel = -MOVE_SPEED
            self.image = walkUp[animCount // 3]
            animCount += 1

        if down:
            self.xvel = 0
            self.yvel = MOVE_SPEED
            self.image = walkDown[animCount // 3]
            animCount += 1

        if left:
            self.yvel = 0
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image = walkLeft[animCount // 3]
            animCount += 1

        if right:
            self.yvel = 0
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image = walkRight[animCount // 3]
            animCount += 1

        if not (left or right) and not (up or down):  # стоим, когда нет указаний идти
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
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = d.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = d.rect.top  # то не падает вниз

                if yvel < 0:  # если движется вверх
                    self.rect.top = d.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает
