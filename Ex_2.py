# -*- coding: utf-8 -*-
import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((1000, 800))

rect(screen, (170, 238, 255), (0, 0, 1000, 400))
rect(screen, (55, 200, 113), (0, 400, 1000, 400))

#left person

line(screen, (0, 0, 0), (190, 720), (230, 715))
line(screen, (0, 0, 0), (230, 715), (300, 520))

ellipse(screen, (167, 147, 172), (250, 235, 150, 300))

line(screen, (0, 0, 0), (420, 710), (380, 708))
line(screen, (0, 0, 0), (380, 708), (356, 514))

line(screen, (0, 0, 0), (280, 273), (147, 431))

polygon(screen, (255, 204, 0), ((160, 430), (155, 330), (73, 385)))
ellipse(screen, (0, 0, 0), (70, 340, 45, 40))
ellipse(screen, (255, 0, 0), (94, 316, 55, 40))
ellipse(screen, (255, 255, 255), (55, 300, 55, 45))

circle(screen, (255, 255, 255), (330, 200), 70)

line(screen, (0, 0, 0), (375, 280), (480, 420))

#right person

line(screen, (0, 0, 0), (600, 700), (640, 700))
line(screen, (0, 0, 0), (640, 700), (640, 540))

line(screen, (0, 0, 0), (750, 700), (709, 699))
line(screen, (0, 0, 0), (709, 699), (709, 540))

line(screen, (0, 0, 0), (480, 420), (670, 270))

polygon(screen, (255, 85, 221), ((570, 550), (790, 550), (680, 230)))
circle(screen, (255, 255, 255), (680, 190), 60)

line(screen, (0, 0, 0), (690, 270), (765, 330))
line(screen, (0, 0, 0), (765, 330), (850, 280))

line(screen, (0, 0, 0), (843, 317), (885, 160))
polygon(screen, (255, 0, 0), ((880, 170), (880, 85), (950, 120)))
circle(screen, (255, 0, 0), (903, 85), 23)
circle(screen, (255, 0, 0), (940, 100), 23)

pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()