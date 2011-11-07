import pygame #@UnresolvedImport
import os, sys
import random
red = (255, 0,0)
black = (0,0,20)

#
#class mainMenuButton(pygame.sprite.Sprite):
#    """interface button class"""
#    change_x=0
#    change_y=0
#    def __init__(self, x, y):
#        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.Surface([200,75])
#        self.image.fill(red);
#        self.rect = self.image.get_rect()
#        self.rect.top = y
#        self.rect.left = x
#    def update(self,player):
#        old_x=self.rect.left
#        new_x=old_x+self.change_x
#        self.rect.left = new_x
#    
#    def didGetPressed(self, coord):
#        ######
#        print "did get pressed you bitch"

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
        
    


    

pygame.init()
#create an instance of mainPerson
#create an initial instance of obstacle
obstacle = mainMusicObstacle(300, 300);
screen = pygame.display.set_mode([1080, 700])
#refresh the screen
renderSprites = pygame.sprite.RenderPlain()
renderSprites.add(obstacle)
global time;
time = 0;
end = False

while end == False:

    renderSprites.draw(screen)   

    pygame.display.flip()
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end=True
        if event.type == pygame.KEYDOWN:
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
                    


                    

            

                    


#                if time 0 pass in obstacle if time 1+ then input obstacle1
                
            

    obstacle.update(renderSprites)


pygame.quit()