from pygame import *
import os

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

class Platform_gorizontal_level2(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/block_up_down_level2.png" % ICON_DIR).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
class Platform_vertical_level2(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/block_left_ringh_level2.png" % ICON_DIR).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
class Gems(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/gems_sun.png" % ICON_DIR).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
class Gems1(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/gems_moon.png" % ICON_DIR).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
class Drab(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/drab1.png" % ICON_DIR).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
class Door(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/door_down.png" % ICON_DIR).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
class Button_sun(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/button.png" % ICON_DIR).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
class Button_moon(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/button1.png" % ICON_DIR).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
