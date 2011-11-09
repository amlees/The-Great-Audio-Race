##Main Menu

import os, pygame
import Main
from pygame.locals import *
def Start():
    pygame.init()
    screen = pygame.display.set_mode([1000, 700])
    pygame.display.set_caption("The Great Audio Race")
    
    state = 0
    checkClick = 0

    titlexPos = screen.get_rect().centerx - 286
    
    buttonGroup = pygame.sprite.Group()
    
    
    
    def renderUI():
        global playButton
        global settingsButton
        global scoresButton
        global exitButton
        global title
        global logo
        playButton = Button((0,0,0), "button-play.png", (400, 150))
        settingsButton = Button((0,0,0), "button-settings.png", (200, 325))
        scoresButton = Button((0,0,0), "button-high scores.png", (600, 325))
        exitButton = Button((0,0,0), "button-exit.png", (400, 500))
        title = Title((0,0,0), "title.png", (titlexPos, 25))
        logo= Logo((0,0,0), "that1group-logo.jpg", (800, 600))
    
        
        
    class Background(pygame.sprite.Sprite):
        def __init__(self, color, filename, location):
            pygame.sprite.Sprite.__init__(self)
            
            self.image = pygame.image.load(filename).convert()
            self.image.set_colorkey(color)
            self.image = pygame.transform.scale(self.image, (1000,700))
            
            self.rect = self.image.get_rect()
            self.rect.x = location[0]
            self.rect.y = location[1]
            
            screen.blit(self.image, self)
                    
    class Button(pygame.sprite.Sprite):
        def __init__(self, color, filename, location):
            pygame.sprite.Sprite.__init__(self)
            
            self.image = pygame.image.load(filename).convert()
            self.image.set_colorkey(color)
            self.image = pygame.transform.scale(self.image, (200,75))
            
            self.rect = self.image.get_rect()
            self.rect.x = location[0]
            self.rect.y = location[1]
            
            screen.blit(self.image, self)
            
        def playPressed(self):
            global checkClick
            mousePos = pygame.mouse.get_pos()
            mousePress = pygame.mouse.get_pressed()
            if mousePress[0] == 1:
                if mousePos[0] >= 400 and mousePos[0] <= 600:
                    if mousePos[1] >= 150 and mousePos[1] <= 225:
                        Main.Game()
    
    
        def settingsPressed(settingsButton):
            mousePos = pygame.mouse.get_pos()
            mousePress = pygame.mouse.get_pressed()
            if mousePress[0] == 1:
                if mousePos[0] >= 200 and mousePos[0] <= 400:
                    if mousePos[1] >= 325 and mousePos[1] <= 400: 
                        print "You're clicking a Settings"
                        
        def scoresPressed(scoresButton):
            mousePos = pygame.mouse.get_pos()
            mousePress = pygame.mouse.get_pressed()
            if mousePress[0] == 1:
                if mousePos[0] >= 600 and mousePos[0] <= 800:
                    if mousePos[1] >= 325 and mousePos[1] <= 400: 
                        print "You're clicking a Scores"
        
        def exitPressed(self, exitButton):
            global state
            mousePos = pygame.mouse.get_pos()
            mousePress = pygame.mouse.get_pressed()
            if mousePress[0] == 1:
                if mousePos[0] >= 400 and mousePos[0] <= 600:
                    if mousePos[1] >= 500 and mousePos[1] <= 575: 
                        print "You're clicking exit"
                        state = 1
                        return state
                        
                        
    class Title(pygame.sprite.Sprite):
        def __init__(self, color, filename, location):
            pygame.sprite.Sprite.__init__(self)
            
            self.image = pygame.image.load(filename).convert()
            self.image.set_colorkey(color)
            self.image = pygame.transform.scale(self.image, (572,104))
            
            self.rect = self.image.get_rect()
            self.rect.x = location[0]
            self.rect.y = location[1]
            
            screen.blit(self.image, self)
            
    class Logo(pygame.sprite.Sprite):
        def __init__(self, color, filename, location):
            pygame.sprite.Sprite.__init__(self)
            
            self.image = pygame.image.load(filename).convert()
            self.image.set_colorkey(color)
            self.image = pygame.transform.scale(self.image, (160,120))
            
            self.rect = self.image.get_rect()
            self.rect.x = location[0]
            self.rect.y = location[1]
            
            screen.blit(self.image, self)
            
    
    
    
    while state == 0:
        
        
        if checkClick == 0:    
            renderUI()
       
        #Add boolean to activate or deactivate
        Button.playPressed(playButton)
        Button.settingsPressed(settingsButton)
        Button.scoresPressed(scoresButton)
        Button.exitPressed(exitButton, state)                  
        
        screen.blit(playButton.image, playButton)
        screen.blit(settingsButton.image, settingsButton)
        screen.blit(scoresButton.image, scoresButton)
        
        pygame.display.update()
        
        checkClick = 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = 1
                end =True