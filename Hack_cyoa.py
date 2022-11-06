import random as r
import pygame
from math import floor

pygame.init()
screen = pygame.display.set_mode((640,360))
clock = pygame.time.Clock()
background = pygame.image.load("assets\\astur\\real_real.jpg")
background = pygame.transform.scale(background, (640, 360))
menu = pygame.image.load("assets\\sprites\\menu_defaultA.png")
menu = pygame.transform.scale(menu, (464, 240))


#Variables to keep a global track of damage throughout game
playerDamage = 0
enemyDamage = 0



class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        #Initiating variables for the player, who is Merek
        self.health = 20
        self.baseDamage = 2
        self.armor = 12
        self.Alive = True
        self.hit = 0
        self.goDown = True
        self.goUp = False
        self.defending = False


        self.image = pygame.image.load("C:\\Users\\pureb\\Documents\\Some_python\\Ocean Blues\\Turtle.team\\assets\\astur\\merik_defaultA.png")

    
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def attack(self): 
        global playerDamage #Damage that will be applied to the enemy
        self.hit = r.randrange(1,21) + self.baseDamage
        print(" ")
        print("You rolled: " + str(self.hit))
        if self.hit >= mantaRay.armor:
            playerDamage = (r.randrange(1,7)) + self.baseDamage
            mantaRay.health = mantaRay.health - playerDamage
            print("You dealt: " + str(playerDamage))

    def defend(self):
        self.armor += 5
        self.defending = True

    def update(self): #Continously checking the sprite and their variables the entire time the game is active
        if self.health <= 0: #Checks their Health
            if self.Alive == True:
                print("You died!")
                self.Alive = False
        
        if self.goDown == True: #Sprite moves down
            self.rect.y += 1
            self.rect.x += 1
            if self.rect.y >= 120:
                self.goUp = True
                self.goDown = False

        if self.goUp == True: #Sprite begins moving up
            self.rect.y -= 1
            self.rect.x -= 1
            if self.rect.y <= 100:
                self.goUp = False
                self.goDown = True     
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, hp, defense, attack, maxDmg):
        super().__init__()
        self.health = hp
        self.baseDamage = attack
        self.Alive = True
        self.attackTime = None
        self.armor = defense
        self.maxDmg = maxDmg
        self.wizardMan = False

        imgOne = pygame.image.load("C:\\Users\\pureb\\Documents\\Some_python\\Ocean Blues\\Turtle.team\\assets\\sprites\\stingray_defaultA.png")
        imgOne = pygame.transform.flip(imgOne, True, False)
        self.image = imgOne
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        imgTwo = pygame.transform.flip(pygame.image.load("C:\\Users\\pureb\\Documents\\Some_python\\Ocean Blues\\Turtle.team\\assets\\sprites\\stingray_WizardA.png"), True, False)
        imgThree = pygame.image.load("C:\\Users\\pureb\\Documents\\Some_python\\Ocean Blues\\Turtle.team\\assets\\sprites\\stingray_WizardB.png")
        imgFour = pygame.image.load("C:\\Users\\pureb\\Documents\\Some_python\\Ocean Blues\\Turtle.team\\assets\\sprites\\stingray_WizardC.png")
        self.listimage = []
        self.listimage.append(imgOne)
        self.listimage.append(imgTwo)
        self.listimage.append(pygame.transform.flip(imgThree, True, False))
        self.listimage.append(pygame.transform.flip(imgFour, True, False))
        self.currentimage = 1

        self.goDown = False
        self.goUp = True

        self.hit = 0
    
    def attack(self):
        global enemyDamage
        self.attackTime = True
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
        if self.wizardMan == True:
            if self.attackTime == True:
                self.currentimage += 0.1
                self.image = self.listimage[int(self.currentimage)]
                if self.currentimage >= 3.5:
                    self.attackTime = False
            if self.attackTime == False:
                self.currentimage -= 0.1
                self.image = self.listimage[int(self.currentimage)]
                if self.currentimage <= 1:
                    self.attackTime = None


        if self.goDown == True:
            self.rect.y += 1
            if self.rect.y >= 120:
                self.goDown = False
                self.goUp = True
        
        if self.goUp == True:
            self.rect.y -= 1
            if self.rect.y <= 90:
                self.goDown = True
                self.goUp = False

        if self.wizardMan == False:
            if self.health <= 40:
                self.image = self.listimage[1]
                self.wizardMan = True

class Arrow(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("assets\\sprites\\arrow.png")
        self.image = pygame.transform.scale(self.image, (105, 95))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.goDown = False
        self.goUp = True
        self.rightness = 1

    def move_right(self):
        if self.rightness < 3:
            self.rect.x += 145
            self.rightness += 1
    def move_left(self):
        if self.rightness > 1:
            self.rect.x -= 145
            self.rightness -= 1

    def update(self):
        if self.goDown == True:
            self.rect.y += 1
            if self.rect.y >= 225:
                self.goDown = False
                self.goUp = True
        
        if self.goUp == True:
            self.rect.y -= 1
            if self.rect.y <= 215:
                self.goDown = True
                self.goUp = False



merek = Player(480,130)
player_group = pygame.sprite.Group()
player_group.add(merek)

arrow = Arrow(165, 270)
menu_assets = pygame.sprite.Group()
menu_assets.add(arrow)

mantaRay = Enemy(140,130, 50, 10, 2, 7)
enemy_group = pygame.sprite.Group()
enemy_group.add(mantaRay)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if arrow.rightness == 1:
                    if merek.defending == True:
                        merek.armor -= 5
                        print(' ')
                        print("Your guard dropped!")
                        merek.defending = False
                    if mantaRay.health > 0:
                        if merek.health > 0:
                            if merek.health > 0:
                                merek.attack()
                            if mantaRay.health > 0:
                                mantaRay.attack()
                if arrow.rightness == 2:
                    merek.defend()
                    print(' ')
                    print("Your guard is up!")
                    merek.health += 2
                    if mantaRay.health > 0:
                        if merek.health > 0:
                                mantaRay.attack()
            if event.key == pygame.K_RIGHT:
                arrow.move_right()
            if event.key == pygame.K_LEFT:
                arrow.move_left()

    pygame.display.flip()
    screen.blit(background, (0,0))
    screen.blit(menu, (85,120))
    player_group.draw(screen)
    enemy_group.draw(screen)
    menu_assets.draw(screen)
    player_group.update()
    enemy_group.update()
    menu_assets.update()
    clock.tick(20)