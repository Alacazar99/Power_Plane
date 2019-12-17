# @Time    : 2019/6/2 11:16
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : bullet.py
# @Software: PyCharm

import pygame
import os.path as path
import setting
from pygame.sprite import Sprite

class HeroBullet(Sprite):
    def __init__(self,x,y):
        super(HeroBullet, self).__init__()
        # 导入子弹
        self.image = pygame.image.load(path.join(setting.img_folder,"bullet2.png"))
        # 定义子弹初始位置
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self, *args):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

class HeroBullet2(Sprite):
    def __init__(self,x,y):

        super(HeroBullet2, self).__init__()
        # 导入子弹
        self.image = pygame.image.load(path.join(setting.img_folder,"bullet2.png"))
        # 定义子弹初始位置
        self.rect = self.image.get_rect()
        # self.rect.center = center
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0
        self.d = 6

    def update(self, *args):

        self.rect.y -= 4
        if self.speedx < -12:
            self.d = 3
        if self.speedx > 12:
            self.d = -3
        self.speedx += self.d
        self.rect.x += self.speedx

        if self.rect.bottom < 0:
            self.kill()

class NpcBullet(Sprite):
    def __init__(self,x,y):
        super(NpcBullet, self).__init__()
        # 导入敌机子弹
        image = pygame.image.load(path.join(setting.img_folder,"bullet1.png"))
        self.image = pygame.transform.scale(image, (4, 8))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self, *args):
        self.rect.y += 7
        if self.rect.centery < 0:
            self.kill()
