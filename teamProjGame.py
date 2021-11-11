import numpy as np
import dlib, cv2 # cv2 : webcam 
from imutils import face_utils
import pygame

import os, sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PRESENT_FRAME_WRITE_PATH = "Jiung/jiung.jpg"




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


    def run(self):
        # pygame initialize
        pygame.init()

        SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Yam-Yam")


        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        keyPointModel = ('models/2018_12_17_22_58_35.h5')

        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: break
            img = frame.copy()
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector(gray_img, 1)
            for face in faces:
                shapes = predictor(gray_img, face)
                shapes = face_utils.shape_to_np(shapes)
                for point in shapes:
                    cv2.circle(img, point, 2, (255, 255, 255))

            cv2.imwrite(PRESENT_FRAME_WRITE_PATH, img)
            img = pygame.image.load(PRESENT_FRAME_WRITE_PATH)
            eagle_img = pygame.transform.scale(pygame.image.load("eagle.jpg"), (300,300))

            SCREEN.blit(img, [0, 0])
            SCREEN.blit(eagle_img, [100,100])
            
            pygame.display.update()
            
            

            



if __name__ == "__main__":
    # generte the game
    print("Welcome to our game !!")
    game = Game()
    game.run()
