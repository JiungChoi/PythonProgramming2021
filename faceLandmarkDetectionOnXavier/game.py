import facetracker_custom as fc
import pygame

import os, sys, time, random

PRESENT_FRAME_WRITE_PATH = "Jiung\jiung.png"

SCREEN_WIDTH_DEFAULT = 600
SCREEN_HEIGHT_DEFAULT = 600
INTRO_BUTTON_LARGE_HEIGHT = 100
INTRO_BUTTON_LARGE_WIDTH = 400
RUN_BUTTON_MID_HEIGHT = 100
RUN_BUTTON_MID_WIDTH = 200

RUN_BUTTON_SMALL_HEIGHT = 50
RUN_BUTTON_SMALL_WIDTH = 50

## Plus Value
SCORE_APPLE = 300
SCORE_BEEF = 1000

## Minus Value
SCORE_CUCUMBER = 500


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
    def downScore(self, value):
        if (self.score - value) > 0:
            self.score -= value
        else:
            self.score = 0

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

class FloatElement: # 부유물 클래스: 점수 클래스(plus)와, 실점(minus) 클래스로 상속한다. 
    moveDir = [[0, 0], [0, 1], [1, 0], [1, 1]] # 부유물 클래스의 방향을 정적변수로 선언
    
    def __init__(self,Floatter_IMG_PATH, w, h):
        self.floatter = pygame.image.load(Floatter_IMG_PATH)
        self.floatter = pygame.transform.scale(self.floatter,(w, h))
        self.rect = self.floatter.get_rect()
        self.rect.x = random.randint(0, game.SCREEN_WIDTH - w)
        self.rect.y = random.randint(0, game.SCREEN_HEIGHT - h)
        self.moveDir = FloatElement.moveDir[random.randrange(4)]
        if Floatter_IMG_PATH == "Images/apple.png":
            self.type = "apple"
        elif Floatter_IMG_PATH == "Images/beef.png":
            self.type = "beef"
        elif Floatter_IMG_PATH == "Images/cucumber.png":
            self.type = "cucumber"

    def randomMove(self):
        
        ## 난이도가 hard 일 때 적용
        '''
        self.rect.x += random.randrange(31) - 15 # move : -15 ~ 15 
        self.rect.y += random.randrange(11) - 5 # move : -5 ~ 5
        if self.rect.x >= game.SCREEN_WIDTH: self.rect.x -= 15
        if self.rect.y >= game.SCREEN_HEIGHT: self.rect.y -= 5 
        '''
        ## 랜덤한 속도로 이동
        if self.moveDir == [0, 0] :
            self.rect.x -= random.randrange(11)
            self.rect.y -= random.randrange(11) 
        elif self.moveDir == [0, 1] :
            self.rect.x -= random.randrange(11)
            self.rect.y += random.randrange(11)
        elif self.moveDir == [1, 0]:
            self.rect.x += random.randrange(11)
            self.rect.y -= random.randrange(11) 
        elif self.moveDir == [1, 1] :
            self.rect.x += random.randrange(11)
            self.rect.y += random.randrange(11)
        
        ## 충돌에대한 방향 보정
        ## x 좌표 보정
        if self.rect.x >= game.SCREEN_WIDTH - self.rect.w : 
            self.rect.x -= 10
            self.moveDir[0] = 0
        elif self.rect.x < self.rect.w:
            self.rect.x += 10
            self.moveDir[0] = 1
        ## y좌표 보정
        if self.rect.y >= game.SCREEN_HEIGHT-self.rect.h: 
            self.rect.y -= 10
            self.moveDir[1] = 0
        elif self.rect.y < self.rect.h:
            self.rect.y += 10
            self.moveDir[1] = 1
        
         
                 


class PlusElement(FloatElement): # 점수 클래스(plus) : 부유물 객체로 부터 상속 받는다. 
    def __init__(self, Floatter_IMG_PATH, w, h):
        super().__init__(Floatter_IMG_PATH, w, h)
    def eat(self):
        if self.type == "medicine.png":
            pass
        elif self.type == "apple":
            game.score.upScore(SCORE_APPLE)
        elif self.type == "beef":
            game.score.upScore(SCORE_BEEF)
        

class MinusElement(FloatElement): # 실점 클래스(plus) : 부유물 객체로 부터 상속 받는다.
    def __init__(self, Floatter_IMG_PATH, w, h):
        super().__init__(Floatter_IMG_PATH, w, h)
    def eat(self):
        if self.type == "cucumber":
            game.score.downScore(SCORE_CUCUMBER)
            game.life.minusLife()

class Game:
    def __init__(self): # 게임 객체를 생성했을 때
        self.userName = input("Insert your name in english : ") # 유저의 이름을 입력받음
        self.userBestScore = 0
        self.SCREEN_WIDTH = SCREEN_WIDTH_DEFAULT
        self.SCREEN_HEIGHT = SCREEN_HEIGHT_DEFAULT
        self.level = "easy"
        self.floatElements = [[],[]]
        self.gameTime = 15
        

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
        self.intro_gameStartButtonInfo = ["Images/intro_gameStrartButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - 1.9*INTRO_BUTTON_LARGE_HEIGHT ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.intro_gameSettingsButtonInfo = ["Images/intro_gameSettingsButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]        
        self.intro_quitGameButtonInfo = ["Images/intro_quitGameButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]  

        self.run_menuButtonInfo = ["Images/run_menuButton.png", [self.SCREEN_WIDTH-RUN_BUTTON_SMALL_WIDTH , 0], (RUN_BUTTON_SMALL_WIDTH, RUN_BUTTON_SMALL_HEIGHT)]
        self.run_menuToIntroButtonInfo = ["Images/run_menuToIntroButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.run_menuCancelButtonInfo = ["Images/run_menuCancelButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2  ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.run_lifeInfo = [["Images/heart1.png", "Images/heart2.png", "Images/heart3.png"], [0, 0], (RUN_BUTTON_MID_WIDTH, RUN_BUTTON_MID_HEIGHT)]
        self.run_restartGameButtonInfo = ["Images/run_restartGameButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2  ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)] 

        ## Game의 부유물 객체 관리
        self.run_plusElementInfo = [["Images/apple.png", "Images/beef.png"], [0, 0], (RUN_BUTTON_SMALL_WIDTH, RUN_BUTTON_SMALL_HEIGHT)]
        self.run_minusElementInfo = [["Images/cucumber.png"], [0, 0] , (RUN_BUTTON_SMALL_WIDTH, RUN_BUTTON_SMALL_HEIGHT)]


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
        self.run_restartGameButton = Button(self.run_restartGameButtonInfo[0], self.run_restartGameButtonInfo[1][0], self.run_restartGameButtonInfo[1][1], self.run_restartGameButtonInfo[2][0], self.run_restartGameButtonInfo[2][1] )

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
        changeColorAndSize = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
        cntForTimeSlow = 0
        while intro:
            cntForTimeSlow += 1
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

            self.gameUserNameFont = pygame.font.SysFont( 'impact', 50+ changeColorAndSize[cntForTimeSlow%10]*2, False, False)
            self.gameUserNameText = self.gameUserNameFont.render(f"{self.userName}, Are You Hungry ?!", True, (60+ changeColorAndSize[cntForTimeSlow%10],changeColorAndSize[cntForTimeSlow%10]*20 ,60+ changeColorAndSize[cntForTimeSlow%10] ))
            self.gameUserNameRect = self.gameUserNameText.get_rect()
            self.SCREEN.blit(self.gameUserNameText, [self.SCREEN_WIDTH/2 - self.gameUserNameRect.w/2, self.SCREEN_HEIGHT - self.gameUserNameRect.h])

            self.gameUserBestScoreFont = pygame.font.SysFont( 'impact', 25+changeColorAndSize[cntForTimeSlow%10], False, False)
            self.gameUserBestScoreText = self.gameUserBestScoreFont.render(f"YOUR BEST SCORE : {self.userBestScore}", True, BLACK)
            self.gameUserBestScoreRect = self.gameUserBestScoreText.get_rect()
            self.SCREEN.blit(self.gameUserBestScoreText, [self.SCREEN_WIDTH/2 - self.gameUserBestScoreRect.w/2, self.SCREEN_HEIGHT*0.01])
            
            self.SCREEN.blit(self.intro_gameStartButton.button, self.intro_gameStartButtonInfo[1])
            self.SCREEN.blit(self.intro_gameSettingsButton.button, self.intro_gameSettingsButtonInfo[1])
            self.SCREEN.blit(self.intro_quitGameButton.button, self.intro_quitGameButtonInfo[1])
            

            pygame.display.update()
            self.clock.tick(20)

    ######## 게임 스크린 ########
    def isInYourMouth(self, isPlusElement, points, element): # points: x*1.1, y*1.25
        if isPlusElement:
            if ((points[55][1]*1.25 - points[50][1]*1.25) > 50 and points[58][0]*1.1>(element.rect.x + element.rect.w/2)>points[62][0]*1.1) and (points[50][1]*1.25<(element.rect.y+ element.rect.h/2)<points[55][1]*1.25): 
                return True
        else:
            if ((points[55][1]*1.25 - points[50][1]*1.25) > 50 and points[58][0]*1.1>(element.rect.x + element.rect.w/2)>points[62][0]*1.1) and (points[50][1]*1.25<(element.rect.y+ element.rect.h/2)<points[55][1]*1.25): 
                return True
        return False
    
    def rejectOnYourMouth(self, points, element):
        if (points[55][1]*1.25 - points[50][1]*1.25 < 35) and (points[58][0]*1.1>element.rect.x + element.rect.w/2>points[62][0]*1.1) and ( (element.rect.y)<points[50][1]*1.25<(element.rect.y + element.rect.h)):
                return True
        return False

    ## GAME Finsh 메서드 오버로딩
    def gameFinish(self, TYPE):
        STOP = True
        while STOP:
            pygame.draw.rect(self.SCREEN, BLACK, [0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
            self.gamePauseFont = pygame.font.SysFont( 'impact', 40, False, False)
            if TYPE == "GAMEOVER":
                self.gamePauseText = self.gamePauseFont.render("GAME OVER", True, WHITE)
            elif TYPE == "TIMEOVER":
                self.gamePauseText = self.gamePauseFont.render("TIME OVER", True, WHITE)
            self.gamePauseTextRect = self.gamePauseText.get_rect() 
            self.SCREEN.blit(self.gamePauseText, [self.SCREEN_WIDTH/2 - self.gamePauseTextRect.w/2, self.gamePauseTextRect.h/2])
            self.SCREEN.blit(self.run_menuToIntroButton.button, self.run_menuToIntroButtonInfo[1])
            self.SCREEN.blit(self.run_restartGameButton.button, self.run_restartGameButtonInfo[1])

            ## 점수 객체 화면 출력
            self.gameScoreFont = pygame.font.SysFont( 'impact', 40, False, False)
            self.gameScoreText = self.gameScoreFont.render(f"SCORE : {self.score.score}", True, RED)
            self.gameScoreTextRect = self.gameScoreText.get_rect()
            self.SCREEN.blit(self.gameScoreText, [0, self.SCREEN_HEIGHT - self.gameScoreTextRect.h])
                
            if self.userBestScore < self.score.score: self.userBestScore = self.score.score
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.run_menuToIntroButton.pressed(event.pos) == True:
                        self.run_menuToIntroButton.switchImg("Images/run_menuToIntroButton_pressed.png")
                    elif self.run_restartGameButton.pressed(event.pos) == True:
                        self.run_restartGameButton.switchImg("Images/run_restartGameButton_pressed.png")

                elif event.type == pygame.MOUSEBUTTONUP:
                    pauseTime = time.time()
                    self.run_menuToIntroButton.switchImg("Images/run_menuToIntroButton.png")
                    self.run_restartGameButton.switchImg("Images/run_restartGameButton.png")

                    if self.run_menuToIntroButton.pressed(event.pos) == True:
                        STOP = False
                        self.floatElements = [[], []]
                        self.score.score = 0
                        self.life.life = 3
                        self.introScreen()

                    elif self.run_menuCancelButton.pressed(event.pos) == True:
                        STOP = False
                        self.floatElements = [[], []]
                        self.life.life = 3
                        self.score.score = 0
                        self.gameStart()
                        
            pygame.display.update()

    def gameStart(self):
        STOP = True
        for points in fc.run(visualize=1, max_threads=4, capture=0):
            
            while STOP:
                pygame.draw.rect(self.SCREEN, BLACK, [0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
                self.gamePauseFont = pygame.font.SysFont( 'impact', 40, False, False)
                self.gamePauseText = self.gamePauseFont.render("Press \"SpaceBar\" to Start Game ", True, WHITE)
                self.gamePauseTextRect = self.gamePauseText.get_rect() 
                self.SCREEN.blit(self.gamePauseText, [self.SCREEN_WIDTH/2 - self.gamePauseTextRect.w/2, self.SCREEN_HEIGHT/2 - self.gamePauseTextRect.h/2])

                
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            startTime = time.time()
                            STOP = False 

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
                                        self.life.life = 3
                                        self.score.score = 0
                                        self.floatElements = [[], []]
                                        self.introScreen()

                                    elif self.run_menuCancelButton.pressed(event.pos) == True:
                                        STOP = False
                                        startTime -= (time.time() - pauseTime) # 정지한 시간만큼 현재 시간 보정
                                        
                            pygame.display.update()

            
            ## 부유물 객체의 생성 [plus : minus = 8 : 2]
            if ((time.time() - startTime)%1 <0.1): # 1초에 2번 부유물 객체 생성
                plusOrMinus = random.randrange(10)
                if plusOrMinus < 8: # 2:8 = (minus:plus) 의 비율로 부유물 객체 생성 
                    self.floatElements[0].append(PlusElement(self.run_plusElementInfo[0][random.randrange(0, 2)], self.run_plusElementInfo[2][0], self.run_plusElementInfo[2][1]))
                else:
                    self.floatElements[1].append(MinusElement(self.run_minusElementInfo[0][random.randrange(0, 1)], self.run_minusElementInfo[2][0], self.run_minusElementInfo[2][1]))
            

            ## 먹은지 안 먹은지 주기적으로 검출
            for element in self.floatElements[0]:
                if (self.isInYourMouth(True , points, element)):
                    element.eat()
                    self.floatElements[0].remove(element)
            
            for element in self.floatElements[1]:
                if (self.isInYourMouth(False , points, element)):
                    element.eat()
                    if self.life.life == 0: self.gameFinish("GAMEOVER") 
                    self.floatElements[1].remove(element)
                if self.rejectOnYourMouth(points, element):
                    self.floatElements[1].remove(element)
            
            


            ## 시간 오버 체크  
            presentTime = (time.time() - startTime)//1 # 현재 시간 측정
            if (presentTime > self.gameTime):
                self.gameFinish("TIMEOVER")
            else:
                self.timmerText = self.timmerFont.render(f"{self.gameTime-int(presentTime)}", True, BLACK)
                self.timmerTextRect = self.timmerText.get_rect()

            
            ## 부유물 30개 넘으면 Game Over
            if (len(self.floatElements[0]) + len(self.floatElements[1]) > 30 ): self.gameFinish("GAMEOVER")

            ## 게임중 추가 요소는 배경 생성 후 추가해줄 것
            self.gameBoard()
            self.SCREEN.blit(self.img, [0, 0]) # 배경
            self.SCREEN.blit(self.timmerText, [self.SCREEN_WIDTH/2 - self.timmerTextRect.w/2, 0])
            self.SCREEN.blit(self.run_menuButton.button, self.run_menuButtonInfo[1])
            
            ## 점수 객체 화면 출력
            self.gameScoreFont = pygame.font.SysFont( 'impact', 40, False, False)
            self.gameScoreText = self.gameScoreFont.render(f"SCORE : {self.score.score}", True, RED)
            self.gameScoreTextRect = self.gameScoreText.get_rect()
            self.SCREEN.blit(self.gameScoreText, [0, self.SCREEN_HEIGHT - self.gameScoreTextRect.h])

            ## 현재 화면의 부유물 수 출력
            self.gameFoodNumFont = pygame.font.SysFont( 'impact', 40, False, False)
            self.gameFoodNumText = self.gameFoodNumFont.render(f"FOOD NUMBER : {len(self.floatElements[0]) + len(self.floatElements[1])}", True, BLUE)
            self.gameFoodNumRect = self.gameFoodNumText.get_rect()
            self.SCREEN.blit(self.gameFoodNumText, [self.SCREEN_WIDTH - self.gameFoodNumRect.w, self.SCREEN_HEIGHT - self.gameFoodNumRect.h])

            ## 부유물 객체를 출력
            for element in self.floatElements[0]:
                self.SCREEN.blit(element.floatter, (element.rect.x, element.rect.y))
            for element in self.floatElements[1]:
                self.SCREEN.blit(element.floatter, (element.rect.x, element.rect.y))
                
            ## 부유물 객체의 이동
            for elementType in self.floatElements:
                for element in elementType:
                    element.randomMove()


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
        self.score = Score()
        


        ## 게임 실행 첫 화면은 인트로로 실행
        self.introScreen()
        
            
            
if __name__ == "__main__":
    # generte the game
    print("Welcome to our game !!")
    game = Game()
    game.run()