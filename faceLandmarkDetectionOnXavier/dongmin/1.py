# 튕

import pygame
from random import randint
BLACK = (0, 0, 0)
 
class Ball(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
        
        
                ## 탁구공 범위 확인 
        ## 1) 진행 방향을 바꾸는 행위
        ## 2) 게임이 종료되는 행위
        if circle_x < bar_width: ## bar에 닿았을 때
            if circle_y >= bar_y - circle_radius and circle_y <= bar_y + bar_height + circle_radius:
                circle_x = bar_width
                speed_x = -speed_x
        if circle_x < -circle_radius: ## bar에 닿지 않고 좌측 벽면에 닿았을 때, 게임 종료 및 초기화
            circle_x, circle_y = circle_start_x, circle_start_y
            bar_x, bar_y = bar_start_x, bar_start_y
        elif circle_x > screen_width - circle_diameter: ## 우측 벽면에 닿았을 때
            speed_x = -speed_x
        if circle_y <= 0: ## 위측 벽면에 닿았을때
            speed_y = -speed_y
            circle_y = 0
        elif circle_y >= screen_height - circle_diameter: ## 아래 벽면에 닿았을때
            speed_y = -speed_y
            circle_y = screen_height - circle_diameter
