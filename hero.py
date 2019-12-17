# @Time    : 2019/6/2 9:44
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : hero.py
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite
import os.path as path
import setting
from bullet import HeroBullet
from bullet import HeroBullet2
import information as info

class Hero(Sprite):
    def __init__(self):
        super().__init__()

        image = pygame.image.load(path.join(setting.img_folder,"me1.png"))
        self.image = pygame.transform.scale(image,(51,60))
        # 定义初始位置
        self.rect = self.image.get_rect()
        self.rect.center = (setting.SCREEN_WIDTH - 200,setting.SCREEN_HEIGHT - 80)
        self.bus = info.DataBus()
        # 定义子弹发射音效
        self.shoot_sud = pygame.mixer.Sound(path.join(setting.snd_folder,"bullet.wav"))
        self.shoot_sud.set_volume(0.8)
        # self.clock = pygame.time.Clock()
        # 子弹延时（效果）
        self.shoot_delay = 500
        self.last_shoot_time = pygame.time.get_ticks()
        self.power = 1
        self.POWERUP_TIME = 5000
        self.power_time = pygame.time.get_ticks()
        # 我方战机生命值
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

        player_img = pygame.image.load(path.join(setting.img_folder, "me1.png")).convert()
        player_mini_img = pygame.transform.scale(player_img, (25, 30))
        player_mini_img.set_colorkey()



    def update(self, *args):
        speed = 10
        keystate = pygame.key.get_pressed()
        if (keystate[pygame.K_LEFT] or keystate[pygame.K_a]):
            self.rect.x -= speed
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.rect.x += speed
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.rect.y -= speed
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.rect.y += speed
        # if keystate[pygame.K_SPACE]:  # 空格键 射击
        if self.power == 1:
            self.shoot()
        if self.power == 2:
            self.powershoot()
        if self.power >= 3:
            self.superpower()
        # 战机复活影藏
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = setting.SCREEN_WIDTH / 2
            self.rect.bottom = setting.SCREEN_HEIGHT - 80


        # 边界检查
        if self.rect.right > setting.SCREEN_WIDTH:
            self.rect.right = setting.SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > setting.SCREEN_HEIGHT:
            self.rect.bottom = setting.SCREEN_HEIGHT

        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > self.POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

    # 生命值减少
    def Lives(self):
        self.lives -= 1

    # 等级提升
    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    # 战机隐藏
    def hide(self):
        # hide the player temporarily

        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (setting.SCREEN_WIDTH/ 2, setting.SCREEN_HEIGHT + 200)



    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot_time > self.shoot_delay:
            self.last_shoot_time = now

            bullet = HeroBullet(self.rect.centerx, self.rect.top)
            self.shoot_sud.play()
            self.bus.add_sprite(bullet)
            self.bus.add_hero_bullet(bullet)

    # 火力升级
    def powershoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot_time > self.shoot_delay:
            self.last_shoot_time = now

            bullet1 = HeroBullet(self.rect.left + 15, self.rect.top)
            bullet2 = HeroBullet(self.rect.right - 15, self.rect.top)
            bullet3 = HeroBullet(self.rect.centerx, self.rect.top - 5)

            # 发射子弹时的音效
            self.shoot_sud.play()

            self.bus.add_sprite(bullet1)
            self.bus.add_sprite(bullet2)
            self.bus.add_sprite(bullet3)

            self.bus.add_hero_bullet(bullet1)
            self.bus.add_hero_bullet(bullet2)
            self.bus.add_hero_bullet(bullet3)

    def superpower(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot_time > 50:
            self.last_shoot_time = now

            bullet3 = HeroBullet2(self.rect.centerx - 32, self.rect.top)
            self.shoot_sud.play()
            self.bus.add_sprite(bullet3)
            self.bus.add_hero_bullet(bullet3)

    def draw_lives(surf, x, y, lives, img):
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            surf.blit(img, img_rect)





class HeroLive(Sprite):
    """
    我方战机爆炸
    """
    def __init__(self, name, num, center):
        super().__init__()
        self.animation = []

    # def judge(self):
    #     if player.shield <= 0:
    #         death_explosion = Explosion(player.rect.center, 'player')
    #         all_sprites.add(death_explosion)
    #         player.hide()
    #         player.lives -= 1
    #         player.shield = 100


