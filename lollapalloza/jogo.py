import pygame
from pygame.locals import *
from sys import exit
from sorteio import sortearSaque
from raquete import *
from bola import *

#TABELA DE CORES
preto = (1,1,1)
cinza = (28,28,28)
verde = (0,100,0)
vermelho = (255,0,0)
mesa = (25,25,112)
branco = borda = rede = (211,211,211)
bolinha = (255,165,0)
plano_de_fundo = (107,142,35)

#PONTUAÇÃO
pts_jogador1 = 0
pts_jogador2 = 0

saque = True

#DEFININDO AS DIMENSÕES DA JANELA
largura = 1120
altura = 656

pygame.init()

#DEFINININDO A FONTE USADA PARA EXIBIR O PLACAR
fonteNumero = pygame.font.SysFont('verdana', 25, True)
fonteTexto = pygame.font.SysFont('verdana', 18, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("TÊNIS DE MESA")
relogio = pygame.time.Clock()
FPS = 45

imagem_seta = pygame.image.load('imagens/setaDaVez.png').convert_alpha()
imagem_seta = pygame.transform.scale(imagem_seta, (32, 32))
posicao_seta = sortearSaque()

bola1 = pygame.image.load('imagens/bolinha.png').convert_alpha()
x_bola = posicionarSaque(posicao_seta)[0]
y_bola = posicionarSaque(posicao_seta)[1]

raquete1 = pygame.image.load('imagens/raquete1.png').convert_alpha()
x_rqt1 = 25
y_rqt1 = 330

raquete2 = pygame.image.load('imagens/raquete2.png').convert_alpha()
x_rqt2 = 1030
y_rqt2 = 330

#CRIAÇÃO DE MÁSCARAS PARA VERIFICAR COLISÕES ENTRE AS IMAGENS
mascara_bola = pygame.mask.from_surface(bola1)
mascara_rqt1 = pygame.mask.from_surface(raquete1)
mascara_rqt2 = pygame.mask.from_surface(raquete2)

while True:
    relogio.tick(FPS)
    
    pontuacao1 = ("%d" %(pts_jogador1))
    pontuacao2 = ("%d" %(pts_jogador2))

    jogador1_formatado = fonteTexto.render("Jogador A", True, branco)
    jogador2_formatado = fonteTexto.render("Jogador B", True, branco)
    p1_formatado = fonteNumero.render(pontuacao1, True, preto)
    p2_formatado = fonteNumero.render(pontuacao2, True, preto)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    #desenhando a região do plano de fundo, placar e mesa
    tela.fill(plano_de_fundo)
    pygame.draw.rect(tela, verde, (0, 0, largura, 120))
    pygame.draw.rect(tela, cinza, (940, 15, 160, 70))
    pygame.draw.line(tela, branco, (940, 50), (1065, 50), 1)
    pygame.draw.rect(tela, branco, (1065, 15, 50, 35))
    pygame.draw.rect(tela, branco, (1065, 50, 50, 35))
    pygame.draw.line(tela, cinza, (1065, 50), (1115, 50), 1)
    pygame.draw.rect(tela, mesa, (100, 120, 920, 500))
    
    #desenhando as bordas esquerda e direita da mesa
    pygame.draw.line(tela, borda, (104, 120), (104, 619), 10)
    pygame.draw.line(tela, borda, (1014, 120), (1014, 619), 10)
    
    #desenhando as bordas superior e inferior
    pygame.draw.line(tela, borda, (100, 124), (1019, 124), 10)
    pygame.draw.line(tela, borda, (100, 614), (1019, 614), 10)
    
    #desenhando a rede e linha divisória da mesa
    pygame.draw.line(tela, rede, (559, 124), (559, 614), 10)
    pygame.draw.aaline(tela, rede, (100, 370), (1019,370))

    #exibindo a pontuação na tela
    tela.blit(jogador1_formatado, (950, 19))
    tela.blit(jogador2_formatado, (950, 55))
    tela.blit(p1_formatado, (1073, 17))
    tela.blit(p2_formatado, (1073, 53))
    tela.blit(imagem_seta, posicao_seta)


    sobreposicao1 = (x_bola - x_rqt1, y_bola - y_rqt1)
    sobreposicao2 = (x_bola - x_rqt2, y_bola - y_rqt2)

    colisao1 = mascara_rqt1.overlap(mascara_bola, sobreposicao1)
    colisao2 = mascara_rqt2.overlap(mascara_bola, sobreposicao2)

    tecla = pygame.key.get_pressed()

    if saque == True and not colisao1 and not colisao2:
        if tecla[K_t]:
            y_bola = B_praCima(y_bola, 130)
        if tecla[K_g]:
            y_bola = B_praBaixo(y_bola, 587)

   
    if colisao1 or colisao2:
        saque = False

    #ações do 1º jogador
    if tecla[K_w]:
        y_rqt1 = R_praCima(y_rqt1, 120)
    if tecla[K_a]:
        x_rqt1 = R_praEsquerda(x_rqt1, 0)
    if tecla[K_s]:
        y_rqt1 = R_praBaixo(y_rqt1, 530)
    if tecla[K_d]:
        x_rqt1 = R_praDireita(x_rqt1, 240)

    #ações do 2º jogador
    if tecla[K_i]:
        y_rqt2 = R_praCima(y_rqt2, 120) 
    if tecla[K_j]:
        x_rqt2 = R_praEsquerda(x_rqt2, 816)
    if tecla[K_k]:
        y_rqt2 = R_praBaixo(y_rqt2, 530)
    if tecla[K_l]:
        x_rqt2 = R_praDireita(x_rqt2, 1056)
    
    tela.blit(raquete1, (x_rqt1, y_rqt1))
    tela.blit(raquete2, (x_rqt2, y_rqt2))
    tela.blit(bola1, (x_bola, y_bola))
    
    pygame.display.flip()