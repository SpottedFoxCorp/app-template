import pygame, sys
from pygame.locals import *

main_clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('App')
screen = pygame.display.set_mode((500, 500), 0, 25)
title_font = pygame.font.SysFont(None, 35)
font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    text_render = font.render(text, 1, color)
    text_rect = text_render.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_render, text_rect)

def main_menu():
    while True:
        screen.fill((0, 0, 0))
        draw_text('Main Menu', title_font, (255, 255, 255), screen, 175, 25)
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
        main_clock.tick(60)


main_menu()