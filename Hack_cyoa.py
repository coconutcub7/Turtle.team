import random as r
import pygame

pygame.init()
screen = pygame.display.set_mode((640,360))
clock = pygame.time.Clock()

playerDamage = 0




class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.health = 20
        self.baseDamage = 2

    def attack(self):
        global playerDamage
        playerDamage = (r.randrange(1,7)) + self.baseDamage
        print(playerDamage)
        

player = Player(0,0)
player_group = pygame.sprite.Group()
player_group.add(player)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.attack()