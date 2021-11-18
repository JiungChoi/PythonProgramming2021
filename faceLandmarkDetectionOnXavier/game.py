import facetracker_custom as fc
import pygame

import os, sys


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PRESENT_FRAME_WRITE_PATH = "Jiung/jiung.jpg"
GAMESTART_BUTTON_IMG = "button.png"
BUTTON_START_HEIGHT = 100
BUTTON_START_WIDTH = 400

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


class Button():
    def __init__(self,BUTTON_IMG_PATH):
        self.button = pygame.image.load(BUTTON_IMG_PATH)
        self.button = pygame.transform.scale(self.button,(BUTTON_START_WIDTH, BUTTON_START_HEIGHT))
        self.rect = self.button.get_rect()
        self.rect.x = SCREEN_WIDTH/2 - BUTTON_START_WIDTH/2
        self.rect.y = SCREEN_HEIGHT/2 - BUTTON_START_HEIGHT/2
        
    def pressed(self, mouse):
        if self.rect.collidepoint(mouse) == True:
            return True

class floatElement: # 부유물 클래스: 점수 클래스(plus)와, 실점(minus) 클래스로 상속한다. 
    def __init__(self, x, y):
        self.x = x # x좌표
        self.y = y # y좌표

class plusElement(floatElement): # 점수 클래스(plus) : 부유물 객체로 부터 상속 받는다. 
    def __init__(self, imgPath, x, y):
        super().__init__(x, y)
        self.img = imgPath # img의 경로

class minusElement(floatElement): # 실점 클래스(plus) : 부유물 객체로 부터 상속 받는다.
    def __init__(self, imgPath, x, y):
        super().__init__(x, y)
        self.img = imgPath # img의 경로


class Game:
    def __init__(self):
        #self.userName = input("Insert user info : ")
        self.WIDTH = 800
        self.HEIGHT = 800
        

    def windowSet(self, width, height):
        SCREEN_WIDTH = width
        SCREEN_HEIGHT = height

    def userSet(self, name):
        self.userName = name

    def introFactor(self): # path, coordinate, size
        self.gameIntroScreen = ["gameIntro.png", [0, 0] , (SCREEN_WIDTH,SCREEN_HEIGHT)]
        self.gameIntroChefs = ["chef.png", [SCREEN_WIDTH/2 - 0.5*SCREEN_WIDTH/1.6,SCREEN_HEIGHT- SCREEN_HEIGHT/2], (SCREEN_WIDTH/1.6, SCREEN_HEIGHT/2)]

    def getImgs(self):
        self.gameIntroImgs = pygame.transform.scale(pygame.image.load("gameIntro.png"), self.gameIntroScreen[2])
        self.gameIntroImgsChefs = pygame.transform.scale(pygame.image.load("chef.png"), self.gameIntroChefs[2])
        

    def gameStart(self):
        for points in fc.run(visualize=1, max_threads=4, capture=0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()

            print(points)
            self.gameBoard()
            
            self.SCREEN.blit(self.img, [0, 0])
            # self.SCREEN.blit(self.eagle_img, [100,100])
            
            pygame.display.update()

    def gameBoard(self):
        self.img = pygame.image.load(PRESENT_FRAME_WRITE_PATH)
        self.img = pygame.transform.scale(self.img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def quitGame(self):
        pygame.quit()
        sys.exit()

    def introScreen(self):
        intro = True

        self.gameStrartButton = Button(GAMESTART_BUTTON_IMG)
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.gameStrartButton.pressed(event.pos) == True:
                        self.gameStart()
                #    self.gameStart()
    

            self.SCREEN.blit(self.gameIntroImgs, self.gameIntroScreen[1])
            self.SCREEN.blit(self.gameIntroImgsChefs, self.gameIntroChefs[1])
            self.SCREEN.blit(self.gameStrartButton.button, self.gameStrartButton.rect)

            pygame.display.update()
            self.clock.tick(15)
            
        


    def run(self):
        # pygame initialize
        pygame.init()
        self.clock = pygame.time.Clock()
        self.introFactor()
        self.getImgs()
        

        self.SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
        pygame.display.set_caption("Yam-Yam")

        self.event = pygame.event.poll()

        self.introScreen()
        
            
            

            



if __name__ == "__main__":
    # generte the game
    print("Welcome to our game !!")
    game = Game()
    game.run()