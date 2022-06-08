import time
import pygame
import sys
import os
import random
import math

CAR_WIDTH, CAR_HEIGHT = 55, 40
ROCK_WIDTH, ROCK_HEIGHT = 30,30

VEL = 5

USER_CAR_IMAGE = pygame.image.load(os.path.join('assets', 'Audi.png'))
USER_CAR = pygame.transform.rotate(pygame.transform.scale(
    USER_CAR_IMAGE, (CAR_WIDTH, CAR_HEIGHT)), 0)

POLICE_CAR_IMAGE = pygame.image.load(os.path.join('assets', 'Police.png'))
POLICE_CAR = pygame.transform.rotate(pygame.transform.scale(
POLICE_CAR_IMAGE, (CAR_WIDTH, CAR_HEIGHT)), 0)

ROCK_IMAGE = pygame.image.load(os.path.join('assets', 'rock.png'))
ROCK = pygame.transform.rotate(pygame.transform.scale(
ROCK_IMAGE, (30, 30)), 0)

COIN_IMAGE = pygame.image.load(os.path.join('assets', 'coin.png'))
COIN = pygame.transform.rotate(pygame.transform.scale(
COIN_IMAGE, (ROCK_WIDTH, ROCK_HEIGHT)), 0)

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

BULLET_VEL = 7
OBJECT_VEL = 2


GENERATION_TIME = 800

ROAD = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'road.png')), (WIDTH, HEIGHT))



class Coin:
    def __init__(self):
        self._amount = 0
    def add_coin(self):
        self._amount+=20


class Car:
    def __init__(self):
        self._x = 500
        self._y = 200
        self._width,self._height = CAR_WIDTH,CAR_HEIGHT
        
    def draw():
        pass
    def speed_up():
        pass
class PoliceCar(Car):
    def check_if_you_are_caught():
        pass

class RoadObject:
    def __init__(self,y,x=800):
        self._x = x
        self._y = y
        self._width = 20
        self._height = 20
        self.b=True
        
    
    def check_collision(self,X,Y):
        car_rect=pygame.Rect(X,Y,CAR_WIDTH,CAR_HEIGHT)
        object_rect=pygame.Rect(self._x,self._y,ROCK_WIDTH,ROCK_HEIGHT),
        if  pygame.Rect.colliderect(car_rect,object_rect) == True:
            self.b=False
            return True
        
    
    def move(self):
        self._x -= OBJECT_VEL
        pass
class UserCar(Car):
    def __init__(self):
        super().__init__()
        
    
        self.bullet=[] 
        super().__init__()
    def fire_regular_bullet(self):
        self.bullet.append(Bullet(self._x+self._width,self._y+self._height//2))
        

        pass
    def use_shield():
        pass
    def activate_shield():
        pass
    def are_you_there(self, roadobject: RoadObject):
        roadobject.check_collision(self._x,self._y)
        if roadobject.check_collision(self._x,self._y):
            self.bounce_back()
        
    def bounce_back(self):
        self._x-=100
        
    def move(self,keys_pressed):
        if keys_pressed[pygame.K_w] and self._y - VEL > 0:  # UP
            self._y -= VEL
        if keys_pressed[pygame.K_s] and self._y + VEL + self._height < HEIGHT - 15:  # DOWN
            self._y += VEL
                
    
    def fire_strong_bullet():
    
        pass
    def check_if_boundaries_exceeded():
        pass


class Obstacle(RoadObject):
   
    def is_shield_active():
        pass
class Bullet:
    def __init__(self,x,y): 
        self._width= 10
        self._height= 5
        self._x=x
        self._y=y

    def are_you_there(self):
        Obstacle.check_collision(self._x,self._y)
    pass
    def move(self):
        self._x += BULLET_VEL
class RoadGame:
    def __init__(self):
        self._u = UserCar() 
        self._object=[]
        
    def add_road_object(self):
        self._object.append(RoadObject(random.randint(50,450)))
    def draw_window(self):
        WIN.blit(ROAD,(0,0))
        WIN.blit(USER_CAR, (self._u._x, self._u._y))
        for bullet in self._u.bullet:
            pygame.draw.rect(WIN,(255, 0, 0), (bullet._x, bullet._y-20 + self._u._height//2 - 2, bullet._width, bullet._height))
        for object in self._object:
            if object.b:
                WIN.blit(ROCK,(object._x,object._y))
            
        pygame.display.update()
        pass
    def TimeTick(self):
    #GENERATING RANDOM OBJECTS    
        global GENERATION_TIME
        
        r= random.randint(0,GENERATION_TIME)
        if r <= 30:
            self.add_road_object()
            
        if GENERATION_TIME >= 550:
                GENERATION_TIME -=5
        for object in self._object:
            self._u.are_you_there(object)
        
     #OBJECT-USERCAR COLLISION
           
        
             
        
     

    def main(self):
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
                
            keys_pressed = pygame.key.get_pressed()
            self._u.move(keys_pressed)
            for bullets in self._u.bullet:
                bullets.move()
            for objects in self._object:
                objects.move()
            
            
            
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