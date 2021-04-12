import random
import pygame
import numpy as np

# pygame.init()

black = ( 0, 0, 0)

screenw = 600
screenh = 750
# screen = pygame.display.set_mode((screenw,screenh))

tablero = ([0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0])

dado = random.randint(1,6)
# def pieza():
#     for i in range(0, 6):
#         for j in range(0, 5):
#             if tablero[j][i] == 1:
#                 pygame.draw.circle(screen, black, (50, 550), 25)
print (dado)


def mov():
    global posX
    global posY
    if (posX + dado) <= 5:
        tablero[posY][posX] = 0
        tablero[posY][posX+dado] = 1
        posX += dado
    elif (posX + dado) >= 6:
        tablero[posY][posX] = 0
        tablero[posY-1][6-((posX+dado)-5)] = 1
        
posX = 3
posY = 4

mov()

print(posX, posY)
print(tablero)

    #tablero = pygame.image.load("tablero.jpg")
    #bg = pygame.transform.scale(tablero, (screenw, screenh))
    #screen.blit(bg,(0,0))
    #pygame.display.update()