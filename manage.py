import pygame
from pygame.locals import *
from Dino import Dino
from Obstacle import ObstacleCourse, Obstacle
from Earth import Earth

FPS = 60
GRAVITY = 0.4
JUMP_POWER = 10
up = False
squat = False
speed = 4
start = False
score = 0

pygame.init()
pygame.display.set_caption('Dino 2D')
clock = pygame.time.Clock()
size = (854, 480)
width, height = size
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()

obstacle_course = ObstacleCourse()
obstacle_course.create()
obstacle_course.drawing(all_sprites)
dino = Dino()

earth = pygame.sprite.Group()

for i in range(0, 6):
    x = (i+1)*100 + i*100
    y = 380
    land = Earth((x, y))
    earth.add(land)


sky = pygame.image.load('image/sky.png')

rec = open('rec.txt', 'r')
recd = int(rec.read())
rec.close()
a = recd

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == K_UP and start:
                up = True
            if event.key == K_DOWN and start:
                squat = True
            if event.key == K_RETURN and not start:
                all_sprites.empty()
                obstacle_course.restart()
                obstacle_course.drawing(all_sprites)
                dino = Dino()
                speed = 4
                score = 0
                up = False
                squat = False
                start = True
                
        elif event.type == pygame.KEYUP:
            if event.key == K_UP and start:
                up = False
            if event.key == K_DOWN and start:
                squat = False
    if start:
        speed += 0.001
        score += 0.05 * int(speed)
        earth.update(int(speed))
        all_sprites.update(int(speed))
        dino.update(up, GRAVITY, JUMP_POWER, squat)
        hits = pygame.sprite.spritecollide(dino, all_sprites, False)
        if hits:
            start = False
    elif not start:
        font = pygame.font.Font(None, 72)
        text = font.render("press enter to start", 1, (0, 0, 0))
        place = text.get_rect(center=(427, 140))
        screen.blit(text, place)

    
    if recd <= int(score):
        recd = int(score)

    pygame.display.update()
    
    
    screen.blit(sky, (0, 0))


    all_sprites.draw(screen)
    earth.draw(screen)
    dino.draw(screen)
    
    font_score = pygame.font.Font(None, 36)
    text_score = font_score.render('Счёт: ' + str(int(score)), 1, (0, 0, 0))
    place_score = text_score.get_rect(center=(750, 30))
    text_rec = font_score.render('Рекорд: ' + str(recd), 1, (0, 0, 0))
    place_rec = text_rec.get_rect(center=(100, 30))
    screen.blit(text_score, place_score)
    screen.blit(text_rec, place_rec)
    clock.tick(FPS)



if a < recd:
    rec = open('rec.txt', 'w')
    rec.write(str(recd))
    rec.close()

pygame.quit()