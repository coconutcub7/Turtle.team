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
        self.goDown = True
        self.goUp = False


        self.image = pygame.image.load("C:\\Users\\pureb\\Documents\\Some_python\\Ocean Blues\\Turtle.team\\assets\\astur\\merik_defaultA.png")

    
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

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
        
        if self.goDown == True:
            self.rect.y += 1
            self.rect.x += 1
            if self.rect.y >= 170:
                self.goUp = True
                self.goDown = False

        if self.goUp == True:
            self.rect.y -= 1
            self.rect.x -= 1
            if self.rect.y <= 150:
                self.goUp = False
                self.goDown = True
            
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, hp, defense, attack, maxDmg):
        super().__init__()
        self.health = hp
        self.baseDamage = attack
        self.Alive = True
        self.armor = defense
        self.maxDmg = maxDmg
        self.hit = 0
    
    def attack(self):
        global enemyDamage
        self.hit = r.randrange(1,21) + self.baseDamage
        print(" ")
        print("The enemy rolled: " + str(self.hit))
        if self.hit >= merek.armor:
            enemyDamage = (r.randrange(1,self.maxDmg) + self.baseDamage)
            merek.health = merek.health - enemyDamage
            print("The enemy dealt: " + str(enemyDamage))
    def update(self):
        if self.health <= 0:
            if self.Alive == True:
                print("You killed the enemy!")
                self.Alive = False
        



merek = Player(480,180)
player_group = pygame.sprite.Group()
player_group.add(merek)

mantaRay = Enemy(0,0, 20, 10, 2, 7)
enemy_group = pygame.sprite.Group()
enemy_group.add(mantaRay)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if mantaRay.health > 0:
                    if merek.health > 0:
                        merek.attack()
                    if mantaRay.health > 0:
                        mantaRay.attack()

    pygame.display.flip()
    player_group.draw(screen)
    player_group.update()
    enemy_group.update()
    clock.tick(30)
