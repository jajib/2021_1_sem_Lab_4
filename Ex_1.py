# -*- coding: utf-8 -*-
import pygame
import math
from pygame.draw import *

def rotate_point(point, center, angle):
    x_ = center[0] + (point[0] - center[0])*math.cos(angle) - (point[1] - center[1])*math.sin(angle)
    y_ = center[1] + (point[0] - center[0])*math.sin(angle) + (point[1] - center[1])*math.cos(angle)
    return x_, y_

pygame.init()

screen = pygame.display.set_mode((600, 600))

rect(screen, (128, 128, 128), (0, 0, 600, 600))
circle(screen, (0, 0, 0), (300, 300), 201, width=5)
circle(screen, (255, 255, 0), (300, 300), 200)

rect(screen, (0, 0, 0), (200, 400, 200, 40))

#left eye

circle(screen, (0, 0, 0), (200, 250), 31, width=5)
circle(screen, (255, 0, 0), (200, 250), 30)

circle(screen, (0, 0, 0), (200, 250), 16)

#right eye

circle(screen, (0, 0, 0), (400, 250), 21, width=5)
circle(screen, (255, 0, 0), (400, 250), 20)

circle(screen, (0, 0, 0), (400, 250), 11)

#eyebrows

left_eyebrow = ((100, 170), (300, 170), (300, 190), (100, 190))
polygon(screen, (0, 0, 0), [rotate_point(i, (200, 180), math.pi/3.3) for i in left_eyebrow])

right_eyebrow = ((500, 170), (300, 170), (300, 190), (500, 190))
polygon(screen, (0, 0, 0), [rotate_point(i, (400, 180), math.pi*(1 - 1/2.8)) for i in right_eyebrowt_eyebrow])

pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()