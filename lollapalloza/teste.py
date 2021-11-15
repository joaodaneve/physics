import pygame
from pygame.locals import *
from sys import exit

largura = 1120
altura = 656

pygame.init()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("TÊNIS DE MESA")

raquete1 = pygame.image.load('imagens/raquete1.png').convert_alpha()
x_rqt1 = 0
y_rqt1 = 320

tela.blit(raquete1, (x_rqt1, y_rqt1))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    pygame.display.flip()