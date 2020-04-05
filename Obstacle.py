import pygame
import random

RED = (255, 0, 0)
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, center, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        a = self.image.get_rect()
        a[0] -= 7
        a[2] -= 7
        self.rect = a
        self.rect.center = center
    def update(self, a):
        self.rect.x -= a
        if self.rect.right < 0:
            self.rect.left = 50 * 500

class ObstacleCourse(object):
    def __init__(self):
        self.list_of_obstacles = []
        self.number_of_obstacles = 50

    def create(self):
        for i in range(self.number_of_obstacles):
            self.list_of_obstacles.append(0)

    def restart(self):
        for i in range(self.number_of_obstacles):
            a = random.randint(0, 5)
            self.list_of_obstacles[i] = a

    def drawing(self, all_sprites):
        for i in range(self.number_of_obstacles):
            y = 280
            image = 0
            height = 0
            width = 0
            if self.list_of_obstacles[i] == 0:
                y -= 50
                image = pygame.image.load('image/cactus_1.gif')
            elif self.list_of_obstacles[i] == 1:
                y -= 40
                image = pygame.image.load('image/cactus_2.gif')
            elif self.list_of_obstacles[i] == 2:
                y -= 30
                image = pygame.image.load('image/cactus_3.gif')
            elif self.list_of_obstacles[i] == 3:
                y -= 25
                image = pygame.image.load('image/bird.gif')
            elif self.list_of_obstacles[i] == 4:
                y -= 70
                image = pygame.image.load('image/bird.gif')
            elif self.list_of_obstacles[i] == 5:
                y -= 125
                image = pygame.image.load('image/bird.gif')
            x = 1280 + i * 500
            center = (x, y)
            obstacle = Obstacle(center, image)
            all_sprites.add(obstacle)
            

