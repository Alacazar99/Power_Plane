import pygame
import sys
import setting
import os.path as path
import hero
from pygame.sprite import Sprite
from Npc import EnermyFactory
import information as info
from Npc import Explosion
from Npc import HeroExplosion
from Npc import Button


class Hit(Sprite):
    """
    碰撞类
    """
    def __init__(self):
        super(Hit, self).__init__()
        self.score = 0
        self.power = 1
        self.die_music = pygame.mixer.Sound(path.join(setting.snd_folder, "enemy1_down.wav"))
        self.get_bullet = pygame.mixer.Sound(path.join(setting.snd_folder,"get_bullet.wav"))
        self.bus = info.DataBus()


class GameHelper:
    def __init__(self):
        self.bus = info.DataBus()

    def collision(self):
        """
        全局碰撞检测
        :return:
        """
        # 子弹和敌军碰撞检测
        hits = pygame.sprite.groupcollide(self.bus.hero_bullets, self.bus.enermys, True, True)
        if hits:
            self.handle_collision(hits)

        #  敌机与战机碰撞
        enermys = self.bus.enermys.sprites()
        enermys_hit = pygame.sprite.spritecollide(self.bus.hero, self.bus.enermys, True, pygame.sprite.collide_circle_ratio(0.7))
        # for e in enermys:
        #     pygame.sprite.collide_circle_ratio(0.7)
        #     if pygame.sprite.collide_circle(self.bus.hero, e):

        if enermys_hit:
            # for b, e in hits.items():
            #     for eson in e:
            #         explosion = HeroExplosion('hero', eson.rect.center)
            #         self.bus.add_sprite(explosion)
            # hero.Hero.hide(self.bus.hero)
            # hero.Hero.Lives(self.bus.hero)
            # hero.Hero.shield = 100
                self.bus.is_game_over =True
                print("Game Over...")

        # 敌机子弹和战机碰撞
        enermys_bullets = self.bus.enermy_bullets.sprites()
        for i in enermys_bullets:
            if pygame.sprite.collide_rect(self.bus.hero, i):
                # # 敌人爆炸动画
                # for b, e in hits.items():
                #     for eson in e:
                #         explosion = HeroExplosion('hero', eson.rect.center)
                #         self.bus.add_sprite(explosion)
                # hero.Hero.hide(self.bus.hero)
                # hero.Hero.Lives(self.bus.hero)
                # hero.Hero.shield = 100
                self.bus.is_game_over = True
                print("Game Over...")


        # 战机和火力道具碰撞
        bullet_prop = self.bus.bullet_props.sprites()
        bullet_hit = pygame.sprite.spritecollide(self.bus.hero, self.bus.bullet_props,True, pygame.sprite.collide_circle_ratio(0.7))
        # for k in bullet_prop:
        #     pygame.sprite.collide_circle_ratio(0.7)
        #     if pygame.sprite.collide_circle(self.bus.hero, k):
        #         hero.Hero.powerup(self.bus.hero)
        if bullet_hit:
            hero.Hero.powerup(self.bus.hero)


        # 战机和加血道具碰撞
        bomb_prop = self.bus.bomb_props.sprites()
        bomb_hit = pygame.sprite.spritecollide(self.bus.hero, self.bus.bomb_props, pygame.sprite.collide_circle_ratio(0.8))
        # if bomb_hit:
        #     hero.Hero.(self.bus.hero)

    def handle_collision(self, hits):
        # 加分
        self.bus.add_score(10 * len(hits))
        # 敌人死亡声音
        self.bus.m.play_die_music()

        # 敌人爆炸动画
        for b, e in hits.items():
            for eson in e:
                explosion = Explosion('enermy', eson.rect.center)
                self.bus.add_sprite(explosion)

    def draw_game_over_view(self):
        self.bus.all_sprites.empty()

        game_over_button = Button("gameover.png", -40)
        begin_button = Button("again.png",40)
        self.bus.all_sprites.add(game_over_button)
        self.bus.all_sprites.add(begin_button)

        if Button.check_click(game_over_button):
            sys.exit()

        if Button.check_click(begin_button):
            self.bus.reset()
            self.bus.is_game_over = False


    #     if not self.bus.game_over_button_clicked:
    #         # 绘制重新开始按钮
    #         self.bus.all_sprites.add(self.bus.game_over_button)
    #
    #         if Npc.Button.check_click(self.bus.game_over_button):
    #             # 绘制开始界面
    #             self.bus.game_over_button_clicked = True
    #     else:
    #         self.bus.game_helper.draw_begin_view()
    #
    # def draw_begin_view(self):
    #     self.bus.all_sprites.empty()
    #     begin_button = Npc.Button("again.png")
    #     self.bus.all_sprites.add(begin_button)
    #
    #     if Npc.Button.check_click(begin_button):
    #         self.bus.reset()
    #         self.bus.is_game_over = False
    # def hit_1(self):
    #     """
    #     我方战机子弹击中敌机
    #     :return:
    #     """
    #     hits = pygame.sprite.groupcollide(self.bus.hero_bullets, self.bus.enermys, True, True)
    #     if hits:
    #         # 累计得分
    #         self.add_score("common", hits)
    #          #敌机爆炸音乐
    #         self.plane_blood_snd("common", hits)
    #         # 敌机爆炸效果
    #         self.play_exprosion("common", hits)
    #
    # def add_score(self, type, hits):
    #     if type == "common":
    #         self.score += len(hits) * 10
    #     print("当前得分：%d"% self.score)
    #
    # def plane_blood_snd(self,type,hits):
    #     if type == "common":
    #         for hit in range(len(hits)):
    #             self.die_music.play()
    #             self.die_music.set_volume(10)
    #
    # def play_exprosion(self,type,hits):
    #     if type == "common":
    #         for b, e in hits.items():
    #             for eson in e:
    #                 explosion = Explosion('enermy')
    #                 self.bus.add_sprite(explosion)
    #                 explosion.init(eson.rect.center)


    # def hit_2(self):
    #     """
    #     敌机子弹击中我方战机
    #     :param self:
    #     :return:
    #     """
    #     hits = pygame.sprite.groupcollide(self.bus.enermy_bullets, self.bus.heros, True, True)
    #     if hits:
    #         self.hero_exprosion("common", hits)
    #
    # def hero_exprosion(self, type, hits):
    #     if type == "common":
    #         for v, k in hits.items():
    #             for kson in k:
    #                 explosion = hero.HeroExplosion("me_destroy_", 4, kson.rect.center)
    #                 self.bus.add_sprite(explosion)

    #
    # def hit_3(self):
    #     """
    #     敌机和我方战机碰撞
    #     :return:
    #     """
    #     hits = pygame.sprite.groupcollide(self.bus.heros, self.bus.npcs, True, True)
    #
    # def hit_4(self):
    #     """
    #     我方战机捕获加血道具
    #     :return:
    #     """
    #     hits = pygame.sprite.groupcollide(self.bus.heros, self.bus.bomb_props, True, True)


