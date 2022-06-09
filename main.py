from re import X
import time
from tkinter import font
from tracemalloc import start
from xml.etree.ElementTree import ProcessingInstruction
from pip import main
import pygame
from pygame import mixer
import sys
import os
import random
import math
import tkinter as tk
from pyparsing import White
pygame.init()
pygame.mixer.init()
CAR_WIDTH, CAR_HEIGHT = 55, 40
REGCAR_WIDTH, REGCAR_HEIGHT = 35, 20
ROCK_WIDTH, ROCK_HEIGHT = 30,30
COIN_WIDTH, COIN_HEIGHT =30,30
VEL = 5

explosion= pygame.mixer.music.load(os.path.join('assets', 'hit-someting-6037.mp3'))
fire_sound= pygame.mixer.music.load(os.path.join('assets', 'gun-gunshot-01.wav'))
global points, newpoints, baba
points = 0

smallfont = pygame.font.SysFont("comicsansms", 25)
mediumfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
randCoinX=random.randrange(890,900)
randCoinY=random.randrange(100,400)
font_name= pygame.font.match_font("arial")

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)

def score(baba):
    text = smallfont.render("Coins: " + str(baba), True, (255,255,255))
    WIN.blit(text, [0,0])

USER_CAR_IMAGE = pygame.image.load(os.path.join('assets', 'Audi.png'))
USER_CAR = pygame.transform.rotate(pygame.transform.scale(
    USER_CAR_IMAGE, (CAR_WIDTH, CAR_HEIGHT)), 0)

TANK_IMAGE = pygame.image.load(os.path.join('assets', 'tank4.png'))
TANK = pygame.transform.rotate(pygame.transform.scale(
    TANK_IMAGE, (CAR_WIDTH, CAR_HEIGHT)), 270)

POLICE_CAR_IMAGE = pygame.image.load(os.path.join('assets', 'Police.png'))
POLICE_CAR = pygame.transform.rotate(pygame.transform.scale(
POLICE_CAR_IMAGE, (CAR_WIDTH, CAR_HEIGHT)), 0)

ROCK_IMAGE = pygame.image.load(os.path.join('assets', 'rock.png'))
ROCK = pygame.transform.rotate(pygame.transform.scale(
ROCK_IMAGE, (30, 30)), 0)

COIN_IMAGE = pygame.image.load(os.path.join('assets', 'coin.png'))
COIN = pygame.transform.rotate(pygame.transform.scale(
COIN_IMAGE, (COIN_WIDTH, COIN_HEIGHT)), 0)

OTHER_CAR_IMAGE = pygame.image.load(os.path.join('assets', 'othercar.png'))
OTHER_CAR = pygame.transform.rotate(pygame.transform.scale(
OTHER_CAR_IMAGE, (CAR_WIDTH, CAR_HEIGHT)), 0)

COIN_IMAGE = pygame.image.load(os.path.join('assets', 'coin.png'))

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

BULLET_VEL = 7
OBJECT_VEL = 2.1

GENERATION_TIME = 800

ROAD = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'road2.png')), (WIDTH, HEIGHT))
_amount=0
class Coin:
    def __init__(self, x=500, y=200):
        
        self._x = x
        self._y= y
    def add_coin():
        global _amount
        _amount = _amount + 20
    def reduce_coin_forshield():
        global _amount
        _amount = _amount -100
    def reduce_coin_forbullet():
        global _amount
        _amount = _amount -50
    def check_collision(self,X,Y):
        car_rect=pygame.Rect(X,Y,CAR_WIDTH,CAR_HEIGHT)#arabanin ve objectlerin koordinatlarini ve dimensionlari ile iki rect objesi olusturuyor carpismayi kontrol etmek icin
        coin_rect=pygame.Rect(self._x,self._y,COIN_WIDTH,COIN_HEIGHT),
        if  pygame.Rect.colliderect(car_rect,coin_rect) == True: 
            self.active=False #self.b attribute'u false yapiyor, false olan objeler blit edilmiyor ekrana
            return True  #collide ederlerse true return ediyor
class Car:
    def __init__(self,x=100,y=200):
        self._x = x
        self._y = y
        self._width,self._height = CAR_WIDTH,CAR_HEIGHT   
    def draw():
        pass
    def speed_up():
        pass
class PoliceCar(Car):
    
    def check_collision(self,X,Y):
        car_rect=pygame.Rect(X,Y,CAR_WIDTH,CAR_HEIGHT)#arabanin ve objectlerin koordinatlarini ve dimensionlari ile iki rect objesi olusturuyor carpismayi kontrol etmek icin
        policecar_rect=pygame.Rect(self._x,self._y,CAR_WIDTH,CAR_HEIGHT),
        if  pygame.Rect.colliderect(car_rect,policecar_rect): #Oyunu bitiren kod
            self.finish()
            pygame.quit
    
    def finish(self):
        finished = True
        while finished:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit(quit())
            WIN.fill((0,0,0))
            draw_text(WIN, str("You Caught! Please press ESCAPE."), 18, WIDTH/2, 10)
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(5)   
class RoadObject:
    def __init__(self,y,x=800):
        self._x = x
        self._y = y
        self._width = 20
        self._height = 20
        self.active=True
        
    def check_collision(self,X,Y):
        car_rect=pygame.Rect(X,Y,CAR_WIDTH,CAR_HEIGHT)#arabanin ve objectlerin koordinatlarini ve dimensionlari ile iki rect objesi olusturuyor carpismayi kontrol etmek icin
        object_rect=pygame.Rect(self._x,self._y,ROCK_WIDTH,ROCK_HEIGHT),
        if  pygame.Rect.colliderect(car_rect,object_rect) == True: 
            #pygame.mixer.Sound.play(explosion)
            self.active=False #self.b attribute'u false yapiyor, false olan objeler blit edilmiyor ekrana
            return True  #collide ederlerse true return ediyor
    
    def deactivate(self):
        self.active = False
    
    def move(self):
        self._x -= OBJECT_VEL
        
class UserCar(Car):
    def __init__(self):
        super().__init__()
        self.shield = False
        self.shieldtime = 0
        self.bullet=[] 
        super().__init__()
    
    def fire_regular_bullet(self):
        if _amount>=50:
            self.bullet.append(Bullet(self._x+self._width,self._y+self._height//2))
            Coin.reduce_coin_forbullet()
        
    def bulletcollision(self,object: RoadObject):
        for bullet in self.bullet:
            if bullet.active:
                if bullet._x >= 900:
                    self.bullet.remove(bullet)
                a = bullet.checkcollision(object._x,object._y)
                if a:
                    self.bullet.remove(bullet)
                return a 
    def use_shield():
        pass
    def activate_shield(self):
        if _amount>=100:
            self.shield = True
            Coin.reduce_coin_forshield()
            self.shieldtime = time.time()
    def deactivate_shield(self):
        currenttime = time.time()
        if currenttime - self.shieldtime>=5:
            self.shield = False   
    
    def are_you_there_roadobject(self, roadobject: RoadObject):
        if self.shield == False:
            f = roadobject.check_collision(self._x,self._y) #kendi koordinatlarini roadobject'e yolluyor
            if f: 
                self.bounce_back() #true return ederse bounceback calisiyor araba geri 
                                #sekiyor bu fonksiyon henuz tam calismiyor
    def are_you_there_regularcar(self, roadobject: RoadObject):
        if self.shield == False:
            f = roadobject.check_collision(self._x,self._y) #kendi koordinatlarini roadobject'e yolluyor
            if f: 
                self.bounce_back()
    def are_you_there_coin(self, coin: Coin):
        coin.check_collision(self._x, self._y)
        if coin.check_collision(self._x,self._y):
            Coin.add_coin()
    def are_you_there_policecar(self, policecar: PoliceCar):
        policecar.check_collision(self._x,self._y) #kendi koordinatlarini roadobject'e yolluyor
        if policecar.check_collision(self._x,self._y): 
            self.bounce_back() #true return ederse bounceback calisiyor araba geri 
                                #sekiyor bu fonksiyon henuz tam calismiyor
        
    def bounce_back(self):
        self._x-=50
    
    def move(self,keys_pressed):
        if keys_pressed[pygame.K_w] and self._y - VEL > 0:  # UP
            self._y -= VEL
        if keys_pressed[pygame.K_s] and self._y + VEL + self._height < HEIGHT - 15:  # DOWN
            self._y += VEL
                
    def pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit(
                            
                            quit()
                        )
            WIN.fill((0,0,0))
            draw_text(WIN, str("Press C to continue or Q to quit."), 18, WIDTH/2, 10)
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(5)
    def fire_strong_bullet():
    
        pass
    def check_if_boundaries_exceeded():
        pass

class Obstacle(RoadObject):
   
    def is_shield_active():
        pass
class Bullet:
    def __init__(self,x,y): 
        self._width= 20
        self._height= 5
        self._x=x
        self._y=y
        self.active = True

    def checkcollision(self,X,Y):
        bullet_rect=pygame.Rect(self._x,self._y,self._width,self._height)
        object_rect=pygame.Rect(X,Y,ROCK_WIDTH,ROCK_HEIGHT)
        a = pygame.Rect.colliderect(bullet_rect,object_rect) 
        if a: 
            self.active=False
            return True
        
    def move(self):
        self._x += BULLET_VEL
class RoadGame:
    
    def __init__(self):
        self._u = UserCar() 
        self._object=[]
        self._policecar=[]
        self._coin=[]
        self._regularcar=[]
        
        for i in range(25):
            self._policecar.append(PoliceCar(10,20*i))
    
    def add_regular_car(self):
        self._regularcar.append(RoadObject(random.randint(50,450)))
    def add_road_object(self):
        self._object.append(RoadObject(random.randint(50,450)))
    def add_coin(self):
        self._coin.append(RoadObject(random.randint(50,450)))
    
    def draw_window(self):
        WIN.blit(ROAD,(0,0))
        draw_text(WIN, str("Ready to Roll?"), 18, WIDTH/2, 10)
        for object in self._object:
            if object.active:
                WIN.blit(ROCK,(object._x,object._y))
        if self._u.shield:
            WIN.blit(TANK, (self._u._x, self._u._y))
        else:
            WIN.blit(USER_CAR, (self._u._x, self._u._y))
        
        for police in self._policecar:
            WIN.blit(POLICE_CAR, (police._x, police._y))
        
        for bullet in self._u.bullet:
            if bullet.active:
                pygame.draw.rect(WIN,(255, 0, 0), (bullet._x, bullet._y-20 + self._u._height//2 - 2, bullet._width, bullet._height))
        
        for regularcar in self._regularcar:
            if regularcar.active:
                WIN.blit(OTHER_CAR,(regularcar._x, regularcar._y))
        
        for coin in self._coin:
            if coin.active:
                WIN.blit(COIN,(coin._x,coin._y))
        
        score(_amount)
        pygame.display.update()
    
    def checkcollision(self): 
        for object in self._object:
            if object.active:
                self._u.are_you_there_roadobject(object)
                a = self._u.bulletcollision(object)#sends object to usercar
                if a: 
                    object.deactivate()
                    self._object.remove(object)  
        for police in self._policecar:
            self._u.are_you_there_policecar(police)
        for regcar in self._regularcar:
            self._u.are_you_there_regularcar(regcar)
        for coins in self._coin:
            if coins.active:
                self._u.are_you_there_coin(coins)
    def delete_objects(self):
        for object in self._object:
            if object._x <= 50:
                self._object.remove(object) 
        for coins in self._coin:
            if coins._x <= 50:
                self._coin.remove(coins)        
                 
    def TimeTick(self): #timetick usecases
    #GENERATING RANDOM OBJECTS    
        global GENERATION_TIME
        r= random.randint(0,GENERATION_TIME)
        if r<=18 and r > 12:
            self.add_regular_car()
        elif r <= 12 and r>7:
            global OBJECT_VEL
            if OBJECT_VEL <15:
                OBJECT_VEL = OBJECT_VEL + .5
            else:
                OBJECT_VEL = OBJECT_VEL - 1
            self.add_road_object()
        elif r<=7:
            self.add_coin()   
        if GENERATION_TIME >= 550:
                GENERATION_TIME -=5
        self.checkcollision()
        self.delete_objects()
        self._u.deactivate_shield()
        
    def main(self):
        pygame.display.set_caption("BUsted!")
        clock = pygame.time.Clock()
         
        run = True
        while run:
            
            clock.tick(FPS)
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:
                        self._u.fire_regular_bullet()
                    if event.key == pygame.K_k:
                        self._u.fire_strong_bullet()
                    if event.key == pygame.K_l:
                        self._u.activate_shield()
                    if event.key == pygame.K_p:
                        self._u.pause()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        
            keys_pressed = pygame.key.get_pressed()
            self._u.move(keys_pressed)
            for bullets in self._u.bullet:
                bullets.move()
            for objects in self._object:
                objects.move()
            for coins in self._coin:
                coins.move()
            for regularcars in self._regularcar:
                regularcars.move()
            
            self.TimeTick()
            a.draw_window()    
    def calculate_score():
        pass
    def create_obstacle():
        pass
    def create_car():
        pass
    def create_coin():
        pass 
    def check_usercar_coin():

        pass
    def create_othercars():
        pass
    def check_if_you_caught():
        pass
    def speed_up():
        pass
a=RoadGame()
a.main()