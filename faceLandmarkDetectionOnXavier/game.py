import facetracker_custom as fc
import pygame

import os, sys, time

PRESENT_FRAME_WRITE_PATH = "Jiung\jiung.png"

SCREEN_WIDTH_DEFAULT = 800
SCREEN_HEIGHT_DEFAULT = 800
INTRO_BUTTON_LARGE_HEIGHT = 100
INTRO_BUTTON_LARGE_WIDTH = 400
RUN_BUTTON_MID_HEIGHT = 100
RUN_BUTTON_MID_WIDTH = 200

RUN_BUTTON_SMALL_HEIGHT = 50
RUN_BUTTON_SMALL_WIDTH = 50

STOP = True

#### COLOR ####
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Life():
    def __init__(self):
        self.life = 3
    def minusLife (self):
        self.life -= 1
    
class Score():
    def __init__(self):
        self.score = 0
    def upScore(self, value):
        self.score += value
    def minusScore(self, value):
        self.score -= value


class Button():
    def __init__(self, BUTTON_IMG_PATH, x, y, w, h):
        self.button = pygame.image.load(BUTTON_IMG_PATH)
        self.button = pygame.transform.scale(self.button,(w, h))
        self.rect = self.button.get_rect()
        self.rect.x = x
        self.rect.y = y

    def switchImg(self, imgPath):
        self.button = self.button = pygame.image.load(imgPath)
        self.button = pygame.transform.scale(self.button, (self.rect.w, self.rect.h))
        
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
        self.level = "easy"

    ########### 환경 설정 ###########

    def windowSet(self, width, height): # 게임의 스크린 크기를 조정하고 싶을 때
        self.SCREEN_WIDTH = width 
        self.SCREEN_HEIGHT = height

    def userSet(self, name): #유저의 이름을 바꾸고 싶을 때
        self.userName = name


    ########### 게임 요소 ###########
    def gameFactor(self): # 이미지 파일들의 정보를 관리 : [경로, [x,y], (width, height))]
        self.intro_gameScreenInfo = ["Images/intro_gameScreen.png", [0, 0] , (self.SCREEN_WIDTH,self.SCREEN_HEIGHT)]
        self.intro_chefInfo = ["Images/chef.png", [self.SCREEN_WIDTH/2 - 0.5*self.SCREEN_WIDTH/1.6, self.SCREEN_HEIGHT- self.SCREEN_HEIGHT/2], (self.SCREEN_WIDTH/1.6, self.SCREEN_HEIGHT/2)]
        self.intro_gameStartButtonInfo = ["Images/intro_gameStrartButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - 2*INTRO_BUTTON_LARGE_HEIGHT ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.intro_gameSettingsButtonInfo = ["Images/intro_gameSettingsButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]        
        self.intro_quitGameButtonInfo = ["Images/intro_quitGameButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]  

        self.run_menuButtonInfo = ["Images/run_menuButton.png", [self.SCREEN_WIDTH-RUN_BUTTON_SMALL_WIDTH , 0], (RUN_BUTTON_SMALL_WIDTH, RUN_BUTTON_SMALL_HEIGHT)]
        self.run_menuToIntroButtonInfo = ["Images/run_menuToIntroButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.run_menuCancelButtonInfo = ["Images/run_menuCancelButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2  ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.run_lifeInfo = [["Images/heart1.png", "Images/heart2.png", "Images/heart3.png"], [0, 0], (RUN_BUTTON_MID_WIDTH, RUN_BUTTON_MID_HEIGHT)]

    def getImgs(self):
        self.imgs_intro_gameScreenInfo = pygame.transform.scale(pygame.image.load(self.intro_gameScreenInfo[0]), self.intro_gameScreenInfo[2])
        self.imgs_intro_chefInfo = pygame.transform.scale(pygame.image.load(self.intro_chefInfo[0]), self.intro_chefInfo[2])
        self.imgs_run_heart1 = pygame.transform.scale(pygame.image.load(self.run_lifeInfo[0][0]), self.run_lifeInfo[2])
        self.imgs_run_heart2 = pygame.transform.scale(pygame.image.load(self.run_lifeInfo[0][1]), self.run_lifeInfo[2])
        self.imgs_run_heart3 = pygame.transform.scale(pygame.image.load(self.run_lifeInfo[0][2]), self.run_lifeInfo[2])
    
    def buttons_generate(self):
        self.intro_gameStartButton = Button(self.intro_gameStartButtonInfo[0], self.intro_gameStartButtonInfo[1][0], self.intro_gameStartButtonInfo[1][1], self.intro_gameStartButtonInfo[2][0], self.intro_gameStartButtonInfo[2][1]) # 인트로 게임 시작 버튼 생성
        self.intro_gameSettingsButton = Button(self.intro_gameSettingsButtonInfo[0], self.intro_gameSettingsButtonInfo[1][0], self.intro_gameSettingsButtonInfo[1][1], self.intro_gameSettingsButtonInfo[2][0], self.intro_gameSettingsButtonInfo[2][1]) #인트로 게임 설정 버튼 생성
        self.intro_quitGameButton = Button(self.intro_quitGameButtonInfo[0], self.intro_quitGameButtonInfo[1][0], self.intro_quitGameButtonInfo[1][1], self.intro_quitGameButtonInfo[2][0], self.intro_quitGameButtonInfo[2][1] )

        self.run_menuButton = Button(self.run_menuButtonInfo[0], self.run_menuButtonInfo[1][0], self.run_menuButtonInfo[1][1], self.run_menuButtonInfo[2][0], self.run_menuButtonInfo[2][1] )
        self.run_menuToIntroButton = Button(self.run_menuToIntroButtonInfo[0], self.run_menuToIntroButtonInfo[1][0], self.run_menuToIntroButtonInfo[1][1], self.run_menuToIntroButtonInfo[2][0], self.run_menuToIntroButtonInfo[2][1] )
        self.run_menuCancelButton = Button(self.run_menuCancelButtonInfo[0], self.run_menuCancelButtonInfo[1][0], self.run_menuCancelButtonInfo[1][1], self.run_menuCancelButtonInfo[2][0], self.run_menuCancelButtonInfo[2][1] )

    ########## 게임 세팅 ##########
    def gameBoard(self):
        self.img = pygame.image.load(PRESENT_FRAME_WRITE_PATH)
        self.img = pygame.transform.scale(self.img, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def quitGame(self):
        pygame.quit()
        sys.exit()

    ########## 게임 인트로 ##########
    def introScreen(self):
        intro = True
        while intro:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.intro_gameStartButton.pressed(event.pos) == True:
                        self.intro_gameStartButton.switchImg("Images/intro_gameStrartButton_pressed.png")
                    elif self.intro_gameSettingsButton.pressed(event.pos) == True:
                        self.intro_gameSettingsButton.switchImg("Images/intro_gameSettingsButton_pressed.png")
                    elif self.intro_quitGameButton.pressed(event.pos) == True:
                        self.intro_quitGameButton.switchImg("Images/intro_quitGameButton_pressed.png")

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.intro_gameStartButton.switchImg("Images/intro_gameStrartButton.png")
                    self.intro_gameSettingsButton.switchImg("Images/intro_gameSettingsButton.png")
                    self.intro_quitGameButton.switchImg("Images/intro_quitGameButton.png")

                    if self.intro_gameStartButton.pressed(event.pos) == True:
                        self.gameStart()
                    elif self.intro_gameSettingsButton.pressed(event.pos) == True:
                        print("기능 미구현")
                    elif self.intro_quitGameButton.pressed(event.pos) == True:
                        self.quitGame()

            self.SCREEN.blit(self.imgs_intro_gameScreenInfo, self.intro_gameScreenInfo[1])
            self.SCREEN.blit(self.imgs_intro_chefInfo, self.intro_chefInfo[1])
            self.SCREEN.blit(self.intro_gameStartButton.button, self.intro_gameStartButtonInfo[1])
            self.SCREEN.blit(self.intro_gameSettingsButton.button, self.intro_gameSettingsButtonInfo[1])
            self.SCREEN.blit(self.intro_quitGameButton.button, self.intro_quitGameButtonInfo[1])
            

            pygame.display.update()
            self.clock.tick(20)


    ######## 게임 스크린 ########
    def gameStart(self):
        startTime = time.time()

        for points in fc.run(visualize=1, max_threads=4, capture=0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.run_menuButton.pressed(event.pos) == True:
                        STOP = True
                        while STOP:
                            self.SCREEN.blit(self.run_menuToIntroButton.button, self.run_menuToIntroButtonInfo[1])
                            self.SCREEN.blit(self.run_menuCancelButton.button, self.run_menuCancelButtonInfo[1])

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    self.quitGame()
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    if self.run_menuToIntroButton.pressed(event.pos) == True:
                                        self.run_menuToIntroButton.switchImg("Images/run_menuToIntroButton_pressed.png")
                                    elif self.run_menuCancelButton.pressed(event.pos) == True:
                                        self.run_menuCancelButton.switchImg("Images/run_menuCancelButton_pressed.png")

                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pauseTime = time.time()
                                    self.run_menuToIntroButton.switchImg("Images/run_menuToIntroButton.png")
                                    self.run_menuCancelButton.switchImg("Images/run_menuCancelButton.png")

                                    if self.run_menuToIntroButton.pressed(event.pos) == True:
                                        self.introScreen()
                                    elif self.run_menuCancelButton.pressed(event.pos) == True:
                                        STOP = False
                                        startTime -= (time.time() - pauseTime) # 정지한 시간만큼 현재 시간 보정
                                        

                            pygame.display.update()

                
            presentTime = (time.time() - startTime)//1 # 현재 시간 측정
            self.timmerText = self.timmerFont.render(f"{60-int(presentTime)}", True, BLACK)
            self.timmerTextRect = self.timmerText.get_rect() 
            
            self.gameBoard()
            self.SCREEN.blit(self.img, [0, 0])
            self.SCREEN.blit(self.timmerText, [self.SCREEN_WIDTH/2 - self.timmerTextRect.w/2, 0])
            self.SCREEN.blit(self.run_menuButton.button, self.run_menuButtonInfo[1])

            print(self.life.life)
            if self.life.life == 3:
                self.SCREEN.blit(self.imgs_run_heart3, self.run_lifeInfo[1]) 
            elif self.life.life ==2:
                self.SCREEN.blit(self.imgs_run_heart2, self.run_lifeInfo[1])
            elif self.life.life ==1:
                self.SCREEN.blit(self.imgs_run_heart1, self.run_lifeInfo[1])

            pygame.display.update()

    ######## 게임 프로그램 실행 ########
    def run(self):
        pygame.init() # 파이게임 라이브러리 초기 세팅
        self.clock = pygame.time.Clock() # timmer 사용을 위한 객체 생성 
        self.gameFactor()  # 어떤 요소를 만들지 선언
        self.getImgs() # gameFactor에서 선언한 요소의 이미지 파일을 불러들인다. [객체는 제외  Ex) Button ]
        self.buttons_generate() # 모든 버튼 생성 메서드
        self.timmerFont = pygame.font.SysFont( 'impact', 70, False, False) # 시간을 화면에 출력해줄 폰트객체 생성
        self.life = Life()
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT)) # 스크린 객체 생성
        pygame.display.set_caption("Yam-Yam") # 게임 타이틀 선언
        self.event = pygame.event.poll() # 이벤트 객체 생성


        ## 게임 실행 첫 화면은 인트로로 실행
        self.introScreen()
        
            
            



if __name__ == "__main__":
    # generte the game
    print("Welcome to our game !!")
    game = Game()
    game.run()