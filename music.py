# @Time    : 2019/6/15 9:04
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : music.py
# @Software: PyCharm
import pygame
import sys
import setting
import os.path as path


class Music:

    singleton = None
    def __new__(cls, *args, **kwargs):
        if Music.singleton is None:
            Music.singleton = super().__new__(cls, *args, **kwargs)
            Music.singleton.initial()

        return Music.singleton

    def initial(self):
        self.die_music = pygame.mixer.Sound(path.join(setting.snd_folder, "enemy1_down.wav"))
        self.bgm = pygame.mixer.Sound(path.join(setting.snd_folder, 'game_music.ogg'))
        self.shoot_sud = pygame.mixer.Sound(path.join(setting.snd_folder, "bullet.wav"))
        self.enermy_die_music = pygame.mixer.Sound(path.join(setting.snd_folder, "enemy1_down.wav"))

        self.set_config()

    def set_config(self):
        """
        配置音乐
        :return:
        """
        self.bgm.set_volume(0.6)

    def play_die_music(self):
        self.die_music.play()

    def play_bgm(self):
        self.bgm.play(loops=-1)

    def play_shoot_sud(self):
        self.shoot_sud.play()

    def play_enmery_die_music(self):
        self.enermy_die_music.play()







