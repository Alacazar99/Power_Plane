# @Time    : 2019/6/2 15:10
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : Npc.py
# @Software: PyCharm

import random
import pygame

from pygame.sprite import Sprite
import os.path as path

import setting
import information as info
from bullet import NpcBullet

class commonEnermy(Sprite):
    def __init__(self,x,y):
        super().__init__()
        image = pygame.image.load(path.join(setting.img_folder,"enemy1.png"))
        self.image = pygame.transform.scale(image,(40,30))
        self.bus = info.DataBus()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.shoot_time = pygame.time.get_ticks()
        self.delay_shoot = random.randint(500,3500)

    def update(self, *args):
        speed = 4
        self.rect.y += speed
        # 可设计其他轨迹
        self.shoot()
        if self.rect.y > setting.SCREEN_HEIGHT:
            self.kill()

    def shoot(self):
        now =  pygame.time.get_ticks()
        if now - self.shoot_time > self.delay_shoot:
            self.delay_shoot = random.randint(500, 3500)
            self.shoot_time = now
            bullet = NpcBullet(self.rect.centerx,self.rect.bottom)
            self.bus.add_sprite(bullet)
            self.bus.add_npc_bullet(bullet)

class EnermyFactory:
    def __init__(self):
        self.bus = info.DataBus()
        # 普通敌军生成时间
        self.last_common_time = pygame.time.get_ticks()



    def generate_comon_enermy(self):
        x = random.randint(26,setting.SCREEN_WIDTH - 26)
        y = random.randint(-100,80)
        common_enermy = commonEnermy(x,y)
        self.bus.add_sprite(common_enermy)
        self.bus.add_enermy(common_enermy)


    def generate_enermy(self):
        now = pygame.time.get_ticks()
        if now - self.last_common_time > 800:
            self.generate_comon_enermy()
            self.last_common_time = now

class Explosion(Sprite):
    animations = dict()
    def __init__(self, who, center):
        super().__init__()
        self.aninmation = []
        self.load()

        if who == "enermy":
            self.animation = Explosion.animations['enemy_main']
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        # 上一帧图片的显示时间
        self.last_frame_time = pygame.time.get_ticks()

    def load(self):
        # 加载敌机爆炸资源
        if Explosion.animations.get("enemy_main") is None:
            enemy_explosion_res = []
            for i in range(0, 4):
                filename = "enemy1_down{}.png".format(i+1)
                img = pygame.image.load(path.join(setting.img_folder,filename))
                enemy_explosion_res.append(img)
            Explosion.animations["enemy_main"] = enemy_explosion_res

    def update(self, *args):
        now = pygame.time.get_ticks()
        if now - self.last_frame_time > 100:
            if self.frame == len(self.animation) - 1:
                self.kill()
            else:
                self.frame += 1
                self.image = self.animation[self.frame]

class HeroExplosion(Sprite):
    animations = dict()
    def __init__(self, who, center):
        super().__init__()
        self.aninmation = []
        self.load()

        if who == "hero":
            self.animation = Explosion.animations['enemy_main']
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        # 上一帧图片的显示时间
        self.last_frame_time = pygame.time.get_ticks()

    def load(self):
        # 加载敌机爆炸资源
        if Explosion.animations.get("enemy_main") is None:
            enemy_explosion_res = []
            for i in range(0, 4):
                filename = "me_destroy_{}.png".format(i+1)
                img = pygame.image.load(path.join(setting.img_folder,filename))
                enemy_explosion_res.append(img)
            Explosion.animations["enemy_main"] = enemy_explosion_res

    def update(self, *args):
        now = pygame.time.get_ticks()
        if now - self.last_frame_time > 100:
            if self.frame == len(self.animation) - 1:
                self.kill()
            else:
                self.frame += 1
                self.image = self.animation[self.frame]



class Button(Sprite):

    def __init__(self,img_name,offset_y):
        super(Button, self).__init__()
        self.image = pygame.image.load(path.join(setting.img_folder,img_name))
        self.rect = self.image.get_rect()
        self.rect.center = setting.SCREEN_WIDTH / 2, (setting.SCREEN_HEIGHT/2) + offset_y


    @staticmethod
    def check_click(button):
        pressed = pygame.mouse.get_pressed()
        print(pressed)
        if pressed == (1, 0, 0):
            print("左键点击")
            pos = pygame.mouse.get_pos()
            button_x = pos[0]
            button_y = pos[1]

            if button.rect.left < button_x < button.rect.right and button.rect.top < button_y < button.rect.bottom:
                return True

            return False
