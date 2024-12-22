import pygame
from random import randrange
import time

#Initalize Pygame
pygame.init()
pygame.font.init
size = width, height = 600, 600
title = "Dodge the alien!"
image = "player.png"
image2 = "enemy.png"
bg = 36, 36, 36
speed = [200,200]

#Create Window with custom title
window = pygame.display.set_mode(size)
pygame.display.set_caption(title)

icon = pygame.image.load(image)
iconr = icon.get_rect()
iconr = iconr.move(speed)
window.blit(icon, iconr)

speed2 = [100, 100]
icon2 = pygame.image.load(image2)
iconr2 = icon2.get_rect()
iconr2 = iconr2.move(speed2)
window.blit(icon2, iconr2)
speed = [0, 0]
speed2 = [0, 0]
score = 0
highScore = 0

exitLoop = False
while exitLoop != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False;

        if event.type == pygame.KEYDOWN:
            if event.key == 1073741903: #RIGHT
                exitLoop = True

    time.sleep(0.4)
                
while True:

    #Change direction if it reaches the borders
    if iconr.left<5 or iconr.right>width:
        speed[0] = 0
    if iconr.top <5 or iconr.bottom>height:
        speed[1] = 0

    posdiffx = iconr.left - iconr2.left
    posdiffy = iconr.top - iconr2.top
   

    if posdiffx > 0:       
        speed2[0] = 2
    else:
        speed2[0] = -2
        
    if posdiffy > 0: 
        speed2[1] = 2
    else:
        speed2[1] = -2
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False;

        if event.type == pygame.KEYDOWN:
            if event.key == 1073741903: #RIGHT
                speed[0] = 3
            if event.key == 1073741904: #LEFT
                speed[0] = -3
            if event.key == 1073741906: #UP
                speed[1] = -3
            if event.key == 1073741905: #DOWN
                speed[1] = 3
                        
    #Move the icon
    iconr = iconr.move(speed)
    
    if iconr2.left<10:
        iconr2.right += 10
    if iconr2.right>width-10:
        iconr2.right -= 10
        
    if iconr2.top <10:
        iconr2.top += 10
    if iconr2.bottom>height-10:
        iconr2.bottom -= 10
  
    gameOver = (abs(iconr.centerx - iconr2.centerx) <= 35) and (abs(iconr.centery - iconr2.centery) <= 35)
    
    if gameOver:
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        # now end game
        text_surface = font.render("Game Over!", False, "yellow", bg)
        window.blit(text_surface, dest=(200,300))
        text_surface = font.render("Score: "+str(score), False, "white", bg)
        window.blit(text_surface, dest=(150,350))
        text_surface = font.render("High Score: "+str(highScore), False, "white", bg)
        window.blit(text_surface, dest=(150,400))
        pygame.display.flip()
        time.sleep(2)
        iconr.right = 200
        iconr.top = 200
        iconr2.right = 100
        iconr2.top = 100
        score = 0
    else:
        score += 1
        if score > highScore:
            highScore = score
        
    iconr2 = iconr2.move(speed2) 
    window.fill(bg)
    window.blit(icon, iconr)
    window.blit(icon2, iconr2)
    pygame.display.flip()  
