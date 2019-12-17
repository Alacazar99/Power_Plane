# @Time    : 2019/6/2 11:24
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : information.py
# @Software: PyCharm
import pygame
import hero
import music
import hit
import setting
# from Npc import Explosion

class DataBus:
    instance = None


    def __new__(cls, *args, **kwargs):
        if DataBus.instance is None:
            DataBus.instance = super().__new__(cls)
            DataBus.instance.reset()


        return DataBus.instance

    def reset(self):

        self.score = 0
        self.is_game_over = False

        self.all_sprites = pygame.sprite.Group()
        self.hero_bullets = pygame.sprite.Group()

        self.enermy_bullets = pygame.sprite.Group()
        self.heros = pygame.sprite.Group()
        self.enermys = pygame.sprite.Group()
        self.bomb_props = pygame.sprite.Group()
        self.bullet_props = pygame.sprite.Group()
        self.m = music.Music()
        self.game_helper = hit.GameHelper()
        # self.game_over_button = Npc.Button("gameover.png")
        # self.game_over_button_clicked = False

        # 初始化英雄
        self.__init_hero()

    def __init_hero(self):
        """
        初始化英雄
        :return:
        """
        self.hero = hero.Hero()
        self.add_sprite(self.hero)

    def add_sprite(self,sprite):
        self.all_sprites.add(sprite)

    def remove_sprite(self,sprite):
        self.all_sprites.remove(sprite)

    def add_hero_bullet(self,hero_bullet):
        self.hero_bullets.add(hero_bullet)

    def add_npc_bullet(self,npc_bullet):
        self.enermy_bullets.add(npc_bullet)

    def add_hero(self,hero):
        self.heros.add(hero)

    def add_enermy(self,enermy):
        self.enermys.add(enermy)

    def add_bomb_prop(self,prop):
        self.bomb_props.add(prop)

    def add_bullet_prop(self,prop):
        self.bullet_props.add(prop)

    def add_score(self,score):
        self.score += score
        num_score = self.score

        print("当前得分：%d" % self.score)


    def draw_text(self, screen):
        font1 = pygame.font.Font(16, True)
        screen.blit(font1.render(u'当前得分：%d' % self.score, True,'red'), [20, 20])





    # def add_score(self,type,hits):
    #     if type == "common":
    #         self.score += len(hits) * 10
    #     print("当前得分：%d"% self.score)
    #
    # def plane_blood_snd(self,type,hits):
    #
    #     if type == "common":
    #         for hit in range(len(hits)):
    #             self.die_music.play()
    #             self.die_music.set_volume(10)
    #
    # def play_exprosion(self,type,hits):
    #     if type == "common":
    #         for b,e in hits.items():
    #             for eson in e:
    #                 explosion = Explosion('enemy1_down', 4, eson.rect.center)
    #                 DataBus().add_sprite(explosion)
