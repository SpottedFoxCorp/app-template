import pygame, sys
from pygame.locals import *
from settings import *


main_clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('App')
screen = pygame.display.set_mode((500, 500), 0, 25)
title_font = pygame.font.SysFont(None, 35)
font = pygame.font.SysFont(None, 20)
click_sound = pygame.mixer.Sound('click_low.wav')
click_sound.set_volume(0.075)
bg_img = pygame.image.load('background.png').convert_alpha()
button_highlighted = pygame.image.load('button_highlighted.png').convert_alpha()
button_unclicked = pygame.image.load('button_unclicked.png').convert_alpha()
button_clicked = pygame.image.load('button_clicked.png').convert_alpha()
text_box = pygame.image.load('text_box.png').convert_alpha()

click = False

def draw_text(text, font, color, surface, x, y):
    text_render = font.render(text, 1, color)
    text_rect = text_render.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_render, text_rect)

def main_menu():
    while True:
        screen.fill(BLACK)
        screen.blit(bg_img, (0,0))
        draw_text('Your App', title_font, WHITE, screen, 175, 25)
        
        mx, my = pygame.mouse.get_pos()
        
        button1_rect = button_unclicked.get_rect()
        button1_rect.topleft = (100, 400)
        button2_rect = button_unclicked.get_rect()
        button2_rect.topleft = (300, 400)
        text_rect = text_box.get_rect()
        text_rect.topleft = (100, 200)

        if button1_rect.collidepoint((mx, my)):
            if click:
                click_sound.play()   
                screen.blit(button_clicked, button1_rect)
            else:
                screen.blit(button_highlighted, button1_rect)
        else:
            screen.blit(button_unclicked, button1_rect)

        if button2_rect.collidepoint((mx, my)):
            if click:
                click_sound.play()
                screen.blit(button_clicked, button2_rect)
            else:
                screen.blit(button_highlighted, button2_rect)
        else:
            screen.blit(button_unclicked, button2_rect)
        
        screen.blit(text_box, text_rect)
        draw_text('Text Input:', font, WHITE, screen, 100, 180)
        draw_text('Data goes here and other information goes here as well', font, WHITE, screen, 75, 75)
        draw_text('Continue', font, WHITE, screen, 110, 415)
        draw_text('Options', font, WHITE, screen, 315, 415)
        
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
        
        pygame.display.update()
        main_clock.tick(60)


main_menu()