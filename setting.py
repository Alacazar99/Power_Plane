
import os.path as path
import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# 工程目录
print(__file__)
project_folder = path.dirname(__file__)

img_folder = path.join(project_folder,"plane/images")
snd_folder = path.join(project_folder,"plane/sound")
print(img_folder)

