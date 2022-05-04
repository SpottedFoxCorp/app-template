import pygame, sys
from pygame.locals import *

main_clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('App')
screen = pygame.display.set_mode((500, 500), 0, 25)
title_font = pygame.font.SysFont(None, 35)
font = pygame.font.SysFont(None, 20)
pygame.mixer.music.load('click_low.wav')
click_sound = pygame.mixer.Sound('click_low.wav')
click_sound.set_volume(0.075)

click = False

def draw_text(text, font, color, surface, x, y):
    text_render = font.render(text, 1, color)
    text_rect = text_render.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_render, text_rect)

def main_menu():
    while True:
        screen.fill((0, 0, 0))
        draw_text('Main Menu', title_font, (255, 255, 255), screen, 175, 25)
        
        mx, my = pygame.mouse.get_pos()


        click = False
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    click_sound.play()   
        
        pygame.display.update()
        main_clock.tick(60)


main_menu()