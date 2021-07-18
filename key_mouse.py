import pygame
from pygame.locals import *
from sys import exit

PLOTTER = False

pygame.init()
width=425
height=550
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
pygame.key.set_repeat(600,600)

color_screen=(49,150,100)
color_line=(255,0,0)

screen.fill(color_screen)
pygame.display.flip()
pygame.mouse.set_visible(True)
 
#pygame.display.iconify() 

def draw_picture(img):
    trace = []
    
    x_old = 0
    y_old = 0
    paused = True

    if img is not None:
        screen.blit(img, (0,0))
        
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
                
        keys  = pygame.key.get_pressed()

        if event.type == pygame.MOUSEBUTTONUP:
            x_old, y_old = pygame.mouse.get_pos()
            trace = []
            if img is not None:
                screen.blit(img, (0,0))
            else:
                screen.fill(color_screen)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                paused = False
            if event.key == pygame.K_q:
                break

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                paused = True

        if not paused:
            x, y = pygame.mouse.get_pos()
            #print (x, y)
            if abs(x - x_old) > 1 or abs(y - y_old) > 1:
                pygame.draw.line(screen, color_line,(x_old,y_old),(x,y), 2)
                trace.append((x_old, y_old))
                x_old = x
                y_old = y

        pygame.display.update()
        
    return trace


import os
if __name__ == '__main__':
    print("Click Mouse At Current Plotter Location.")
    print("Hold down 'A' key an trace the picture.")
    print("Press Q to send trace to plotter.")
    
    image_file = input("Enter image file: ")
    image_file = image_file.strip()
    if os.path.isfile(image_file):
        img = pygame.image.load(image_file)
        img = pygame.transform.scale(img, (width, height))
    else:
        img = None
          

    trace = draw_picture(img)
    print(trace)
