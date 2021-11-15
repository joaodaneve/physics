from random import randint

def B_praCima(y_bolinha, limite):
    y_bolinha-=5

    if y_bolinha < limite:
        y_bolinha = limite
    
    return y_bolinha

def B_praBaixo(y_bolinha, limite):
    y_bolinha+=5

    if y_bolinha > limite:
        y_bolinha = limite
    
    return y_bolinha

def posicionarSaque(posicao_seta):
    posicao_saque = []

    if posicao_seta == [900, 15]:
        posicao_saque = [92, 359]
    else:
        posicao_saque = [1005, 359]

    return posicao_saque

def rebater(x_bola, y_bola):
    vX = randint(4, 8)
    vY = randint(4, 8)
    
    x_bola += vX
    y_bola += vY
    
    direcao = [x_bola, y_bola]
    return direcao

'''def atualizarPosicao():
    Vx = randint(4, 8)
    Vy = randint(-8, 8)
    velocidade = [Vx, Vy]

    return velocidade'''