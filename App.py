# @Time    : 2019/6/2 9:03
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : App.py
# @Software: PyCharm

import pygame
import sys
import hero
import os.path as path
import setting
from information import DataBus
from Npc import EnermyFactory
from Npc import Button
from prop import PropFactory
import hit
# import music

class App:

    def start(self):
        pygame.init()    # 启动pygame
        pygame.mixer.init()
        # 确定游戏界面
        screen = pygame.display.set_mode((400, 600))

        # 设置帧率
        clock = pygame.time.Clock()
        bus = DataBus()
        # 设置游戏名称
        pygame.display.set_caption("外星人入侵")
        # 设置游戏背景
        # bg_img = pygame.image.load(path.join(setting.img_folder, "background.png")).convert()
        bg_img = pygame.image.load(path.join(setting.img_folder, "789.jpg")).convert()
        # bg_img = pygame.image.load(path.join(setting.img_folder, "888.png")).convert()
        screen.blit(bg_img,(0,0))

        # 设置游戏背景音乐
        bgm = pygame.mixer.Sound(path.join(setting.snd_folder,'game_music.ogg'))
        bgm.set_volume(0.5)
        bgm.play(loops = -1)
        # 调用

        ef = EnermyFactory()
        pp = PropFactory()
        transColor = pygame.Color(0, 0, 0)
        player_img = pygame.image.load(path.join(setting.img_folder, "me1.png")).convert()

        player_mini_img = pygame.transform.scale(player_img, (25, 30))
        player_mini_img.set_colorkey(transColor)

        game_font = pygame.font.SysFont('arial', 24, True)


        # 让渲染结果一次显示
        pygame.display.flip()

        while True:
            screen.blit(bg_img, (0, 0))
            clock.tick(30)
            if not bus.is_game_over:
                # 制造敌机
                ef.generate_enermy()
                # 制造道具
                pp.generate_bomb_prop()
                pp.generate_bullet_prop()

                # 更新坐标（核心）
                bus.all_sprites.update()
                # 映射到屏幕
                bus.all_sprites.draw(screen)
                # 碰撞检测: 玩家子弹和敌机
                bus.game_helper.collision()
                screen.blit(game_font.render(u'%d' % bus.score, True, [255, 0, 0]), [20, 20])
                hero.Hero.draw_lives(screen, 300, 20, 3, player_mini_img)

                # 让渲染结果一次显示
                pygame.display.flip()

            if bus.is_game_over:
                bg_img = pygame.image.load(path.join(setting.img_folder, "888.png")).convert()
                screen.blit(bg_img, (0, 0))
                bus.game_helper.draw_game_over_view()

            bus.all_sprites.draw(screen)
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 游戏关闭
                    sys.exit()

App().start()
# 定义一个碰撞模块 hit.py
# hits = pygame.sprite.groupcollide(bus.hero_bullets, bus.enermys, True, True)
# # print(len(hits))
# if hits:
#     # 累计得分
#     bus.add_score("common",hits)
#     # 敌机爆炸音乐
#     bus.plane_blood_snd("common",hits)
#     # 敌机爆炸效果
#     bus.play_exprosion("common",hits)