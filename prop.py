import random
import pygame
from pygame.sprite import Sprite
import os.path as path
import setting
import hit
import information as info
import math




class Bombprop(Sprite):
    # 定义加血道具
    def __init__(self,x,y):
        super().__init__()
        image = pygame.image.load(path.join(setting.img_folder,"bomb_supply.png"))
        self.image = pygame.transform.scale(image,(20,35))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self, *args):
        speed = 2
        self.rect.y += speed
        if self.rect.y > setting.SCREEN_HEIGHT:
            self.kill()


class Bulletprop(Sprite):
    # 定义加火力道具
    def __init__(self,x,y):
        super(Bulletprop, self).__init__()
        prop_image = pygame.image.load(path.join(setting.img_folder,"bullet_supply.png"))
        self.image = pygame.transform.scale(prop_image, (20, 35))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self, *args):
        speed = 2
        self.rect.y += speed
        if self.rect.y > setting.SCREEN_HEIGHT:
            self.kill()

class PropFactory:
    def __init__(self):
        self.bus = info.DataBus()
        # 普通敌军生成时间
        self.prop_time = pygame.time.get_ticks()
        self.bullet_time = pygame.time.get_ticks() - 500

    def generate_comon_prop(self):
        # 定义加血道具位置
        x = random.randint(26, setting.SCREEN_WIDTH - 26)
        y = random.randint(26, 180)
        bomb_supply = Bombprop(x, y)
        self.bus.add_sprite(bomb_supply)
        self.bus.add_bomb_prop(bomb_supply)

    def bullet_prop(self):
        # 定义火力道具位置
        x = random.randint(26, setting.SCREEN_WIDTH - 26)
        y = random.randint(26, 180)

        bullet_supply = Bulletprop(x, y)
        self.bus.add_sprite(bullet_supply)
        self.bus.add_bullet_prop(bullet_supply)

    # 加血道具出现时间间隔
    def generate_bomb_prop(self):
        now = pygame.time.get_ticks()
        if now - self.prop_time > 2000 :
            self.generate_comon_prop()
            self.prop_time  = now

    def generate_bullet_prop(self):
        it = pygame.time.get_ticks()
        if it - self.bullet_time > 3000:
            self.bullet_prop()
            self.bullet_time = it
