import pygame
class Earth(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/earth.gif')
        self.rect = self.image.get_rect()
        self.rect.center = center
    def update(self, a):
        self.rect.x -= a
        if self.rect.right < 0:
            self.rect.left = 900 - a