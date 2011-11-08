import pygame #@UnresolvedImport
from pygame.locals import *
import os, sys
import random
import array

red = (255, 0,0)
black = (0,0,20)

class mainMusicObstacle(pygame.sprite.Sprite):
    """class that controls the main race obstacles"""
    change_x=0
    change_y=0
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,50])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
    def update(self,player):
        old_x=self.rect.left
        new_x=old_x+self.change_x
        self.rect.left = new_x
        
class mainMapBricks(pygame.sprite.Sprite):
    change_x=0
    change_y=0
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([100,100])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
    def update(self,player):
        old_x=self.rect.left
        new_x=old_x+self.change_x
        self.rect.left = new_x


def basicLayoutArray(mapArraysX, mapArraysY):
    x = 0;
    for i in  mapArraysX:
        posX = mapArraysX[x]
        posY = mapArraysY[x];
        brick = mainMapBricks(posX, posY);
        print "i made instance ", x
#        print brick.rect.x, brick.rect.y;
        renderSprites.add(brick);
        brick.update(renderSprites)
        x= x+1;
        


def addBlockPerBeatX(positionObstacle):
    print "i got her"
#    if time == 0:
    posX = positionObstacle.rect.x +50;
    print posX
    return posX
def addBlockPerBeatY(positionObstacle):
    
    posY = positionObstacle.rect.y +50;
    print posY
    return posY


class spaceShip(pygame.sprite.Sprite):
    change_x = 0;
    change_y= 0;
    """contains a method sets up the x and y, as well as the array movement so that velocity plays a role"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.top = y;
        self.rect.left = x;
        self.speed = 20
        self.state = "still"
        self.reinit()
    def reinit(self):
        self.state =  "still"
        self.movepos= [0,0];
        self.x = 520;
        self.y = 600;
    def move(self, dx, dy):
        if self.rect.left + dx< 0:
            self.rect.left = 0
        elif self.rect.right + dx> screen.get_width():
            self.rect.right = screen.get_width()
        else:
            self.rect.x += dx
        if self.rect.top + dy< 0:
            self.rect.top = 0
        elif self.rect.bottom + dy > screen.get_height():
            self.rect.bottom = screen.get_height()
        else:
            self.rect.y += dy

    def update(self,player):
        old_x=self.rect.left
        new_x=old_x+self.change_x
        self.rect.left = new_x

pygame.init()
#create an instance of mainPerson
#create an initial instance of obstacle
obstacle = mainMusicObstacle(300, 300);
global screen;
screen = pygame.display.set_mode([1080, 700]);
#ship = spaceShip(510, 615, screen);
ship = spaceShip(540, 600);
#refresh the screen
renderSprites = pygame.sprite.RenderPlain()
renderSprites.add(obstacle)
renderSprites.add(ship)
global time;
time = 0;
end = False
mapArraysX = [0, 0, 0, 100, 100, 200]
mapsArraysY = [0, 100,200, 100, 200, 300]
basicLayoutArray(mapArraysX, mapsArraysY)


while end == False:
    moveX = 0
    moveY = 0
    renderSprites.draw(screen)   
    pygame.display.flip()
    screen.fill(black)
    
    keyDown = pygame.key.get_pressed()
    if keyDown[K_LEFT]:
        moveX -= 3
        ship.move(moveX, moveY)
        screen.blit(ship.image, ship)
        ship.update(renderSprites)
    if keyDown[K_RIGHT]:
        moveX += 3
        ship.move(moveX, moveY)
        screen.blit(ship.image, ship)
        ship.update(renderSprites)
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end=True
        
            if event.key == pygame.K_RIGHT:
                ship.moveRight()
                ship.updatePos();
                ship.update(renderSprites);
                
            if event.key == pygame.K_a:
                if time == 0:
                    x = addBlockPerBeatX(obstacle);
                    obstacle1 = mainMusicObstacle(x, obstacle.rect.y)
                    renderSprites.add(obstacle1);
                    time = time+1;
                if time >0:
                    print "yea"
                    x = addBlockPerBeatX(obstacle1);
                    obstacle1 = mainMusicObstacle(x, obstacle.rect.y)
                    renderSprites.add(obstacle1);
                    obstacle1.update(renderSprites)
            if event.key == pygame.K_s:
                if time == 0:
                        y = addBlockPerBeatY(obstacle);
                        obstacle1 = mainMusicObstacle(obstacle.rect.x ,y)
                        renderSprites.add(obstacle1);
                        obstacle1.update(renderSprites)
                if time >0:
                        y = addBlockPerBeatY(obstacle1);
                        obstacle1 = mainMusicObstacle(obstacle.rect.x ,y)
                        renderSprites.add(obstacle1);
                        obstacle1.update(renderSprites)
                    

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ship.movepos = [0,0]
                ship.state = "still"
                    

            

                    


#                if time 0 pass in obstacle if time 1+ then input obstacle1
                
            

    obstacle.update(renderSprites)


pygame.quit()