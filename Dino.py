import pygame
GREEN = (0, 255, 0)

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = [pygame.image.load('image/dino_1.gif'),
            pygame.image.load('image/dino_1.1.gif'),
            pygame.image.load('image/dino_1.2.gif'),
            pygame.image.load('image/dino_1.3.gif'),
            pygame.image.load('image/dino_1.4.gif'),
            pygame.image.load('image/dino_1.5.gif'),
            pygame.image.load('image/dino_1.gif'),
            pygame.image.load('image/dino_1.6.gif'),
            pygame.image.load('image/dino_1.7.gif'),
            pygame.image.load('image/dino_1.8.gif'),
            pygame.image.load('image/dino_1.9.gif'),
            pygame.image.load('image/dino_1.10.gif')]
        self.image2 = [pygame.image.load('image/dino_2.gif'),
            pygame.image.load('image/dino_2.1.gif'),
            pygame.image.load('image/dino_2.2.gif'),
            pygame.image.load('image/dino_2.3.gif'),
            pygame.image.load('image/dino_2.4.gif'),
            pygame.image.load('image/dino_2.5.gif'),
            pygame.image.load('image/dino_2.gif'),
            pygame.image.load('image/dino_2.6.gif'),
            pygame.image.load('image/dino_2.7.gif'),
            pygame.image.load('image/dino_2.8.gif'),
            pygame.image.load('image/dino_2.9.gif'),
            pygame.image.load('image/dino_2.10.gif')]
        self.AnimCount = 0
        self.image = self.image1[self.AnimCount]
        a = self.image.get_rect()
        a[0] -=30
        a[1] -=20
        a[2] -=30
        self.rect = a
        self.rect.center = (280, 242)
        self.yvel = 0
        self.onGround = False

    def update(self, up, GRAVITY, JUMP_POWER, squat):
        if self.rect.bottom < 280:
            self.onGround = False
        else:
            self.onGround = True
            self.rect.bottom = 280
            self.yvel = 0
        if up:
            if self.onGround and not squat:
                self.yvel = -JUMP_POWER
        if not self.onGround:
            self.yvel +=  GRAVITY
        self.rect.y += self.yvel
        if squat and self.onGround:
            self.image = self.image2[self.AnimCount]
            self.AnimCount +=1
            if self.AnimCount > 10:
                self.AnimCount = 0
            self.rect.y += 32
        elif not squat and self.onGround:
            self.image = self.image1[self.AnimCount]
            self.AnimCount +=1
            if self.AnimCount > 10:
                self.AnimCount = 0
        else:
            self.image = self.image1[0]
        
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))
