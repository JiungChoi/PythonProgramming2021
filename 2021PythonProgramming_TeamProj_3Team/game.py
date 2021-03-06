import facetracker_custom as fc
import pygame

import os, sys, time, random

PRESENT_FRAME_WRITE_PATH = "Jiung\jiung.png"

## 게임 요소들의 크기를 상수로 정의
SCREEN_WIDTH_DEFAULT = 600
SCREEN_HEIGHT_DEFAULT = 600
INTRO_BUTTON_LARGE_WIDTH = SCREEN_WIDTH_DEFAULT*0.3
INTRO_BUTTON_LARGE_HEIGHT = SCREEN_HEIGHT_DEFAULT*0.1
RUN_BUTTON_MID_WIDTH = SCREEN_WIDTH_DEFAULT*0.2
RUN_BUTTON_MID_HEIGHT = SCREEN_WIDTH_DEFAULT*0.2
RUN_BUTTON_SMALL_WIDTH = SCREEN_WIDTH_DEFAULT*0.15
RUN_BUTTON_SMALL_HEIGHT = SCREEN_HEIGHT_DEFAULT*0.15
RUN_BUTTON_FIRE_WIDTH = SCREEN_WIDTH_DEFAULT*0.1
RUN_BUTTON_FIRE_HEIGHT = SCREEN_HEIGHT_DEFAULT*0.1

## Plus Value : 게임에 돌아다니는 부유물 객체의 점수를 정의
SCORE_CHICKEN = 1000
SCORE_BEEF = 2000
SCORE_SUSHI = 3000

## Minus Value : 게임에 돌아다니는 부유물 객체의 점수를 정의
SCORE_CUCUMBER = 500

## 게임 일시 정지에 사용되는 Flag
STOP = True

## COLOR : 게임에 사용될 색깔 값 상수로 정의 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
BRONZE = (153, 102, 0)

## 유저의 생명을 관리하는 Life 클래스
class Life():
    def __init__(self):
        self.life = 3
    def plusLife (self, value):
        if self.life < 3:
            self.life += value
        else:
            pass

    def minusLife (self, value):
        self.life -= value
    

## 유저의 점수를 관리하는 Score 클래스
class Score():
    def __init__(self):
        self.score = 0
    # 현재 게임 모드에 따라서 점수가 반영 된다.
    def upScore(self, value): 
        if PlusElement.DOUBLE_MODE == True: 
            if MinusElement.Minus_MODE == True: 
                self.score += int(2*0.7*value) 
            else:
                self.score += int(2*value) 
        else:
            if MinusElement.Minus_MODE == True: 
                self.score += int(0.7*value)
            else: 
                self.score += value 
                
    # 현재 게임 모드에 따라서 점수가 반영 된다.
    def downScore(self, value): 
        if (self.score - value) > 0:
            self.score -= value
        else:
            self.score = 0

## 게임에 사용되는 버튼 클래스
class Button():
    def __init__(self, BUTTON_IMG_PATH, x, y, w, h): # 버튼 클래스는 생성과 동시에 경로를 포함한 이미지 정보를 통해 파이게임에서 사용 가능한 이미지 객체로 생성
        self.button = pygame.image.load(BUTTON_IMG_PATH)
        self.button = pygame.transform.scale(self.button,(w, h))
        self.rect = self.button.get_rect()
        self.rect.x = x
        self.rect.y = y

    def switchImg(self, imgPath): # 눌렀을 때 이미지가 변환 되도록 해줄 메서드
        self.button = self.button = pygame.image.load(imgPath)
        self.button = pygame.transform.scale(self.button, (self.rect.w, self.rect.h))
        
    def pressed(self, mouse): # 버튼이 눌린지 아닌지 검출해줄 메서드
        if self.rect.collidepoint(mouse) == True:
            return True

## 부유물 클래스: 점수 클래스(plus)와, 실점(minus) 클래스로 상속한다.
class FloatElement: 
    # 부유물 클래스의 이동 방향을 정적변수로 선언
    moveDir = [[0, 0], [0, 1], [1, 0], [1, 1]] 
    
    def __init__(self,Floatter_IMG_PATH, w, h):
        self.floatter = pygame.image.load(Floatter_IMG_PATH)
        self.floatter = pygame.transform.scale(self.floatter,(w, h))
        self.rect = self.floatter.get_rect()
        self.rect.x = random.randint(0, game.SCREEN_WIDTH - w)
        self.rect.y = random.randint(0, game.SCREEN_HEIGHT - h)
        self.moveDir = FloatElement.moveDir[random.randrange(4)]
        if Floatter_IMG_PATH == "Images/chicken.png":
            self.type = "chicken"
        elif Floatter_IMG_PATH == "Images/beef.png":
            self.type = "beef"
        elif Floatter_IMG_PATH == "Images/sushi.png":
            self.type = "sushi"
        elif Floatter_IMG_PATH == "Images/goldApple.png":
            self.type = "goldApple"
        elif Floatter_IMG_PATH == "Images/medicine.png":
            self.type = "medicine"
        elif Floatter_IMG_PATH == "Images/cucumber.png":
            self.type = "cucumber" 
        elif Floatter_IMG_PATH == "Images/redMushroom.png":
            self.type = "redMushroom"
    
    ## 난이도에 따라 다른 이동
    def randomMove(self):

        # 난이도 easy
        if game.gameMode == "easy":
            self.rect.x += random.randrange(31) - 15 # move : -15 ~ 15 
            self.rect.y += random.randrange(11) - 5 # move : -5 ~ 5
            # 충돌에대한 방향 보정
            if self.rect.x > game.SCREEN_WIDTH: self.rect.x -= 30
            elif self.rect.x < 0: self.rect.x += 30
            if self.rect.y > game.SCREEN_HEIGHT: self.rect.y -= 30
            elif self.rect.y < 0: self.rect.y += 30
        
        # 난이도 nomal
        if game.gameMode == "nomal":
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

            # 충돌에대한 방향 보정
            # x 좌표 보정
            if self.rect.x >= game.SCREEN_WIDTH - self.rect.w : 
                self.rect.x -= 10
                self.moveDir[0] = 0
            elif self.rect.x < self.rect.w:
                self.rect.x += 10
                self.moveDir[0] = 1
            # y좌표 보정
            if self.rect.y >= game.SCREEN_HEIGHT-self.rect.h: 
                self.rect.y -= 10
                self.moveDir[1] = 0
            elif self.rect.y < self.rect.h:
                self.rect.y += 10
                self.moveDir[1] = 1

        # 난이도 hard
        if game.gameMode == "hard":
            if self.moveDir == [0, 0] :
                self.rect.x -= random.randrange(31)
                self.rect.y -= random.randrange(31) 
            elif self.moveDir == [0, 1] :
                self.rect.x -= random.randrange(31)
                self.rect.y += random.randrange(31)
            elif self.moveDir == [1, 0]:
                self.rect.x += random.randrange(31)
                self.rect.y -= random.randrange(31) 
            elif self.moveDir == [1, 1] :
                self.rect.x += random.randrange(31)
                self.rect.y += random.randrange(31)

            # 충돌에대한 방향 보정
            # x 좌표 보정
            if self.rect.x >= game.SCREEN_WIDTH - self.rect.w : 
                self.rect.x -= 30
                self.moveDir[0] = 0
            elif self.rect.x < self.rect.w:
                self.rect.x += 30
                self.moveDir[0] = 1
            # y좌표 보정
            if self.rect.y >= game.SCREEN_HEIGHT-self.rect.h: 
                self.rect.y -= 30
                self.moveDir[1] = 0
            elif self.rect.y < self.rect.h:
                self.rect.y += 30
                self.moveDir[1] = 1

# 부유물 클래스(plus, 점수 획득요소) : 부유물 객체로 부터 상속 받는다.
class PlusElement(FloatElement): 
    DOUBLE_MODE = False
    def __init__(self, Floatter_IMG_PATH, w, h):
        super().__init__(Floatter_IMG_PATH, w, h) 

    def eat(self):
        if self.type == "medicine.png":
            pass
        elif self.type == "chicken":
            game.score.upScore(SCORE_CHICKEN)
        elif self.type == "beef":
            game.score.upScore(SCORE_BEEF) 
        elif self.type == "sushi":
            game.score.upScore(SCORE_SUSHI)
        elif self.type == "goldApple":
            PlusElement.DOUBLE_MODE = True
            return True
        elif self.type == "medicine":
            if MinusElement.Minus_MODE == True:
                MinusElement.Minus_MODE = False
            game.life.plusLife(1)
        return False

# 부유물 클래스(minus, 실점 요소) : 부유물 객체로 부터 상속 받는다.
class MinusElement(FloatElement):
    Minus_MODE = False
    def __init__(self, Floatter_IMG_PATH, w, h):
        super().__init__(Floatter_IMG_PATH, w, h)
        
    def eat(self):
        if self.type == "cucumber":
            game.score.downScore(SCORE_CUCUMBER) 
            game.life.minusLife(1)
        elif self.type == "redMushroom":
            MinusElement.Minus_MODE = True
            game.life.minusLife(2)
            


'''
    <게임 객체의 메서드 구성>
    ##### 게임 세팅
       ## 게임 객체 생성자
       ## 게임판 생성
                    
    ##### 게임 관리 도우미
       ## 문자 출력 도우미

    ##### 환경 설정
       ## 메인
       ## 게임 난이도 설정
       ## 유저 랭킹      

    ##### 게임 요소 관리
       ## 이미지 파일 관리
       ## 이미지 파일 생성
       ## 버튼 생성
       
    ##### 게임 인트로
       ## 인트로 메인 화면 출력

    ##### 게임 실행
       ## 먹은 음식 검출
       ## 거부한 음식 검출
       ## 게임 종료
       ## 게임 요소 정리
       ## 부유물 객체 생성
       ## 식사, 시간, 이벤트 체크
       ## 게임 시작
       ## 게임 프로그램 실행

    ##### 게임 프로그램 종료
       ## 저장 및 종료
'''



class Game:
    ########## 게임 세팅 ##########
    ## 게임 세팅 : 게임 객체의 생성자 
    def __init__(self): 
        self.userName = input("Insert your name in english : ") # 유저의 이름을 입력받음
        self.userBestScore = 0
        self.SCREEN_WIDTH = SCREEN_WIDTH_DEFAULT
        self.SCREEN_HEIGHT = SCREEN_HEIGHT_DEFAULT
        self.gameMode = "nomal"
        self.floatElements = [[],[]]
        self.gameTime = 60
        self.userHistory = False
        
        # user 관리 파일을 유저의 열어서 최고 점수를 불러온다.
        for user in open("User/userInfo.txt", "r", encoding="UTF-8"):
            user = user.split()
            if self.userName == user[0]:
                self.userBestScore = user[1]
                self.userHistory = True

    ## 게임 세팅 : 게임판 객체 생성
    def gameBoard(self):
        self.img = pygame.image.load(PRESENT_FRAME_WRITE_PATH)
        self.img = pygame.transform.scale(self.img, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))


    ########## 게임 관리 도우미 ##########
    ## 게임 관리 도우미: 문자 출력 도우미
    def textHelpper(self, TEXT, SIZE, COLOR, X, Y):
        self.gameFont = pygame.font.SysFont( 'impact', SIZE, False, False)
        self.gameText = self.gameFont.render(f"{TEXT}", True, COLOR)
        self.gameTextRect = self.gameText.get_rect() 
        self.SCREEN.blit(self.gameText, [X - self.gameTextRect.w/2, Y - self.gameTextRect.h/2])


    ########### 환경 설정 ###########
    ## 환경 설정 메인
    def gameSettings(self):
        STOP = True
        self.SCREEN.blit(self.imgs_intro_gameScreenInfo, self.intro_gameScreenInfo[1])
        self.SCREEN.blit(self.imgs_intro_chefInfo, self.intro_chefInfo[1])
        while STOP:
            self.SCREEN.blit(self.settings_modeButton.button, self.settings_modeButtonInfo[1])
            self.SCREEN.blit(self.settings_userButton.button, self.settings_userButtonInfo[1])
            self.SCREEN.blit(self.run_menuCancelButton.button, [self.run_menuCancelButtonInfo[1][0], self.run_menuCancelButtonInfo[1][1]])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if self.settings_modeButton.pressed(event.pos) == True:
                        self.settings_modeButton.switchImg("Images/settings_modeButton_pressed.png")
                    elif self.settings_userButton.pressed(event.pos) == True:
                        self.settings_userButton.switchImg("Images/settings_userButton_pressed.png")
                    elif self.run_menuCancelButton.pressed(event.pos) == True:
                        self.run_menuCancelButton.switchImg("Images/run_menuCancelButton_pressed.png")

                elif event.type == pygame.MOUSEBUTTONUP:
                    pauseTime = time.time()
                    self.settings_modeButton.switchImg("Images/settings_modeButton.png")
                    self.settings_userButton.switchImg("Images/settings_userButton.png")
                    self.run_menuCancelButton.switchImg("Images/run_menuCancelButton.png")

                    if self.settings_modeButton.pressed(event.pos) == True:
                        self.gameSettingsModeSelect()
                    elif self.settings_userButton.pressed(event.pos) == True:
                        self.gameSettingsPrintUserRanking()
                    elif self.run_menuCancelButton.pressed(event.pos) == True:
                        self.introScreen()

    ## 환경 설정 : 게임 난이도 설정
    def gameSettingsModeSelect(self):
        STOP = True
        self.SCREEN.blit(self.imgs_intro_gameScreenInfo, self.intro_gameScreenInfo[1])
        self.SCREEN.blit(self.imgs_intro_chefInfo, self.intro_chefInfo[1])
        while STOP:
            self.SCREEN.blit(self.settings_modeEasyButton.button, self.settings_modeEasyButtonInfo[1])
            self.SCREEN.blit(self.settings_modeNomalButton.button, self.settings_modeNomalButtonInfo[1])
            self.SCREEN.blit(self.settings_modeHardButton.button, self.settings_modeHardButtonInfo[1])
            self.SCREEN.blit(self.settings_menuCancelButton.button, [self.settings_userButtonInfo[1][0], self.settings_userButtonInfo[1][1]+ 2*self.settings_userButtonInfo[2][1]])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.settings_modeEasyButton.pressed(event.pos) == True:
                        self.settings_modeEasyButton.switchImg("Images/settings_modeEasyButton_pressed.png")
                    elif self.settings_modeNomalButton.pressed(event.pos) == True:
                        self.settings_modeNomalButton.switchImg("Images/settings_modeNomalButton_pressed.png")
                    elif self.settings_modeHardButton.pressed(event.pos) == True:
                        self.settings_modeHardButton.switchImg("Images/settings_modeHardButton_pressed.png")
                    elif self.settings_menuCancelButton.pressed(event.pos) == True:
                        self.settings_menuCancelButton.switchImg("Images/run_menuCancelButton_pressed.png")

                elif event.type == pygame.MOUSEBUTTONUP:
                    pauseTime = time.time()
                    self.settings_modeEasyButton.switchImg("Images/settings_modeEasyButton.png")
                    self.settings_modeNomalButton.switchImg("Images/settings_modeNomalButton.png")
                    self.settings_modeHardButton.switchImg("Images/settings_modeHardButton.png")
                    self.settings_menuCancelButton.switchImg("Images/run_menuCancelButton.png")

                    if self.settings_modeEasyButton.pressed(event.pos) == True:
                        self.gameMode = "easy"
                        self.introScreen()
                    elif self.settings_modeNomalButton.pressed(event.pos) == True:
                        self.gameMode = "nomal"
                        self.introScreen()
                    elif self.settings_modeHardButton.pressed(event.pos) == True:
                        self.gameMode = "hard"
                        self.introScreen()
                    elif self.settings_menuCancelButton.pressed(event.pos) == True:
                        self.gameSettings()

            pygame.display.update()

    ## 환경 설정 : 유저 랭킹 출력
    def gameSettingsPrintUserRanking(self):
        STOP = True
        self.SCREEN.blit(self.settings_userRanking, self.settings_userRankingInfo[1])
        
        ## 유저 정보 열람
        userRank = []
        for user in open("User/userInfo.txt", "r", encoding="UTF-8"):
            user = user.split()
            if len(userRank) == 0:
                userRank.append(user)
            else:
                for rankCnt in range(len(userRank)):
                    if int(userRank[rankCnt][1]) < int(user[1]):
                        userRank.insert(rankCnt, user)
                        if len(userRank) > 10: userRank.pop()
                        break         
        while STOP:
            self.SCREEN.blit(self.run_menuButton.button, self.run_menuButtonInfo[1])

            for rank in range(len(userRank)):
                if rank == 0:
                    self.textHelpper(f"{rank+1}st {userRank[rank][0]} : {userRank[rank][1]}", 35, GOLD, self.SCREEN_WIDTH/2, self.SCREEN_WIDTH*0.07*(rank+4))
                elif rank == 1:
                    self.textHelpper(f"{rank+1}st {userRank[rank][0]} : {userRank[rank][1]}", 33, SILVER, self.SCREEN_WIDTH/2, self.SCREEN_WIDTH*0.07*(rank+4))
                elif rank == 2:
                    self.textHelpper(f"{rank+1}st {userRank[rank][0]} : {userRank[rank][1]}", 31, BRONZE, self.SCREEN_WIDTH/2, self.SCREEN_WIDTH*0.07*(rank+4))
                else:
                    self.textHelpper(f"{rank+1}st {userRank[rank][0]} : {userRank[rank][1]}", 20, BLACK, self.SCREEN_WIDTH/2, self.SCREEN_WIDTH*0.07*(rank+4))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.run_menuButton.pressed(event.pos) == True:
                        self.introScreen()

            pygame.display.update()


    ########### 게임 요소 관리 ###########
    ## 게임 요소 관리 : 이미지 파일들의 정보를 관리 ... [경로, [x,y], (width, height))]
    def gameFactor(self): 
        self.intro_gameScreenInfo = ["Images/intro_gameScreen.png", [0, 0] , (self.SCREEN_WIDTH,self.SCREEN_HEIGHT)]
        self.intro_chefInfo = ["Images/chef.png", [self.SCREEN_WIDTH/2 - 0.5*self.SCREEN_WIDTH/1.6, self.SCREEN_HEIGHT- self.SCREEN_HEIGHT/2], (self.SCREEN_WIDTH/1.6, self.SCREEN_HEIGHT/2)]
        self.intro_gameStartButtonInfo = ["Images/intro_gameStrartButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - 2*INTRO_BUTTON_LARGE_HEIGHT ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.intro_gameSettingsButtonInfo = ["Images/intro_gameSettingsButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]        
        self.intro_quitGameButtonInfo = ["Images/intro_quitGameButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]  

        self.settings_modeButtonInfo = ["Images/settings_modeButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - 2*INTRO_BUTTON_LARGE_HEIGHT ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.settings_userButtonInfo = ["Images/settings_userButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2- INTRO_BUTTON_LARGE_HEIGHT], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]   
        self.settings_modeEasyButtonInfo = ["Images/settings_windowSettingsButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - 2*INTRO_BUTTON_LARGE_HEIGHT ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.settings_modeNomalButtonInfo = ["Images/settings_modeButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.settings_modeHardButtonInfo = ["Images/settings_userButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]   
        self.settings_userRankingInfo = ["Images/settings_userInfoScreen.png", [0, 0], (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)]

        self.run_menuButtonInfo = ["Images/run_menuButton.png", [self.SCREEN_WIDTH-RUN_BUTTON_SMALL_WIDTH , 0], (RUN_BUTTON_SMALL_WIDTH, RUN_BUTTON_SMALL_HEIGHT)]
        self.run_menuToIntroButtonInfo = ["Images/run_menuToIntroButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.run_menuCancelButtonInfo = ["Images/run_menuCancelButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2  ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.run_lifeInfo = [["Images/heart1.png", "Images/heart2.png", "Images/heart3.png"], [0, 0], (RUN_BUTTON_MID_WIDTH, RUN_BUTTON_MID_HEIGHT)]
        self.run_restartGameButtonInfo = ["Images/run_restartGameButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2  ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)] 
        self.run_yesButtonInfo = ["Images/run_yesButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.run_noButtonInfo = ["Images/run_noButton.png", [self.SCREEN_WIDTH/2 - INTRO_BUTTON_LARGE_WIDTH/2, self.SCREEN_HEIGHT/2 - INTRO_BUTTON_LARGE_HEIGHT/2 ], (INTRO_BUTTON_LARGE_WIDTH, INTRO_BUTTON_LARGE_HEIGHT)]
        self.run_fireInfo = ["Images/fire.png", [0, 0], (RUN_BUTTON_FIRE_WIDTH, RUN_BUTTON_FIRE_HEIGHT)]
        self.run_bandInfo = ["Images/band.png", [0, 0], (RUN_BUTTON_FIRE_WIDTH, RUN_BUTTON_FIRE_HEIGHT)]
        self.run_waitingScreenEasyInfo = ["Images/run_waitingScreenEasy.png", [0, 0], (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)]
        self.run_waitingScreenNomalInfo = ["Images/run_waitingScreenNomal.png", [0, 0], (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)]
        self.run_waitingScreenHardInfo = ["Images/run_waitingScreenHard.png", [0, 0], (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)]


        ## Game의 부유물 객체 관리
        self.run_plusElementInfo = [["Images/chicken.png", "Images/beef.png", "Images/sushi.png", "Images/goldApple.png","Images/medicine.png"], [0, 0], (RUN_BUTTON_MID_WIDTH, RUN_BUTTON_MID_HEIGHT)]
        self.run_minusElementInfo = [["Images/cucumber.png","Images/redMushroom.png"], [0, 0] , (RUN_BUTTON_MID_WIDTH, RUN_BUTTON_MID_HEIGHT)]

    ## 게임 요소 관리 : 파이게임 이미지 객체 생성
    def getImgs(self):
        self.imgs_intro_gameScreenInfo = pygame.transform.scale(pygame.image.load(self.intro_gameScreenInfo[0]), self.intro_gameScreenInfo[2])
        self.imgs_intro_chefInfo = pygame.transform.scale(pygame.image.load(self.intro_chefInfo[0]), self.intro_chefInfo[2])
        self.imgs_run_heart1 = pygame.transform.scale(pygame.image.load(self.run_lifeInfo[0][0]), self.run_lifeInfo[2])
        self.imgs_run_heart2 = pygame.transform.scale(pygame.image.load(self.run_lifeInfo[0][1]), self.run_lifeInfo[2])
        self.imgs_run_heart3 = pygame.transform.scale(pygame.image.load(self.run_lifeInfo[0][2]), self.run_lifeInfo[2])
        self.imgs_run_fire = pygame.transform.scale(pygame.image.load(self.run_fireInfo[0]), self.run_fireInfo[2])
        self.settings_userRanking = pygame.transform.scale(pygame.image.load(self.settings_userRankingInfo[0]), self.settings_userRankingInfo[2])
        self.imgs_run_band = pygame.transform.scale(pygame.image.load(self.run_bandInfo[0]), self.run_bandInfo[2])
        self.imgs_run_waitingScreenEasy = pygame.transform.scale(pygame.image.load(self.run_waitingScreenEasyInfo[0]), self.run_waitingScreenEasyInfo[2])
        self.imgs_run_waitingScreenNomal = pygame.transform.scale(pygame.image.load(self.run_waitingScreenNomalInfo[0]), self.run_waitingScreenNomalInfo[2])
        self.imgs_run_waitingScreenHard = pygame.transform.scale(pygame.image.load(self.run_waitingScreenHardInfo[0]), self.run_waitingScreenHardInfo[2])

    ## 게임 요소 관리 : 파이게임 버튼 객체 생성
    def buttons_generate(self):
        self.intro_gameStartButton = Button(self.intro_gameStartButtonInfo[0], self.intro_gameStartButtonInfo[1][0], self.intro_gameStartButtonInfo[1][1], self.intro_gameStartButtonInfo[2][0], self.intro_gameStartButtonInfo[2][1]) # 인트로 게임 시작 버튼 생성
        self.intro_gameSettingsButton = Button(self.intro_gameSettingsButtonInfo[0], self.intro_gameSettingsButtonInfo[1][0], self.intro_gameSettingsButtonInfo[1][1], self.intro_gameSettingsButtonInfo[2][0], self.intro_gameSettingsButtonInfo[2][1]) #인트로 게임 설정 버튼 생성
        self.intro_quitGameButton = Button(self.intro_quitGameButtonInfo[0], self.intro_quitGameButtonInfo[1][0], self.intro_quitGameButtonInfo[1][1], self.intro_quitGameButtonInfo[2][0], self.intro_quitGameButtonInfo[2][1] )

        self.run_menuButton = Button(self.run_menuButtonInfo[0], self.run_menuButtonInfo[1][0], self.run_menuButtonInfo[1][1], self.run_menuButtonInfo[2][0], self.run_menuButtonInfo[2][1] )
        self.run_menuToIntroButton = Button(self.run_menuToIntroButtonInfo[0], self.run_menuToIntroButtonInfo[1][0], self.run_menuToIntroButtonInfo[1][1], self.run_menuToIntroButtonInfo[2][0], self.run_menuToIntroButtonInfo[2][1] )
        self.run_menuCancelButton = Button(self.run_menuCancelButtonInfo[0], self.run_menuCancelButtonInfo[1][0], self.run_menuCancelButtonInfo[1][1], self.run_menuCancelButtonInfo[2][0], self.run_menuCancelButtonInfo[2][1] )
        self.run_restartGameButton = Button(self.run_restartGameButtonInfo[0], self.run_restartGameButtonInfo[1][0], self.run_restartGameButtonInfo[1][1], self.run_restartGameButtonInfo[2][0], self.run_restartGameButtonInfo[2][1] )
        self.run_yesButton = Button(self.run_yesButtonInfo[0], self.run_yesButtonInfo[1][0], self.run_yesButtonInfo[1][1], self.run_yesButtonInfo[2][0], self.run_yesButtonInfo[2][1] )
        self.run_noButton = Button(self.run_noButtonInfo[0], self.run_noButtonInfo[1][0], self.run_noButtonInfo[1][1], self.run_noButtonInfo[2][0], self.run_noButtonInfo[2][1] )

        self.settings_modeButton = Button(self.settings_modeButtonInfo[0], self.settings_modeButtonInfo[1][0], self.settings_modeButtonInfo[1][1], self.settings_modeButtonInfo[2][0], self.settings_modeButtonInfo[2][1]) #인트로 게임 설정 버튼 생성
        self.settings_userButton = Button(self.settings_userButtonInfo[0], self.settings_userButtonInfo[1][0], self.settings_userButtonInfo[1][1], self.settings_userButtonInfo[2][0], self.settings_userButtonInfo[2][1] )
       
        self.settings_modeEasyButton = Button(self.settings_modeEasyButtonInfo[0], self.settings_modeEasyButtonInfo[1][0], self.settings_modeEasyButtonInfo[1][1], self.settings_modeEasyButtonInfo[2][0], self.settings_modeEasyButtonInfo[2][1]) # 인트로 게임 시작 버튼 생성
        self.settings_modeNomalButton = Button(self.settings_modeNomalButtonInfo[0], self.settings_modeNomalButtonInfo[1][0], self.settings_modeNomalButtonInfo[1][1], self.settings_modeNomalButtonInfo[2][0], self.settings_modeNomalButtonInfo[2][1]) #인트로 게임 설정 버튼 생성
        self.settings_modeHardButton = Button(self.settings_modeHardButtonInfo[0], self.settings_modeHardButtonInfo[1][0], self.settings_modeHardButtonInfo[1][1], self.settings_modeHardButtonInfo[2][0], self.settings_modeHardButtonInfo[2][1] )
        self.settings_menuCancelButton = Button(self.run_menuCancelButtonInfo[0], self.run_menuCancelButtonInfo[1][0], self.run_menuCancelButtonInfo[1][1]+self.run_menuCancelButtonInfo[2][1], self.run_menuCancelButtonInfo[2][0], self.run_menuCancelButtonInfo[2][1] )

    
    ########## 게임 인트로 ##########
    ## 게임 인트로: 인트로 메인 화면
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
                        self.gameSettings()
                    elif self.intro_quitGameButton.pressed(event.pos) == True:
                        self.quitGame()


            ## 게임 스크린
            self.SCREEN.blit(self.imgs_intro_gameScreenInfo, self.intro_gameScreenInfo[1])
            self.SCREEN.blit(self.imgs_intro_chefInfo, self.intro_chefInfo[1])

            ## 인트로 멘트
            self.gameUserNameFont = pygame.font.SysFont( 'impact', 30+ changeColorAndSize[cntForTimeSlow%10]*2, False, False)
            if self.userHistory:
                self.gameUserNameText = self.gameUserNameFont.render(f"hi, {self.userName}", True, (changeColorAndSize[cntForTimeSlow%10]*10+60 ,0 ,changeColorAndSize[cntForTimeSlow%10]*20 ))
            else:
                self.gameUserNameText = self.gameUserNameFont.render(f"Welcome {self.userName}", True, (changeColorAndSize[cntForTimeSlow%10]*10+60 ,0 ,changeColorAndSize[cntForTimeSlow%10]*20 ))
            self.gameUserNameRect = self.gameUserNameText.get_rect()
            self.SCREEN.blit(self.gameUserNameText, [self.SCREEN_WIDTH/2 - self.gameUserNameRect.w/2, self.SCREEN_HEIGHT - self.gameUserNameRect.h])
            
            ## 유저의 최고 점수
            self.gameUserBestScoreFont = pygame.font.SysFont( 'impact', 20+changeColorAndSize[cntForTimeSlow%10], False, False)
            self.gameUserBestScoreText = self.gameUserBestScoreFont.render(f"YOUR BEST SCORE : {self.userBestScore}", True, BLACK)
            self.gameUserBestScoreRect = self.gameUserBestScoreText.get_rect()
            self.SCREEN.blit(self.gameUserBestScoreText, [self.SCREEN_WIDTH/2 - self.gameUserBestScoreRect.w/2, self.SCREEN_HEIGHT*0.01])
            
            ## 게임 버튼
            self.SCREEN.blit(self.intro_gameStartButton.button, self.intro_gameStartButtonInfo[1])
            self.SCREEN.blit(self.intro_gameSettingsButton.button, self.intro_gameSettingsButtonInfo[1])
            self.SCREEN.blit(self.intro_quitGameButton.button, self.intro_quitGameButtonInfo[1])
            
            pygame.display.update()
            self.clock.tick(15)

    ########## 게임 실행 ##########
    ## 게임 실행: 먹은 음식 검출
    def isInYourMouth(self, isPlusElement, points, element): # points: x*1.1, y*1.25
        if isPlusElement:
            if ((points[55][1]*1.25 - points[50][1]*1.25) > 50 and points[58][0]*1.1>(element.rect.x + element.rect.w/2)>points[62][0]*1.1) and (points[50][1]*1.25<(element.rect.y+ element.rect.h/2)<points[55][1]*1.25): 
                return True
        else:
            if ((points[55][1]*1.25 - points[50][1]*1.25) > 50 and points[58][0]*1.1>(element.rect.x + element.rect.w/2)>points[62][0]*1.1) and (points[50][1]*1.25<(element.rect.y+ element.rect.h/2)<points[55][1]*1.25): 
                return True
        return False
    
    ## 게임 실행: 거부한 음식 검출
    def rejectOnYourMouth(self, points, element):
        if (points[55][1]*1.25 - points[50][1]*1.25 < 35) and (points[58][0]*1.1>element.rect.x + element.rect.w/2>points[62][0]*1.1) and ( (element.rect.y)<points[50][1]*1.25<(element.rect.y + element.rect.h)):
                return True
        return False

    ## 게임 실행: 게임 종료
    def gameFinish(self, TYPE):
        STOP = True
        while STOP:
            pygame.draw.rect(self.SCREEN, BLACK, [0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
            if TYPE == "GAMEOVER":
                self.textHelpper("GAME OVER", 40, WHITE, self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.1)
            elif TYPE == "TIMEOVER":
                self.textHelpper("TIME OVER", 40, WHITE, self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.1)
             
            self.SCREEN.blit(self.run_menuToIntroButton.button, self.run_menuToIntroButtonInfo[1])
            self.SCREEN.blit(self.run_restartGameButton.button, self.run_restartGameButtonInfo[1])

            ## 점수 객체 화면 출력
            self.gameScoreFont = pygame.font.SysFont( 'impact', 40, False, False)
            self.gameScoreText = self.gameScoreFont.render(f"SCORE : {self.score.score}", True, RED)
            self.gameScoreTextRect = self.gameScoreText.get_rect()
            self.SCREEN.blit(self.gameScoreText, [0, self.SCREEN_HEIGHT - self.gameScoreTextRect.h])
                
            if int(self.userBestScore) < self.score.score: self.userBestScore = str(self.score.score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.run_menuToIntroButton.pressed(event.pos) == True:
                        self.run_menuToIntroButton.switchImg("Images/run_menuToIntroButton_pressed.png")
                    elif self.run_restartGameButton.pressed(event.pos) == True:
                        self.run_restartGameButton.switchImg("Images/run_restartGameButton_pressed.png")

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.run_menuToIntroButton.switchImg("Images/run_menuToIntroButton.png")
                    self.run_restartGameButton.switchImg("Images/run_restartGameButton.png")

                    if self.run_menuToIntroButton.pressed(event.pos) == True:
                        STOP = False
                        self.gameFactorClear()
                        self.introScreen()

                    elif self.run_menuCancelButton.pressed(event.pos) == True:
                        STOP = False
                        self.gameFactorClear()
                        self.gameStart()
                        
            pygame.display.update()

    ## 게임 실행: 게임 요소 정리
    def gameFactorClear(self):
        STOP = False
        PlusElement.DOUBLE_MODE = False
        MinusElement.Minus_MODE = False
        self.floatElements = [[], []]
        self.life.life = 3
        self.score.score = 0
    
    ## 게임 실행: 부유물 객체 생성
    def floatterGenerotr(self):
        if self.gameMode == "easy":
            ## 부유물 객체의 생성 [plus : minus = 8 : 2]
            if ((time.time() - self.startTime)%1 <0.06): # 1초에 2번 부유물 객체 생성
                plusOrMinus = random.randrange(100)
                if plusOrMinus < 70: # 2:8 = (minus:plus) 의 비율로 부유물 객체 생성 
                    self.floatElements[0].append(PlusElement(self.run_plusElementInfo[0][random.randrange(0, 3)], self.run_plusElementInfo[2][0], self.run_plusElementInfo[2][1]))
                elif 70<= plusOrMinus  <80:
                    self.floatElements[1].append(MinusElement(self.run_minusElementInfo[0][random.randrange(0, 1)], self.run_minusElementInfo[2][0], self.run_minusElementInfo[2][1]))
                elif 80<=plusOrMinus<85:
                    self.floatElements[0].append(PlusElement(self.run_plusElementInfo[0][3], self.run_plusElementInfo[2][0], self.run_plusElementInfo[2][1]))
                elif 85<=plusOrMinus<90:
                     self.floatElements[1].append(MinusElement(self.run_minusElementInfo[0][1], self.run_minusElementInfo[2][0], self.run_minusElementInfo[2][1]))
                elif 90<=plusOrMinus<95:
                    self.floatElements[0].append(PlusElement(self.run_plusElementInfo[0][4], self.run_plusElementInfo[2][0], self.run_plusElementInfo[2][1]))
        
        elif self.gameMode == "nomal":
            ## 부유물 객체의 생성 [plus : minus = 8 : 2]
            if ((time.time() - self.startTime)%1 <0.1): # 1초에 2번 부유물 객체 생성
                plusOrMinus = random.randrange(100)
                if plusOrMinus < 70: # 2:8 = (minus:plus) 의 비율로 부유물 객체 생성 
                    self.floatElements[0].append(PlusElement(self.run_plusElementInfo[0][random.randrange(0, 3)], self.run_plusElementInfo[2][0], self.run_plusElementInfo[2][1]))
                elif 70<= plusOrMinus  <80:
                    self.floatElements[1].append(MinusElement(self.run_minusElementInfo[0][random.randrange(0, 1)], self.run_minusElementInfo[2][0], self.run_minusElementInfo[2][1]))
                elif 80<=plusOrMinus<85:
                    self.floatElements[0].append(PlusElement(self.run_plusElementInfo[0][3], self.run_plusElementInfo[2][0], self.run_plusElementInfo[2][1]))
                elif 85<=plusOrMinus<90:
                     self.floatElements[1].append(MinusElement(self.run_minusElementInfo[0][1], self.run_minusElementInfo[2][0], self.run_minusElementInfo[2][1]))
                elif 90<=plusOrMinus<95:
                    self.floatElements[0].append(PlusElement(self.run_plusElementInfo[0][4], self.run_plusElementInfo[2][0], self.run_plusElementInfo[2][1]))
        
        elif self.gameMode == "hard":
            ## 부유물 객체의 생성 [plus : minus = 8 : 2]
            if ((time.time() - self.startTime)%1 <0.16): # 1초에 2번 부유물 객체 생성
                plusOrMinus = random.randrange(100)
                if plusOrMinus < 70: # 2:8 = (minus:plus) 의 비율로 부유물 객체 생성 
                    self.floatElements[0].append(PlusElement(self.run_plusElementInfo[0][random.randrange(0, 3)], self.run_plusElementInfo[2][0], self.run_plusElementInfo[2][1]))
                elif 70<= plusOrMinus  <80:
                    self.floatElements[1].append(MinusElement(self.run_minusElementInfo[0][random.randrange(0, 1)], self.run_minusElementInfo[2][0], self.run_minusElementInfo[2][1]))
                elif 80<=plusOrMinus<85:
                    self.floatElements[0].append(PlusElement(self.run_plusElementInfo[0][3], self.run_plusElementInfo[2][0], self.run_plusElementInfo[2][1]))
                elif 85<=plusOrMinus<90:
                     self.floatElements[1].append(MinusElement(self.run_minusElementInfo[0][1], self.run_minusElementInfo[2][0], self.run_minusElementInfo[2][1]))
                elif 90<=plusOrMinus<95:
                    self.floatElements[0].append(PlusElement(self.run_plusElementInfo[0][4], self.run_plusElementInfo[2][0], self.run_plusElementInfo[2][1]))
    
    ## 게임 실행: 식사, 시간, 이벤트 체크
    def eatChecker(self):
        ## 먹은지 안 먹은지 주기적으로 검출
        for element in self.floatElements[0]:
            if (self.isInYourMouth(True , self.points, element)):
                if element.eat():
                    self.startPeverTime = time.time()
                    
                self.floatElements[0].remove(element)
        
        for element in self.floatElements[1]:
            if (self.isInYourMouth(False , self.points, element)):
                element.eat()
                if self.life.life <= 0: self.gameFinish("GAMEOVER") 
                self.floatElements[1].remove(element)
            if self.rejectOnYourMouth(self.points, element):
                self.floatElements[1].remove(element)

    def timeChecker(self): 
        ## 시간 체크
        # 타임오버
        self.presentTime = (time.time() - self.startTime)//1 # 현재 시간 측정
        if (self.presentTime > self.gameTime):
            self.gameFinish("TIMEOVER")
        else:
            self.timmerText = self.timmerFont.render(f"{self.gameTime-int(self.presentTime)}", True, BLACK)
            self.timmerTextRect = self.timmerText.get_rect()
        # 피버타임 시간 체크
        if time.time() - self.startPeverTime > 10:
            PlusElement.DOUBLE_MODE = False

    def run_eventChecker(self):
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
                                    self.gameFactorClear()
                                    self.introScreen()

                                elif self.run_menuCancelButton.pressed(event.pos) == True:
                                    STOP = False
                                    self.startTime -= (time.time() - pauseTime) # 정지한 시간만큼 현재 시간 보정
                                    
                        pygame.display.update()

    ## 게임 실행: 게임 시작 (메인화면)
    def gameStart(self):
        STOP = True
        self.startPeverTime = 0
        self.finishPeverTime = 0
        for points in fc.run(visualize=1, max_threads=4, capture=0):
            self.points = points
            while STOP:
                if self.gameMode == "easy": self.SCREEN.blit(self.imgs_run_waitingScreenEasy, self.run_waitingScreenEasyInfo[1])
                elif self.gameMode == "nomal": self.SCREEN.blit(self.imgs_run_waitingScreenNomal, self.run_waitingScreenNomalInfo[1])
                elif self.gameMode == "hard": self.SCREEN.blit(self.imgs_run_waitingScreenHard, self.run_waitingScreenHardInfo[1])

                self.gamePauseFont = pygame.font.SysFont( 'impact', 40, False, False)
                self.gamePauseText = self.gamePauseFont.render("Press \"SpaceBar\" to Start Game ", True, WHITE)
                self.gamePauseTextRect = self.gamePauseText.get_rect() 
                self.SCREEN.blit(self.gamePauseText, [self.SCREEN_WIDTH/2 - self.gamePauseTextRect.w/2, self.SCREEN_HEIGHT - self.gamePauseTextRect.h])
                
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.startTime = time.time()
                            STOP = False 

            self.run_eventChecker()
            self.floatterGenerotr()
            self.eatChecker()
            self.timeChecker()
        
            
            ## 부유물 30개 넘으면 Game Over
            if (len(self.floatElements[0]) + len(self.floatElements[1]) > 30 ): self.gameFinish("GAMEOVER")

            ## 게임중 추가 요소는 배경 생성 후 추가해줄 것
            self.gameBoard()
            self.SCREEN.blit(self.img, [0, 0]) # 배경
            self.SCREEN.blit(self.timmerText, [self.SCREEN_WIDTH/2 - self.timmerTextRect.w/2, 0])
            self.SCREEN.blit(self.run_menuButton.button, self.run_menuButtonInfo[1])
            ### 피버타임
            if PlusElement.DOUBLE_MODE:
                game.SCREEN.blit(self.imgs_run_fire, [points[67][0], points[67][1]*1.1])
                game.SCREEN.blit(self.imgs_run_fire, [points[66][0], points[66][1]*1.1])
            if MinusElement.Minus_MODE:
                game.SCREEN.blit(self.imgs_run_band, [points[67][0], points[67][1]*1.1])
                game.SCREEN.blit(self.imgs_run_band, [points[66][0], points[66][1]*1.1])
            
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

    ## 게임 실행: 게임 프로그램 실행
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
        
        # 게임 실행 첫 화면은 인트로로 실행
        self.introScreen()
        

    ########## 게임 프로그램 종료 ##########
    ## 게임 프로그램 종료 : 저장 및 종료
    def quitGame(self):
        STOP = True
        while STOP:
            pygame.draw.rect(self.SCREEN, BLACK, [0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
            self.textHelpper("SAVE OR NOT?", 40, WHITE, self.SCREEN_WIDTH/2, self.SCREEN_WIDTH*0.1)
            self.textHelpper(f"Your Best Score : {self.userBestScore}", 20, WHITE, self.SCREEN_WIDTH/2, self.SCREEN_WIDTH*0.2)
            self.SCREEN.blit(self.run_noButton.button, self.run_noButtonInfo[1])
            self.SCREEN.blit(self.run_yesButton.button, self.run_yesButtonInfo[1])
            ## 점수 객체 화면 출력
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.run_yesButton.pressed(event.pos) == True:
                        self.run_yesButton.switchImg("Images/run_yesButton_pressed.png")
                    elif self.run_noButton.pressed(event.pos) == True:
                        self.run_noButton.switchImg("Images/run_noButton_pressed.png")

                elif event.type == pygame.MOUSEBUTTONUP:
                    pauseTime = time.time()
                    self.run_yesButton.switchImg("Images/run_yesButton.png")
                    self.run_noButton.switchImg("Images/run_noButton.png")

                    if self.run_yesButton.pressed(event.pos) == True:
                        ## user 관리 파일에 유저의 최고점수를 저장한다.
                        print(self.userHistory)
                        if self.userHistory:
                            file = open("User/userInfo.txt", "r", encoding="UTF-8")
                            edit_file = []
                            
                            for user in file:
                                user = user.split()
                                if self.userName != user[0]:
                                    edit_file.append(f"{user[0]} {user[1]}\n")
                                
                            file = open("User/userInfo.txt", "w", encoding="UTF-8")
                            file.write(f"{self.userName} {self.userBestScore}\n")
                            file = open("User/userInfo.txt", "a", encoding="UTF-8")
                            for userInfo in edit_file:
                                file.write(userInfo)
                            STOP = False

                        else :
                            STOP = False
                            file = open("User/userInfo.txt", "a", encoding="UTF-8")
                            file.write(f"{self.userName} {self.userBestScore}\n")
                            STOP = False

                    elif self.run_noButton.pressed(event.pos) == True:
                        STOP = False
            pygame.display.update()
        
        pygame.quit()
        sys.exit()
    
  
if __name__ == "__main__":
    # generte the game
    print("Welcome to our game !!")
    game = Game()
    game.run()
