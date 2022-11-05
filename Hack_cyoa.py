import random as r
import pygame

pygame.init()
screen = pygame.display.set_mode((640,360))
clock = pygame.time.Clock()

playerDamage = 0

enemyDamage = 0



class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.health = 20
        self.baseDamage = 2
        self.armor = 12
        self.Alive = True
        self.hit = 0

    def attack(self):
        global playerDamage
        self.hit = r.randrange(1,21) + self.baseDamage
        print(" ")
        print("You rolled: " + str(self.hit))
        if self.hit >= mantaRay.armor:
            playerDamage = (r.randrange(1,7)) + self.baseDamage
            mantaRay.health = mantaRay.health - playerDamage
            print("You dealt: " + str(playerDamage))

    def update(self):
        if self.health <= 0:
            if self.Alive == True:
                print("You died!")
                self.Alive = False
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.health = 20
        self.baseDamage = 2
        self.Alive = True
        self.armor = 10
        self.hit = 0

    def attack(self):
        global enemyDamage
        self.hit = r.randrange(1,21) + self.baseDamage
        print(" ")
        print("The enemy rolled: " + str(self.hit))
        if self.hit >= merek.armor:
            enemyDamage = (r.randrange(1,7) + self.baseDamage)
            merek.health = merek.health - enemyDamage
            print("The enemy dealt: " + str(enemyDamage))
    def update(self):
        if self.health <= 0:
            if self.Alive == True:
                print("You killed the enemy!")
                self.Alive = False



merek = Player(0,0)
player_group = pygame.sprite.Group()
player_group.add(merek)

mantaRay = Enemy(0,0)
enemy_group = pygame.sprite.Group()
enemy_group.add(mantaRay)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if merek.health > 0:
                    merek.attack()
                if mantaRay.health > 0:
                    mantaRay.attack()

    pygame.display.flip()
    player_group.update()
    enemy_group.update()
    clock.tick(60)
