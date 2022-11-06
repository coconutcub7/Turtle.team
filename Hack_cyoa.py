import random as r
import pygame
from math import floor

pygame.init()
playmusic = pygame.mixer.Channel(1)
background = pygame.image.load("assets\\backgrounds\\background_encounter1.png")
menu = pygame.image.load("assets\\sprites\\menu_defaultA.png")
menu = pygame.transform.scale(menu, (464, 240))
normalMenu = menu
leftArrow = pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic_leftarrow1.png"), (367, 204))
rightArrow = pygame.transform.scale(pygame.image.load("assets\sprites\menu_magic_rightarrow1.png"), (367, 204))
selectedLeftArrow = pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic_leftarrow0.png"), (367, 204))
selectedRightArrow = pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic_rightarrow0.png"), (367, 204))
currentRightArrow = rightArrow
currentLeftArrow = leftArrow

vampireMusic = pygame.mixer.Sound("assets\\music\\encounter 3\\squid_battle.wav")

finalBossMusic = pygame.mixer.Sound("assets\\music\\organ\\organ_mixdown.wav")

lightning1 = pygame.image.load("assets\\sprites\\lightning_assetA.png")
lightning2 = pygame.image.load("assets\\sprites\\lightning_assetB.png")
lightning3 = pygame.image.load("assets\\sprites\\lightning_assetC.png")

#Variables to keep a global track of damage throughout game
playerDamage = 0
enemyDamage = 0

remainingCharges1 = 0
remainingCharges2 = 0
remainingCharges3 = 0
enemyApproaches = pygame.mixer.Sound("assets\\music\\encounter_1\\approach.wav")
enemyBattle = pygame.mixer.Sound("assets\\music\\encounter_1\\Battle.wav")
enemyEncounter = pygame.mixer.Sound("assets\\music\\encounter_1\\encounter.wav")



class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        #Initiating variables for the player, who is Merek
        self.health = 200
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
        if mantaRay in enemy_group:
            if self.hit >= mantaRay.armor:
                playerDamage = (r.randrange(1,7)) + self.baseDamage
                mantaRay.health = mantaRay.health - playerDamage
        if dragon_fish in enemy_group:
            if self.hit >= dragon_fish.armor:
                playerDamage = (r.randrange(1,7)) + self.baseDamage
                dragon_fish.health = dragon_fish.health - playerDamage
        if vampiir in enemy_group:
            if self.hit >= vampiir.armor:
                playerDamage = (r.randrange(1,7)) + self.baseDamage
                vampiir.health = vampiir.health - playerDamage
        if angler_fish in enemy_group:
            if self.hit >= dragon_fish.armor:
                playerDamage = (r.randrange(1,7)) + self.baseDamage
                angler_fish.health = angler_fish.health - playerDamage
        if final in enemy_group:
            if self.hit >= final.armor:
                playerDamage = (r.randrange(1,7)) + self.baseDamage
                final.health = final.health - playerDamage
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
        
class MantaRay(pygame.sprite.Sprite):
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
        special_effects.add(bolt)
        self.hit = r.randrange(1,21) + self.baseDamage
        print(" ")
        print("The enemy rolled: " + str(self.hit))
        if self.hit >= merek.armor:
            enemyDamage = (r.randrange(1,self.maxDmg) + self.baseDamage)
            merek.health = merek.health - enemyDamage
            print("The enemy dealt: " + str(enemyDamage))
            print("You have " + str(merek.health) + " HP left!")
    def update(self):
        if self.health <= 0:
            if self.Alive == True:
                print("You killed the enemy!")
                self.Alive = False
                EndOne()
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
                    bolt.kill()
                    bolt.rect.x = 140
                    bolt.image = lightning1


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

class Lightning(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        global lightning1, lightning2, lightning3

        self.image = lightning1
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def update(self):
        global lightning1, lightning2, lightning3
        if 2 >= mantaRay.currentimage <3:
            self.image = lightning2
            self.rect.x = 240
        if mantaRay.currentimage >= 3:
            self.image = lightning3
            self.rect.x = 480

class Arrow(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        global remainingCharges1, remainingCharges2, remainingCharges3

        self.image = pygame.image.load("assets\\sprites\\arrow.png")
        self.image = pygame.transform.scale(self.image, (105, 95))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.goDown = False
        self.goUp = True
        self.rightness = 1
        self.inMagicMenu = False
        self.triggerOnce = False
        self.magicMenu1 = []
        self.magicMenu1.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic4.png"), (464, 240)))
        self.magicMenu1.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic3.png"), (464, 240)))
        self.magicMenu1.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic2.png"), (464, 240)))
        self.magicMenu1.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic1.png"), (464, 240)))
        self.magicMenu1.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic0.png"), (464, 240)))
        remainingCharges1 = 0


        self.magicMenu2 = []
        self.magicMenu2.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic4.png"), (464, 240)))
        self.magicMenu2.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic3.png"), (464, 240)))
        self.magicMenu2.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic2.png"), (464, 240)))
        self.magicMenu2.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic1.png"), (464, 240)))
        self.magicMenu2.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic0.png"), (464, 240)))
        remainingCharges2 = 0



        self.magicMenu3 = []
        self.magicMenu3.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic4.png"), (464, 240)))
        self.magicMenu3.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic3.png"), (464, 240)))
        self.magicMenu3.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic2.png"), (464, 240)))
        self.magicMenu3.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic1.png"), (464, 240)))
        self.magicMenu3.append(pygame.transform.scale(pygame.image.load("assets\\sprites\\menu_magic0.png"), (464, 240)))
        remainingCharges3 = 0


        self.magicMenus = []
        self.magicMenus.append(self.magicMenu1)
        self.magicMenus.append(self.magicMenu2)
        self.magicMenus.append(self.magicMenu3)
        self.defaultMenu = normalMenu


    def move_right(self):
        global leftArrow, rightArrow, selectedRightArrow, selectedLeftArrow, currentRightArrow
        if self.inMagicMenu == False:
            if self.rightness < 3:
                self.rect.x += 145
                self.rightness += 1
        if self.inMagicMenu == True:
            currentRightArrow = selectedRightArrow

    def move_left(self):
        if self.inMagicMenu == False:
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

class dragonFish(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, hp, defense, attack, maxDmg):
        super().__init__()
        self.health = hp
        self.baseDamage = attack
        self.Alive = True
        self.attackTime = None
        self.armor = defense
        self.maxDmg = maxDmg

        imgOne = pygame.image.load("assets\\sprites\\dragonfish_defaultA.png")
        self.image = pygame.transform.scale2x(imgOne)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        imgTwo = pygame.image.load("assets\\sprites\\dragonfish_defaultB.png")
        imgThree = pygame.image.load("assets\\sprites\\dragonfish_defaultC.png")
        self.listimage = []
        self.listimage.append(pygame.transform.scale2x(imgOne))
        self.listimage.append(pygame.transform.scale2x(imgTwo))
        self.listimage.append(pygame.transform.scale2x(imgThree))
    
        self.currentimage = 0

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
            print("You have " + str(merek.health) + " HP left!")
    def update(self):
        if self.health <= 0:
            if self.Alive == True:
                print("You killed the enemy!")
                self.Alive = False
                EndTwo()
        if self.attackTime == True:
            self.currentimage += 0.1
            self.image = self.listimage[int(self.currentimage)]
            if self.currentimage >= 2.5:
                self.attackTime = False
        if self.attackTime == False:
            self.currentimage -= 0.1
            self.image = self.listimage[int(self.currentimage)]
            if self.currentimage <= 0:
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

class vampire(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, hp, defense, attack, maxDmg):
        super().__init__()
        self.health = hp
        self.baseDamage = attack
        self.Alive = True
        self.attackTime = None
        self.armor = defense
        self.maxDmg = maxDmg

        imgOne = pygame.transform.scale2x(pygame.image.load("assets\\sprites\\vampiresquid_defaultA.png"))
        imgTwo = pygame.transform.scale2x(pygame.image.load("assets\\sprites\\vampiresquid_defaultB.png"))
        self.image = pygame.transform.flip(imgOne, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.listimage = []
        self.listimage.append(pygame.transform.flip(imgOne, True, False))
        self.listimage.append(pygame.transform.flip(imgTwo, True, False))
    
        self.currentimage = 0

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
            print("You have " + str(merek.health) + " HP left!")
    def update(self):
        if self.health <= 0:
            if self.Alive == True:
                print("You killed the enemy!")
                self.Alive = False
                EndThree()
        if self.attackTime == True:
            self.currentimage += 0.1
            self.image = self.listimage[int(self.currentimage)]
            print(self.currentimage)
            if self.currentimage >= 1.5:
                self.attackTime = False
        if self.attackTime == False:
            self.currentimage -= 0.1
            self.image = self.listimage[int(self.currentimage)]
            print(self.currentimage)
            if self.currentimage <= 0.2:
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

class anglerFish(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, hp, defense, attack, maxDmg):
        super().__init__()
        self.health = hp
        self.baseDamage = attack
        self.Alive = True
        self.attackTime = None
        self.armor = defense
        self.maxDmg = maxDmg

        imgThree = pygame.transform.scale2x(pygame.image.load("assets\\sprites\\anglerfish_defaultA.png"))
        imgTwo = pygame.transform.scale2x(pygame.image.load("assets\\sprites\\anglerfish_defaultB.png"))
        imgOne = pygame.transform.scale2x(pygame.image.load("assets\\sprites\\anglerfish_defaultC.png"))
        self.image = pygame.transform.flip(imgOne, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.listimage = []
        self.listimage.append(pygame.transform.flip(imgOne, True, False))
        self.listimage.append(pygame.transform.flip(imgTwo, True, False))
        self.listimage.append(pygame.transform.flip(imgThree, True, False))
    
        self.currentimage = 0

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
            print("You have " + str(merek.health) + " HP left!")
    def update(self):
        if self.health <= 0:
            if self.Alive == True:
                print("You killed the enemy!")
                self.Alive = False
                EndFour()
        if self.attackTime == True:
            self.currentimage += 0.1
            self.image = self.listimage[int(self.currentimage)]
            if self.currentimage >= 2.5:
                self.attackTime = False
        if self.attackTime == False:
            self.currentimage -= 0.1
            self.image = self.listimage[int(self.currentimage)]
            if self.currentimage <= 0:
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

class Leviathin(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, hp, defense, attack, maxDmg):
        super().__init__()
        self.health = hp
        self.baseDamage = attack
        self.Alive = True
        self.attackTime = None
        self.armor = defense
        self.maxDmg = maxDmg

        imgOne = pygame.transform.scale(pygame.image.load("assets\\sprites\\leviathan_defaultA.png"), (250,250))
        imgTwo = pygame.transform.scale(pygame.image.load("assets\\sprites\\leviathan_defaultB.png"), (250,250))
        imgThree = pygame.transform.scale(pygame.image.load("assets\\sprites\\leviathan_defaultC.png"), (250,250))
        self.image = imgOne
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.listimage = []
        self.listimage.append(imgOne)
        self.listimage.append(imgTwo)
        self.listimage.append(imgThree)
    
        self.currentimage = 0

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
            print("You have " + str(merek.health) + " HP left!")
    def update(self):
        if self.health <= 0:
            if self.Alive == True:
                print("You killed the enemy!")
                self.Alive = False
        if self.attackTime == True:
            self.currentimage += 0.1
            self.image = self.listimage[int(self.currentimage)]
            if self.currentimage >= 2.5:
                self.attackTime = False
        if self.attackTime == False:
            self.currentimage -= 0.1
            self.image = self.listimage[int(self.currentimage)]
            if self.currentimage <= 0:
                self.attackTime = None


        if self.goDown == True:
            self.rect.y += 1
            if self.rect.y >= 0:
                self.goDown = False
                self.goUp = True
        
        if self.goUp == True:
            self.rect.y -= 1
            if self.rect.y <= -30:
                self.goDown = True
                self.goUp = False

class Magic(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        imgOne = pygame.image.load("assets\\sprites\\magicparticles_asset1.png")
        imgTwo = pygame.image.load("assets\\sprites\\magicparticles_asset2.png")
        imgThree = pygame.image.load("assets\\sprites\\magicparticles_asset3.png")
        self.heal = 15
        self.baseDamage = 3
        self.turnCount = 0
        self.castedDaze = False
        self.image = imgOne
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.wait = 0


        self.magicList = []
        self.magicList.append(imgOne)
        self.magicList.append(imgTwo)
        self.magicList.append(imgThree)

    def healing(self):
        special_effects.add(mejik)
        merek.health += self.heal
        self.wait = 0
        print("Healed " + str(self.heal) + " HP!")
        self.image = self.magicList[0]
        self.rect.x = 480
        self.rect.y = 130
    def damage(self):
        special_effects.add(mejik)
        self.wait = 0
        print("You cast arcane bolt!")
        self.image = self.magicList[1]
        self.rect.x = 140
        if mantaRay in enemy_group:
            playerDamage = (r.randrange(5,11)) + self.baseDamage
            mantaRay.health = mantaRay.health - playerDamage
            print("Arcane bolt dealt " + str(playerDamage) + " Damage!")
        if dragon_fish in enemy_group:
            playerDamage = (r.randrange(5,11)) + self.baseDamage
            dragon_fish.health = dragon_fish.health - playerDamage
            print("Arcane bolt dealt " + str(playerDamage) + " Damage!")
        if vampiir in enemy_group:
            playerDamage = (r.randrange(5,11)) + self.baseDamage
            vampiir.health = vampiir.health - playerDamage
            print("Arcane bolt dealt " + str(playerDamage) + " Damage!")
        if angler_fish in enemy_group:
            playerDamage = (r.randrange(5,11)) + self.baseDamage
            angler_fish.health = angler_fish.health - playerDamage
            print("Arcane bolt dealt " + str(playerDamage) + " Damage!")
        if final in enemy_group:
            playerDamage = (r.randrange(5,11)) + self.baseDamage
            final.health = final.health - playerDamage
            print("Arcane bolt dealt " + str(playerDamage) + " Damage!")
    def daze(self):
        special_effects.add(mejik)
        self.wait = 0
        if self.castedDaze == False:
            self.image = self.magicList [2]
            self.rect.x = 140
            print("You daze the enemy! You are able to evade their attack more easily for 3 turns.")
            self.turnCount = 1
            merek.armor += 4
            self.castedDaze = True

    def update(self):
        if self.turnCount == 3:
            print("Daze ran off the enemy!")
            merek.armor -= 4
        if self.wait <=20:
            self.wait += 1
        else:
            mejik.kill()

        
def choicesOne():
    print("The radio begins to buzz.")
    print("1. Answer")
      #explaination of lifesteal and where it may be useful
    print("2. Ignore") 
      #less chance of beating the game (skips right to post-stingray magic collection)
     #post-stingray magic collection
    #1. collect stingray magic 
      #-> +2 mag, -1 ac
    #2. don't touch magic
 #- signal from team: dive deeper (effectively an explore round, you gain +1 lifesteal xp) 
    #1. where?
      #-> to the magma trenches. your reads indicate something promising in that direction
    answerOne = int(input('Choose 1 or 2: '))
    if answerOne == 1:
        print('Captain: "Afternoon Merek. We are radioing you to ask you if you encountered any strange red jewels."')
        print('"No... Why?')
        print('Captain: "Its because some of those red jewels can grant a potent magic, known as lifesteal."')
        print('"Lifsteal?"')
        print('Captain: "Precisely. It would be useful to collect them and bring them back to base. Or should you be in danger..."')
        print('Captain:"You could use them to save yer lifee."')
        input(' ')
        print('"Ill be sure to keep that in mind. Ill be returning to the mission then."')
        print('Captain: "Good luck."')
        print('You put the radio away, swimming deeper in the ocean. Before you encounter a strange stingray.')
    else:
        print('You put the radio away instead. Focusing on the task ahead first.')


merek = Player(480,130)
player_group = pygame.sprite.Group()
player_group.add(merek)

arrow = Arrow(165, 270)
menu_assets = pygame.sprite.Group()
menu_assets.add(arrow)

bolt = Lightning(140, 130)
mejik = Magic(0,0)
special_effects = pygame.sprite.Group()
special_effects.add(mejik)

mantaRay = MantaRay(140,130, 10, 10, 2, 7)
dragon_fish = dragonFish(140, 130, 10, 12, 3, 8)
vampiir = vampire(140, 130, 10, 13, 3, 9)
angler_fish = anglerFish(140, 130, 50, 15, 4, 10)
final = Leviathin(100, 80, 80, 10, 12, 10)
enemy_group = pygame.sprite.Group()
enemy_group.add(mantaRay)

def EndOne():
    pygame.display.quit()
    playmusic.stop()
    mantaRay.kill()
    SceneTwo()

def EndTwo():
    pygame.display.quit()
    playmusic.stop()
    dragon_fish.kill()
    SceneThree()

def EndThree():
    pygame.display.quit()
    playmusic.stop()
    vampiir.kill()
    SceneFour()

def EndFour():
    pygame.display.quit()
    playmusic.stop()
    angler_fish.kill()
    SceneFive()


def SceneOne():
    screen = pygame.display.set_mode((640,360))
    clock = pygame.time.Clock()
    #Before the sting ray battle
    #Scenery, dialogue, etc. for the lead up before tutorial-esque battle.
    background = pygame.image.load("assets\\backgrounds\\background_encounter1.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    choicesOne()
                    EncounterOne()
        
        pygame.display.flip()
        screen.blit(background, (0,0))
        clock.tick(20)

def SceneTwo():
    
    #Scenery before the dragun
    background = pygame.image.load("assets\\backgrounds\\background_encounter2.png")
    screen = pygame.display.set_mode((640,360))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #Insert the story/plot as functions under this line of code
                    EncounterTwo()
        
        pygame.display.flip()
        screen.blit(background, (0,0))
        clock.tick(20)
    
def SceneThree():
    background = pygame.image.load("assets\\backgrounds\\background_encounter3.png")
    screen = pygame.display.set_mode((640,360))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #Insert the story/plot as functions under this line of code
                    EncounterThree()
        
        pygame.display.flip()
        screen.blit(background, (0,0))
        clock.tick(20)

def SceneFour():
    background = pygame.image.load("assets\\backgrounds\\background_encounter4.png")
    screen = pygame.display.set_mode((640,360))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #Insert the story/plot as functions under this line of code
                    EncounterFour()
        
        pygame.display.flip()
        screen.blit(background, (0,0))
        clock.tick(20)

def SceneFive():
    background = pygame.image.load("assets\\backgrounds\\background_encounter5.png")
    screen = pygame.display.set_mode((640,360))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #Insert the story/plot as functions under this line of code
                    EncounterFive()
        
        pygame.display.flip()
        screen.blit(background, (0,0))
        clock.tick(20)


def EncounterOne():
    global menu, remainingCharges1, remainingCharges2, remainingCharges3,currentLeftArrow, currentRightArrow
    screen = pygame.display.set_mode((640,360))
    clock = pygame.time.Clock()
    playmusic.play(enemyBattle, -1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    arrow.inMagicMenu = False
                    arrow.rightness = 3
                    menu = arrow.defaultMenu
                if event.key == pygame.K_RETURN:
                    if arrow.inMagicMenu == True:
                        if currentRightArrow == selectedRightArrow:
                            if menu in arrow.magicMenu2:
                                menu = arrow.magicMenus[2][remainingCharges3]
                            if menu in arrow.magicMenu1:
                                menu = arrow.magicMenus[1][remainingCharges2]
                        if currentLeftArrow == selectedLeftArrow:
                            if menu in arrow.magicMenu2:
                                menu = arrow.magicMenus[0][remainingCharges1]
                            if menu in arrow.magicMenu3:
                                menu = arrow.magicMenus[1][remainingCharges2]
                        if currentLeftArrow == leftArrow and currentRightArrow == rightArrow:
                            if menu in arrow.magicMenu1:
                                if remainingCharges1 != 4:
                                    remainingCharges1 += 1
                                    menu = arrow.magicMenus[0][remainingCharges1]
                                    mejik.healing()
                                else:
                                    print("Out of magic!")
                            if menu in arrow.magicMenu2:
                                if remainingCharges2 != 4:
                                    remainingCharges2 += 1
                                    menu = arrow.magicMenus[1][remainingCharges2]
                                    mejik.damage()
                                else:
                                    print("Out of magic!")
                            if menu in arrow.magicMenu3:
                                if remainingCharges3 != 4:
                                    remainingCharges3 += 1
                                    menu = arrow.magicMenus[2][remainingCharges3]
                                    mejik.daze()
                                else:
                                    print("Out of magic!")

                                


                    if arrow.inMagicMenu == False:
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
                        if arrow.rightness == 3:
                            menu = arrow.magicMenus[0][remainingCharges1]
                            arrow.inMagicMenu = True
                            arrow.rightness = 5

                if event.key == pygame.K_RIGHT:
                    arrow.move_right()
                if event.key == pygame.K_LEFT:
                    if arrow.inMagicMenu == False:
                        arrow.move_left()
                    if arrow.inMagicMenu == True:
                        currentLeftArrow = leftArrow
                        currentRightArrow = rightArrow
                if event.key == pygame.K_DOWN:
                    currentLeftArrow = selectedLeftArrow
                    currentRightArrow = rightArrow
                if event.key == pygame.K_UP:
                    currentRightArrow = selectedRightArrow
                    currentLeftArrow = leftArrow


        pygame.display.flip()
        screen.blit(background, (0,0))
        screen.blit(menu, (85,120))
        if arrow.inMagicMenu == True:
            screen.blit(currentRightArrow, (362, 178))
            screen.blit(currentLeftArrow, (521, 208))
        player_group.draw(screen)
        enemy_group.draw(screen)
        menu_assets.draw(screen)
        special_effects.draw(screen)
        player_group.update()
        enemy_group.update()
        menu_assets.update()
        special_effects.update()
        clock.tick(20)

def EncounterTwo():
    global menu, remainingCharges1, remainingCharges2, remainingCharges3,currentLeftArrow, currentRightArrow
    screen = pygame.display.set_mode((640,360))
    clock = pygame.time.Clock()
    playmusic.play(enemyBattle, -1)
    enemy_group.add(dragon_fish)
    background = pygame.image.load("assets\\backgrounds\\background_encounter2.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    arrow.inMagicMenu = False
                    arrow.rightness = 3
                    menu = arrow.defaultMenu
                if event.key == pygame.K_RETURN:
                    if arrow.inMagicMenu == True:
                        if currentRightArrow == selectedRightArrow:
                            if menu in arrow.magicMenu2:
                                menu = arrow.magicMenus[2][remainingCharges3]
                            if menu in arrow.magicMenu1:
                                menu = arrow.magicMenus[1][remainingCharges2]
                        if currentLeftArrow == selectedLeftArrow:
                            if menu in arrow.magicMenu2:
                                menu = arrow.magicMenus[0][remainingCharges1]
                            if menu in arrow.magicMenu3:
                                menu = arrow.magicMenus[1][remainingCharges2]
                        if currentLeftArrow == leftArrow and currentRightArrow == rightArrow:
                            if menu in arrow.magicMenu1:
                                if remainingCharges1 != 4:
                                    remainingCharges1 += 1
                                    menu = arrow.magicMenus[0][remainingCharges1]
                                    mejik.healing()
                                else:
                                    print("Out of magic!")
                            if menu in arrow.magicMenu2:
                                if remainingCharges2 != 4:
                                    remainingCharges2 += 1
                                    menu = arrow.magicMenus[1][remainingCharges2]
                                    mejik.damage()
                                else:
                                    print("Out of magic!")
                            if menu in arrow.magicMenu3:
                                if remainingCharges3 != 4:
                                    remainingCharges3 += 1
                                    menu = arrow.magicMenus[2][remainingCharges3]
                                    mejik.daze()
                                else:
                                    print("Out of magic!")


                    if arrow.inMagicMenu == False:
                        if arrow.rightness == 1:
                            if merek.defending == True:
                                merek.armor -= 5
                                print(' ')
                                print("Your guard dropped!")
                                merek.defending = False
                            if dragon_fish.health > 0:
                                if merek.health > 0:
                                    if merek.health > 0:
                                        merek.attack()
                                    if dragon_fish.health > 0:
                                        dragon_fish.attack()
                        if arrow.rightness == 2:
                            merek.defend()
                            print(' ')
                            print("Your guard is up!")
                            merek.health += 2
                            if dragon_fish.health > 0:
                                if merek.health > 0:
                                        dragon_fish.attack()
                        if arrow.rightness == 3:
                            menu = arrow.magicMenus[0][remainingCharges1]
                            arrow.inMagicMenu = True
                            arrow.rightness = 5

                if event.key == pygame.K_RIGHT:
                    arrow.move_right()
                if event.key == pygame.K_LEFT:
                    if arrow.inMagicMenu == False:
                        arrow.move_left()
                    if arrow.inMagicMenu == True:
                        currentLeftArrow = leftArrow
                        currentRightArrow = rightArrow
                if event.key == pygame.K_DOWN:
                    currentLeftArrow = selectedLeftArrow
                    currentRightArrow = rightArrow
                if event.key == pygame.K_UP:
                    currentRightArrow = selectedRightArrow
                    currentLeftArrow = leftArrow


        pygame.display.flip()
        screen.blit(background, (0,0))
        screen.blit(menu, (85,120))
        if arrow.inMagicMenu == True:
            screen.blit(currentRightArrow, (362, 178))
            screen.blit(currentLeftArrow, (521, 208))
        player_group.draw(screen)
        enemy_group.draw(screen)
        menu_assets.draw(screen)
        player_group.update()
        enemy_group.update()
        menu_assets.update()
        clock.tick(20)

def EncounterThree():
    global menu, remainingCharges1, remainingCharges2, remainingCharges3,currentLeftArrow, currentRightArrow
    screen = pygame.display.set_mode((640,360))
    clock = pygame.time.Clock()
    playmusic.play(vampireMusic, -1)
    enemy_group.add(vampiir)
    background = pygame.image.load("assets\\backgrounds\\background_encounter3.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    arrow.inMagicMenu = False
                    arrow.rightness = 3
                    menu = arrow.defaultMenu
                if event.key == pygame.K_RETURN:
                    if arrow.inMagicMenu == True:
                        if currentRightArrow == selectedRightArrow:
                            if menu in arrow.magicMenu2:
                                menu = arrow.magicMenus[2][remainingCharges3]
                            if menu in arrow.magicMenu1:
                                menu = arrow.magicMenus[1][remainingCharges2]
                        if currentLeftArrow == selectedLeftArrow:
                            if menu in arrow.magicMenu2:
                                menu = arrow.magicMenus[0][remainingCharges1]
                            if menu in arrow.magicMenu3:
                                menu = arrow.magicMenus[1][remainingCharges2]
                        if currentLeftArrow == leftArrow and currentRightArrow == rightArrow:
                            if menu in arrow.magicMenu1:
                                if remainingCharges1 != 4:
                                    remainingCharges1 += 1
                                    menu = arrow.magicMenus[0][remainingCharges1]
                                    mejik.healing()
                                else:
                                    print("Out of magic!")
                            if menu in arrow.magicMenu2:
                                if remainingCharges2 != 4:
                                    remainingCharges2 += 1
                                    menu = arrow.magicMenus[1][remainingCharges2]
                                    mejik.damage()
                                else:
                                    print("Out of magic!")
                            if menu in arrow.magicMenu3:
                                if remainingCharges3 != 4:
                                    remainingCharges3 += 1
                                    menu = arrow.magicMenus[2][remainingCharges3]
                                    mejik.daze()
                                else:
                                    print("Out of magic!")


                    if arrow.inMagicMenu == False:
                        if arrow.rightness == 1:
                            if merek.defending == True:
                                merek.armor -= 5
                                print(' ')
                                print("Your guard dropped!")
                                merek.defending = False
                            if vampiir.health > 0:
                                if merek.health > 0:
                                    if merek.health > 0:
                                        merek.attack()
                                    if vampiir.health > 0:
                                        vampiir.attack()
                        if arrow.rightness == 2:
                            merek.defend()
                            print(' ')
                            print("Your guard is up!")
                            merek.health += 2
                            if vampiir.health > 0:
                                if merek.health > 0:
                                        vampiir.attack()
                        if arrow.rightness == 3:
                            menu = arrow.magicMenus[0][remainingCharges1]
                            arrow.inMagicMenu = True
                            arrow.rightness = 5

                if event.key == pygame.K_RIGHT:
                    arrow.move_right()
                if event.key == pygame.K_LEFT:
                    if arrow.inMagicMenu == False:
                        arrow.move_left()
                    if arrow.inMagicMenu == True:
                        currentLeftArrow = leftArrow
                        currentRightArrow = rightArrow
                if event.key == pygame.K_DOWN:
                    currentLeftArrow = selectedLeftArrow
                    currentRightArrow = rightArrow
                if event.key == pygame.K_UP:
                    currentRightArrow = selectedRightArrow
                    currentLeftArrow = leftArrow


        pygame.display.flip()
        screen.blit(background, (0,0))
        screen.blit(menu, (85,120))
        if arrow.inMagicMenu == True:
            screen.blit(currentRightArrow, (362, 178))
            screen.blit(currentLeftArrow, (521, 208))
        player_group.draw(screen)
        enemy_group.draw(screen)
        menu_assets.draw(screen)
        player_group.update()
        enemy_group.update()
        menu_assets.update()
        clock.tick(20)

def EncounterFour():
    global menu, remainingCharges1, remainingCharges2, remainingCharges3,currentLeftArrow, currentRightArrow
    screen = pygame.display.set_mode((640,360))
    clock = pygame.time.Clock()
    playmusic.play(enemyBattle, -1)
    enemy_group.add(angler_fish)
    background = pygame.image.load("assets\\backgrounds\\background_encounter4.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    arrow.inMagicMenu = False
                    arrow.rightness = 3
                    menu = arrow.defaultMenu
                if event.key == pygame.K_RETURN:
                    if arrow.inMagicMenu == True:
                        if currentRightArrow == selectedRightArrow:
                            if menu in arrow.magicMenu2:
                                menu = arrow.magicMenus[2][remainingCharges3]
                            if menu in arrow.magicMenu1:
                                menu = arrow.magicMenus[1][remainingCharges2]
                        if currentLeftArrow == selectedLeftArrow:
                            if menu in arrow.magicMenu2:
                                menu = arrow.magicMenus[0][remainingCharges1]
                            if menu in arrow.magicMenu3:
                                menu = arrow.magicMenus[1][remainingCharges2]
                        if currentLeftArrow == leftArrow and currentRightArrow == rightArrow:
                            if menu in arrow.magicMenu1:
                                if remainingCharges1 != 4:
                                    remainingCharges1 += 1
                                    menu = arrow.magicMenus[0][remainingCharges1]
                                    mejik.healing()
                                else:
                                    print("Out of magic!")
                            if menu in arrow.magicMenu2:
                                if remainingCharges2 != 4:
                                    remainingCharges2 += 1
                                    menu = arrow.magicMenus[1][remainingCharges2]
                                    mejik.damage()
                                else:
                                    print("Out of magic!")
                            if menu in arrow.magicMenu3:
                                if remainingCharges3 != 4:
                                    remainingCharges3 += 1
                                    menu = arrow.magicMenus[2][remainingCharges3]
                                    mejik.daze()
                                else:
                                    print("Out of magic!")

                    if arrow.inMagicMenu == False:
                        if arrow.rightness == 1:
                            if merek.defending == True:
                                merek.armor -= 5
                                print(' ')
                                print("Your guard dropped!")
                                merek.defending = False
                            if angler_fish.health > 0:
                                if merek.health > 0:
                                    if merek.health > 0:
                                        merek.attack()
                                    if angler_fish.health > 0:
                                        angler_fish.attack()
                        if arrow.rightness == 2:
                            merek.defend()
                            print(' ')
                            print("Your guard is up!")
                            merek.health += 2
                            if angler_fish.health > 0:
                                if merek.health > 0:
                                        angler_fish.attack()
                        if arrow.rightness == 3:
                            menu = arrow.magicMenus[0][remainingCharges1]
                            arrow.inMagicMenu = True
                            arrow.rightness = 5

                if event.key == pygame.K_RIGHT:
                    arrow.move_right()
                if event.key == pygame.K_LEFT:
                    if arrow.inMagicMenu == False:
                        arrow.move_left()
                    if arrow.inMagicMenu == True:
                        currentLeftArrow = leftArrow
                        currentRightArrow = rightArrow
                if event.key == pygame.K_DOWN:
                    currentLeftArrow = selectedLeftArrow
                    currentRightArrow = rightArrow
                if event.key == pygame.K_UP:
                    currentRightArrow = selectedRightArrow
                    currentLeftArrow = leftArrow


        pygame.display.flip()
        screen.blit(background, (0,0))
        screen.blit(menu, (85,120))
        if arrow.inMagicMenu == True:
            screen.blit(currentRightArrow, (362, 178))
            screen.blit(currentLeftArrow, (521, 208))
        player_group.draw(screen)
        enemy_group.draw(screen)
        menu_assets.draw(screen)
        player_group.update()
        enemy_group.update()
        menu_assets.update()
        clock.tick(20)

def EncounterFive():
    global menu, remainingCharges1, remainingCharges2, remainingCharges3,currentLeftArrow, currentRightArrow
    screen = pygame.display.set_mode((640,360))
    clock = pygame.time.Clock()
    playmusic.play(finalBossMusic, -1)
    enemy_group.add(final)
    background = pygame.image.load("assets\\backgrounds\\background_encounter5.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    arrow.inMagicMenu = False
                    arrow.rightness = 3
                    menu = arrow.defaultMenu
                if event.key == pygame.K_RETURN:
                    if arrow.inMagicMenu == True:
                        if currentRightArrow == selectedRightArrow:
                            if menu in arrow.magicMenu2:
                                menu = arrow.magicMenus[2][remainingCharges3]
                            if menu in arrow.magicMenu1:
                                menu = arrow.magicMenus[1][remainingCharges2]
                        if currentLeftArrow == selectedLeftArrow:
                            if menu in arrow.magicMenu2:
                                menu = arrow.magicMenus[0][remainingCharges1]
                            if menu in arrow.magicMenu3:
                                menu = arrow.magicMenus[1][remainingCharges2]
                        if currentLeftArrow == leftArrow and currentRightArrow == rightArrow:
                            if menu in arrow.magicMenu1:
                                if remainingCharges1 != 4:
                                    remainingCharges1 += 1
                                    menu = arrow.magicMenus[0][remainingCharges1]
                                    mejik.healing()
                                else:
                                    print("Out of magic!")
                            if menu in arrow.magicMenu2:
                                if remainingCharges2 != 4:
                                    remainingCharges2 += 1
                                    menu = arrow.magicMenus[1][remainingCharges2]
                                    mejik.damage()
                                else:
                                    print("Out of magic!")
                            if menu in arrow.magicMenu3:
                                if remainingCharges3 != 4:
                                    remainingCharges3 += 1
                                    menu = arrow.magicMenus[2][remainingCharges3]
                                    mejik.daze()
                                else:
                                    print("Out of magic!")


                    if arrow.inMagicMenu == False:
                        if arrow.rightness == 1:
                            if merek.defending == True:
                                merek.armor -= 5
                                print(' ')
                                print("Your guard dropped!")
                                merek.defending = False
                            if final.health > 0:
                                if merek.health > 0:
                                    if merek.health > 0:
                                        merek.attack()
                                    if final.health > 0:
                                        final.attack()
                        if arrow.rightness == 2:
                            merek.defend()
                            print(' ')
                            print("Your guard is up!")
                            merek.health += 2
                            if final.health > 0:
                                if merek.health > 0:
                                        final.attack()
                        if arrow.rightness == 3:
                            menu = arrow.magicMenus[0][remainingCharges1]
                            arrow.inMagicMenu = True
                            arrow.rightness = 5

                if event.key == pygame.K_RIGHT:
                    arrow.move_right()
                if event.key == pygame.K_LEFT:
                    if arrow.inMagicMenu == False:
                        arrow.move_left()
                    if arrow.inMagicMenu == True:
                        currentLeftArrow = leftArrow
                        currentRightArrow = rightArrow
                if event.key == pygame.K_DOWN:
                    currentLeftArrow = selectedLeftArrow
                    currentRightArrow = rightArrow
                if event.key == pygame.K_UP:
                    currentRightArrow = selectedRightArrow
                    currentLeftArrow = leftArrow


        pygame.display.flip()
        screen.blit(background, (0,0))
        screen.blit(menu, (85,120))
        if arrow.inMagicMenu == True:
            screen.blit(currentRightArrow, (362, 178))
            screen.blit(currentLeftArrow, (521, 208))
        player_group.draw(screen)
        enemy_group.draw(screen)
        menu_assets.draw(screen)
        player_group.update()
        enemy_group.update()
        menu_assets.update()
        clock.tick(20)

SceneOne()