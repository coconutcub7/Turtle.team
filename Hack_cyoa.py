import random as r
import pygame

pygame.init()
screen = pygame.display.set_mode((640,360))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    print("hello. Mi llamo tortilla.")