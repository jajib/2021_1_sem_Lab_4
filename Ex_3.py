# -*- coding: utf-8 -*-
import pygame
from pygame.draw import *

pygame.init()

disp = pygame.display.set_mode((1070, 800))

screen = pygame.Surface((535, 800))

rect(screen, (170, 238, 255), (0, 0, 1000, 400))
rect(screen, (55, 200, 113), (0, 400, 1000, 400))

#left person

line(screen, (0, 0, 0), (125, 650), (150, 645))
line(screen, (0, 0, 0), (150, 645), (200, 525))

ellipse(screen, (167, 147, 172), (175, 360, 100, 200))

line(screen, (0, 0, 0), (275, 640), (250, 640))
line(screen, (0, 0, 0), (250, 640), (245, 545))

line(screen, (0, 0, 0), (195, 385), (105, 475))

circle(screen, (255, 255, 255), (220, 340), 35)

line(screen, (0, 0, 0), (255, 385), (310, 470))

#right person

line(screen, (0, 0, 0), (385, 650), (405, 650))
line(screen, (0, 0, 0), (405, 650), (410, 545))

line(screen, (0, 0, 0), (480, 652), (452, 650))
line(screen, (0, 0, 0), (452, 650), (452, 545))

line(screen, (0, 0, 0), (310, 470), (428, 380))

polygon(screen, (255, 85, 221), ((365, 550), (500, 550), (432, 360)))
circle(screen, (255, 255, 255), (432, 335), 35)

line(screen, (0, 0, 0), (440, 380), (485, 430))
line(screen, (0, 0, 0), (485, 430), (535, 390))

f_screen = pygame.transform.flip(screen, True, False)
pygame.Surface.blit(disp, screen, (0, 0))
pygame.Surface.blit(disp, f_screen, (535, 0))

line(disp, (0, 0, 0), (110, 480), (70, 335))
polygon(disp, (255, 0, 0), ((70, 335), (25, 270), (100, 255)))
circle(disp, (255, 0, 0), (40, 260), 25)
circle(disp, (255, 0, 0), (80, 245), 25)

line(disp, (0, 0, 0), (535, 390), (547, 203))
polygon(disp, (255, 204, 0), ((547, 203), (490, 100), (600, 90)))
ellipse(disp, (0, 0, 0), (490, 67, 55, 48))
ellipse(disp, (255, 0, 0), (545, 60, 54, 50))
ellipse(disp, (255, 255, 255), (514, 25, 57, 59))

polygon(disp, (255, 204, 0), ((965, 485), (965, 410), (1020, 436)))
ellipse(disp, (0, 0, 0), (967, 400, 27, 35))
ellipse(disp, (255, 0, 0), (995, 397, 30, 43))
ellipse(disp, (255, 255, 255), (980, 375, 35, 45))

pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()