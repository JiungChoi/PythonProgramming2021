import facetracker_custom as fc
import pygame

import os, sys

PRESENT_FRAME_WRITE_PATH = "Jiung\jiung.jpg"

SCREEN_WIDTH_DEFAULT = 800
SCREEN_HEIGHT_DEFAULT = 800
BUTTON_START_HEIGHT = 100
BUTTON_START_WIDTH = 400

#### COLOR ####
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
        self.rect.x = game.SCREEN_WIDTH/2 - BUTTON_START_WIDTH/2
        self.rect.y = game.SCREEN_HEIGHT/2 - BUTTON_START_HEIGHT/2
        
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
    def __init__(self): # 게임 객체를 생성했을 때
        self.userName = input("Insert user info : ") # 유저의 이름을 입력받음
        self.SCREEN_WIDTH = SCREEN_WIDTH_DEFAULT
        self.SCREEN_HEIGHT = SCREEN_HEIGHT_DEFAULT

    ######### 환경 설정 #########

    def windowSet(self, width, height): # 게임의 스크린 크기를 조정하고 싶을 때
        self.SCREEN_WIDTH = width 
        self.SCREEN_HEIGHT = height

    def userSet(self, name): #유저의 이름을 바꾸고 싶을 때
        self.userName = name


    ######### 게임 요소 #########
    def gameFactor(self): # 이미지 파일들의 정보를 관리 : [경로, [x,y], (width, height))]
        self.intro_gameScreen = ["gameIntro.png", [0, 0] , (self.SCREEN_WIDTH,self.SCREEN_HEIGHT)]
        self.intro_chef = ["chef.png", [self.SCREEN_WIDTH/2 - 0.5*self.SCREEN_WIDTH/1.6, self.SCREEN_HEIGHT- self.SCREEN_HEIGHT/2], (self.SCREEN_WIDTH/1.6, self.SCREEN_HEIGHT/2)]
        self.button = ["button.png", "NONE", (BUTTON_START_WIDTH, BUTTON_START_HEIGHT)]


    def getImgs(self):
        self.imgs_intro_gameScreen = pygame.transform.scale(pygame.image.load(self.intro_gameScreen[0]), self.intro_gameScreen[2])
        self.imgs_intro_chef = pygame.transform.scale(pygame.image.load(self.intro_chef[0]), self.intro_chef[2])
        
    ######## 게임 스크린 ########
    def gameStart(self):
        for points in fc.run(visualize=1, max_threads=4, capture=0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()

            #print(points)
            self.gameBoard()
            
            self.SCREEN.blit(self.img, [0, 0])
            pygame.display.update()



    def gameBoard(self):
        self.img = pygame.image.load(PRESENT_FRAME_WRITE_PATH)
        self.img = pygame.transform.scale(self.img, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def quitGame(self):
        pygame.quit()
        sys.exit()

    ######## 게임 첫 화면 ########
    def introScreen(self):
        intro = True

        self.gameStrartButton = Button(self.button[0]) # 버튼 생성
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.gameStrartButton.pressed(event.pos) == True:
                        self.gameStart()
                
    

            self.SCREEN.blit(self.imgs_intro_gameScreen, self.intro_gameScreen[1])
            self.SCREEN.blit(self.imgs_intro_chef, self.intro_chef[1])
            self.SCREEN.blit(self.gameStrartButton.button, self.gameStrartButton.rect)

            pygame.display.update()
            self.clock.tick(15)
            
        


    def run(self):
        # pygame initialize
        pygame.init() 
        self.clock = pygame.time.Clock()
        self.gameFactor() 
        self.getImgs()
        

        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT)) 
        pygame.display.set_caption("Yam-Yam")

        self.event = pygame.event.poll()

        self.introScreen()
        
            
            

            



if __name__ == "__main__":
    # generte the game
    print("Welcome to our game !!")
    game = Game()
    game.run()